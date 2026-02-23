# Skill: diccionario-documentar-tabla

## Descripcion
Flujo guiado para documentar completamente UNA tabla.
Ejecuta en orden: sync → utilidad → ejemplos → generar MD.

## Uso
```
/diccionario-documentar-tabla PA_Adm
/diccionario-documentar-tabla --schema SQLUser --tabla CT_Loc
```

## Flujo completo

### Paso 1: Verificar/Sincronizar tabla
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

TABLA = 'NOMBRE_TABLA'  # Reemplazar

cur.execute('''
    SELECT t.id, s.nombre, t.nombre, t.descripcion, t.uso_clinico,
           (SELECT COUNT(*) FROM columnas WHERE tabla_id = t.id) as cols
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.nombre = ?
''', (TABLA,))
row = cur.fetchone()

if row:
    print(f'Tabla: {row[1]}.{row[2]}')
    print(f'Descripcion: {row[3] or \"(sin descripcion)\"}')
    print(f'Columnas: {row[5]}')
    print(f'Utilidad: {row[4] or \"(PENDIENTE)\"}')
else:
    print(f'Tabla no encontrada: {TABLA}')
    print('Ejecutar primero: python sincronizar_todo.py --schema <schema>')
"
```

### Paso 2: Agregar utilidad
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

TABLA = 'NOMBRE_TABLA'
UTILIDAD = '''
DESCRIPCION DE LA TABLA:
- Para que se usa
- Que datos contiene
- Con que tablas se relaciona
'''

cur.execute('SELECT id FROM tablas WHERE nombre = ?', (TABLA,))
row = cur.fetchone()
if row:
    cur.execute('UPDATE tablas SET uso_clinico = ? WHERE id = ?', (UTILIDAD.strip(), row[0]))
    conn.commit()
    print(f'Utilidad agregada a {TABLA}')
"
```

### Paso 3: Agregar ejemplos (solo columnas seguras)
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

TABLA = 'NOMBRE_TABLA'

# Ejemplos por columna (agregar manualmente)
EJEMPLOS = {
    'COLUMNA1': 'valor1, valor2, valor3',
    'COLUMNA2': 'ejemplo1, ejemplo2',
}

cur.execute('''
    SELECT c.id, c.nombre
    FROM columnas c
    JOIN tablas t ON c.tabla_id = t.id
    WHERE t.nombre = ?
''', (TABLA,))

for col_id, col_nombre in cur.fetchall():
    if col_nombre in EJEMPLOS:
        cur.execute('UPDATE columnas SET valores_ejemplo = ? WHERE id = ?',
                   (EJEMPLOS[col_nombre], col_id))
        print(f'  {col_nombre}: {EJEMPLOS[col_nombre]}')

conn.commit()
print(f'Ejemplos agregados a {TABLA}')
"
```

### Paso 4: Regenerar MD
```bash
cd "c:\_Consultas\Diccionario_Datos" && python generar_md_tablas.py --tabla NOMBRE_TABLA
```

### Paso 5: Verificar resultado
```bash
cat "c:\_Consultas\Diccionario_Datos\tablas_md\SQLUser\NOMBRE_TABLA.md" | head -30
```

## Ejemplo completo para CT_Loc

```bash
# 1. Verificar
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('SELECT id FROM tablas WHERE nombre = \"CT_Loc\"')
print('CT_Loc encontrada' if cur.fetchone() else 'No encontrada')
"

# 2. Agregar utilidad
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    UPDATE tablas SET uso_clinico = 'Catalogo de ubicaciones/servicios del hospital. Define unidades clinicas, servicios y areas donde se asignan camas y pacientes.'
    WHERE nombre = 'CT_Loc'
''')
conn.commit()
print('Utilidad agregada')
"

# 3. Agregar ejemplos
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    UPDATE columnas SET valores_ejemplo = 'URG, UCI, PED, MED'
    WHERE nombre = 'CTLOC_Code'
    AND tabla_id = (SELECT id FROM tablas WHERE nombre = 'CT_Loc')
''')
conn.commit()
print('Ejemplos agregados')
"

# 4. Regenerar MD
python generar_md_tablas.py --tabla CT_Loc
```

## Notas
- Reemplazar NOMBRE_TABLA en cada paso
- Los ejemplos son opcionales (solo para columnas clave)
- Evitar datos personales en ejemplos
- Regenerar MD al final para ver cambios
