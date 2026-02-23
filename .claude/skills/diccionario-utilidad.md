# Skill: diccionario-utilidad

## Descripcion
Permite agregar o actualizar la descripcion de utilidad de una tabla.
La utilidad puede ser clinica, administrativa, tecnica, o cualquier otra.
Esta informacion aparece en la seccion "## Utilidad" de los MD generados.

## Uso
```
/diccionario-utilidad PA_Adm "Tabla principal de admisiones/episodios de pacientes"
/diccionario-utilidad --schema SQLUser --tabla PA_Adm "Descripcion..."
/diccionario-utilidad --listar-vacias --limite 10
```

## Instrucciones

### Agregar utilidad a una tabla
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
import sys

tabla = 'NOMBRE_TABLA'  # Reemplazar con nombre de tabla
utilidad = '''DESCRIPCION'''  # Reemplazar con descripcion

conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

# Buscar tabla
cur.execute('''
    SELECT t.id, s.nombre, t.nombre, t.uso_clinico
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.nombre = ? OR t.nombre LIKE ?
''', (tabla, f'%{tabla}%'))
rows = cur.fetchall()

if not rows:
    print(f'No se encontro tabla: {tabla}')
    sys.exit(1)

if len(rows) > 1:
    print(f'Multiples tablas encontradas:')
    for r in rows:
        print(f'  {r[1]}.{r[2]}')
    sys.exit(1)

tabla_id, schema, nombre, uso_actual = rows[0]
print(f'Tabla: {schema}.{nombre}')
print(f'Uso actual: {uso_actual or \"(vacio)\"}')

# Actualizar
cur.execute('UPDATE tablas SET uso_clinico = ? WHERE id = ?', (utilidad, tabla_id))
conn.commit()
print(f'Actualizado: {utilidad[:50]}...')
"
```

### Listar tablas sin utilidad documentada
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    SELECT s.nombre, t.nombre
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.uso_clinico IS NULL OR t.uso_clinico = ''
    ORDER BY s.nombre, t.nombre
    LIMIT 20
''')
print('Tablas sin utilidad documentada:')
for schema, tabla in cur.fetchall():
    print(f'  {schema}.{tabla}')
"
```

### Regenerar MD despues de actualizar
Despues de actualizar la utilidad, regenerar el MD de la tabla:
```bash
cd "c:\_Consultas\Diccionario_Datos" && python generar_md_tablas.py --tabla NOMBRE_TABLA
```

## Ejemplos de utilidad

- **PA_Adm**: "Tabla principal de admisiones y episodios clinicos. Cada fila representa una visita/hospitalizacion."
- **PA_PatMas**: "Datos demograficos del paciente (nombre, RUT, fecha nacimiento). Tabla maestra de pacientes."
- **CT_Loc**: "Catalogo de ubicaciones/servicios del hospital. Usado para asignar camas y unidades."
- **OE_Ord**: "Ordenes medicas (laboratorio, imagenes, procedimientos). Seguimiento de solicitudes."

## Notas
- El campo `uso_clinico` acepta texto largo (sin limite)
- Puede incluir uso clinico, administrativo, tecnico, etc.
- Se recomienda describir: que datos contiene, para que se usa, y con que tablas se relaciona
