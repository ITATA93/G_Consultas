# Skill: diccionario-actividad

## Descripcion
Verifica si las tablas tienen datos (estan activas) consultando el servidor.
Usa metodo liviano (EXISTS/TOP 1) para no saturar el servidor.
Guarda resultado en campo `tiene_datos` de la tabla.

**IMPORTANTE**: Ejecutar por schema para no saturar el servidor.

## Uso
```
/diccionario-actividad --schema SQLUser        # Verificar un schema
/diccionario-actividad --schema CT --prefijo   # Solo tablas CT_*
/diccionario-actividad --listar-vacias         # Listar tablas sin datos verificados
/diccionario-actividad --stats                 # Estadisticas de actividad
```

## Campos en SQLite (tabla `tablas`)
```sql
-- Agregar campos si no existen
ALTER TABLE tablas ADD COLUMN tiene_datos INTEGER DEFAULT NULL;  -- NULL=no verificado, 0=vacia, 1=tiene datos
ALTER TABLE tablas ADD COLUMN registros_aprox INTEGER DEFAULT NULL;  -- Opcional: conteo aproximado
ALTER TABLE tablas ADD COLUMN ultima_verificacion TEXT DEFAULT NULL;  -- Fecha de verificacion
```

## Instrucciones

### Verificar actividad de un schema (liviano)
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
import iris  # intersystems_irispython

SCHEMA = 'SQLUser'  # Cambiar segun necesidad
LIMITE = 50  # Tablas por ejecucion

# Conectar
conn_sqlite = sqlite3.connect('diccionario.db')
cur = conn_sqlite.cursor()

# Leer credenciales
with open('../credentials/alma_iris.txt', 'r') as f:
    lines = f.readlines()
    user = lines[0].strip()
    pwd = lines[1].strip()

conn_iris = iris.connect('10.63.180.25', 51773, 'LIVE-CLOV', user, pwd)
cursor_iris = conn_iris.cursor()

# Obtener tablas del schema sin verificar
cur.execute('''
    SELECT t.id, s.nombre, t.nombre
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE s.nombre = ? AND t.ultima_verificacion IS NULL
    LIMIT ?
''', (SCHEMA, LIMITE))
tablas = cur.fetchall()

print(f'Verificando {len(tablas)} tablas de {SCHEMA}...')

from datetime import datetime
ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for tabla_id, schema, nombre in tablas:
    try:
        # Metodo liviano: EXISTS (para al primer registro)
        cursor_iris.execute(f'SELECT TOP 1 1 FROM {schema}.{nombre}')
        tiene = 1 if cursor_iris.fetchone() else 0

        cur.execute('''
            UPDATE tablas
            SET tiene_datos = ?, ultima_verificacion = ?
            WHERE id = ?
        ''', (tiene, ts, tabla_id))

        estado = 'ACTIVA' if tiene else 'VACIA'
        print(f'  {schema}.{nombre}: {estado}')
    except Exception as e:
        print(f'  {schema}.{nombre}: ERROR - {str(e)[:50]}')

conn_sqlite.commit()
conn_iris.close()
print(f'Verificacion completada: {len(tablas)} tablas')
"
```

### Ver estadisticas de actividad
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

print('=== ESTADISTICAS DE ACTIVIDAD ===')

cur.execute('SELECT COUNT(*) FROM tablas WHERE tiene_datos = 1')
activas = cur.fetchone()[0]

cur.execute('SELECT COUNT(*) FROM tablas WHERE tiene_datos = 0')
vacias = cur.fetchone()[0]

cur.execute('SELECT COUNT(*) FROM tablas WHERE tiene_datos IS NULL')
sin_verificar = cur.fetchone()[0]

total = activas + vacias + sin_verificar
print(f'Tablas activas (con datos): {activas:,}')
print(f'Tablas vacias (sin datos):  {vacias:,}')
print(f'Sin verificar:              {sin_verificar:,}')
print(f'Total:                      {total:,}')

if activas + vacias > 0:
    pct = (activas / (activas + vacias)) * 100
    print(f'Porcentaje activas:         {pct:.1f}%')
"
```

### Listar tablas sin verificar por schema
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    SELECT s.nombre, COUNT(*) as pendientes
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.tiene_datos IS NULL
    GROUP BY s.nombre
    ORDER BY pendientes DESC
    LIMIT 20
''')
print('Schemas con tablas sin verificar:')
for schema, count in cur.fetchall():
    print(f'  {schema}: {count:,} tablas')
"
```

### Listar tablas vacias de un schema
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    SELECT t.nombre, t.ultima_verificacion
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE s.nombre = 'SQLUser' AND t.tiene_datos = 0
    ORDER BY t.nombre
''')
print('Tablas vacias en SQLUser:')
for nombre, fecha in cur.fetchall():
    print(f'  {nombre} (verificado: {fecha})')
"
```

## Notas de rendimiento
- `SELECT TOP 1 1` es muy liviano (para al primer registro)
- Procesar maximo 50 tablas por ejecucion
- Esperar entre ejecuciones si el servidor esta lento
- Priorizar schemas importantes: SQLUser, questionnaire

## Mostrar en MD
Despues de verificar, regenerar MDs para mostrar estado:
```bash
python generar_md_tablas.py --schema SQLUser
```
El MD mostrara: `**Estado:** Activa` o `**Estado:** Sin datos`
