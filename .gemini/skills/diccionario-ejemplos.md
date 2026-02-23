# Skill: diccionario-ejemplos

## Descripcion
Obtiene valores de ejemplo para las columnas de una tabla desde el servidor.
Los ejemplos se guardan en el campo `valores_ejemplo` de la tabla columnas.

**IMPORTANTE**: Solo obtiene datos NO identificables:
- Excluye columnas con nombres sensibles (Name, RUT, Address, Phone, etc.)
- Solo muestra valores distintos (DISTINCT)
- Limita a 3 ejemplos por columna
- NO obtiene datos de tablas de pacientes directamente

## Uso
```
/diccionario-ejemplos CT_Loc                    # Ejemplos de tabla de catalogos
/diccionario-ejemplos --schema SQLUser --tabla CT_Loc
/diccionario-ejemplos --solo-catalogos         # Solo tablas CT_* (seguras)
```

## Instrucciones

### Obtener ejemplos de una tabla de catalogo (CT_*)
Las tablas CT_* son catalogos/maestros y son seguras para obtener ejemplos.

```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3

# Configuracion
TABLA = 'CT_Loc'  # Reemplazar con nombre de tabla
LIMITE_EJEMPLOS = 3

# Columnas a excluir (datos sensibles)
EXCLUIR_PATRONES = [
    'Name', 'Nombre', 'RUT', 'DNI', 'Address', 'Direccion',
    'Phone', 'Telefono', 'Email', 'Password', 'Token',
    'PAPMI', 'PatMas'  # Referencias a pacientes
]

def es_columna_sensible(nombre):
    nombre_upper = nombre.upper()
    for patron in EXCLUIR_PATRONES:
        if patron.upper() in nombre_upper:
            return True
    return False

# Conectar a SQLite
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

# Buscar tabla
cur.execute('''
    SELECT t.id, s.nombre, t.nombre
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.nombre = ?
''', (TABLA,))
row = cur.fetchone()
if not row:
    print(f'Tabla no encontrada: {TABLA}')
    exit(1)

tabla_id, schema, nombre = row
print(f'Tabla: {schema}.{nombre}')

# Obtener columnas
cur.execute('''
    SELECT id, nombre, tipo_dato
    FROM columnas
    WHERE tabla_id = ?
''', (tabla_id,))
columnas = cur.fetchall()

print(f'Columnas: {len(columnas)}')
print()

# Para cada columna no sensible, mostrar query de ejemplo
for col_id, col_nombre, tipo in columnas:
    if es_columna_sensible(col_nombre):
        print(f'  SKIP (sensible): {col_nombre}')
        continue

    # Query para obtener ejemplos (ejecutar manualmente en servidor)
    query = f'SELECT DISTINCT TOP {LIMITE_EJEMPLOS} \"{col_nombre}\" FROM {schema}.{nombre} WHERE \"{col_nombre}\" IS NOT NULL'
    print(f'  {col_nombre}: {query}')
"
```

### Actualizar ejemplos manualmente
Despues de obtener los ejemplos del servidor:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3

# Configuracion
TABLA = 'CT_Loc'
COLUMNA = 'CTLOC_Code'
EJEMPLOS = 'URG, UCI, PED'  # Valores separados por coma

conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

# Buscar columna
cur.execute('''
    SELECT c.id
    FROM columnas c
    JOIN tablas t ON c.tabla_id = t.id
    WHERE t.nombre = ? AND c.nombre = ?
''', (TABLA, COLUMNA))
row = cur.fetchone()

if row:
    cur.execute('UPDATE columnas SET valores_ejemplo = ? WHERE id = ?', (EJEMPLOS, row[0]))
    conn.commit()
    print(f'Actualizado: {TABLA}.{COLUMNA} = {EJEMPLOS}')
else:
    print(f'No encontrado: {TABLA}.{COLUMNA}')
"
```

### Regenerar MD despues de actualizar
```bash
cd "c:\_Consultas\Diccionario_Datos" && python generar_md_tablas.py --tabla NOMBRE_TABLA
```

## Tablas seguras para ejemplos
- `CT_*` - Catalogos y maestros
- `ARC_*` - Archetypes
- `PAC_*Type*` - Tipos de admision
- `RBC_*` - Configuracion de agenda

## Tablas NO seguras (evitar)
- `PA_PatMas` - Datos de pacientes
- `PA_Adm` - Admisiones (tiene datos de pacientes)
- `MR_*` - Registros medicos
- Cualquier tabla con datos personales

## Notas
- Los ejemplos aparecen en columna "Ejemplo" del MD solo si existen
- Campo `valores_ejemplo` en SQLite (texto libre)
- Formato recomendado: valores separados por coma
