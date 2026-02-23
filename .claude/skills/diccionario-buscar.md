# Skill: diccionario-buscar

## Descripcion
Busca tablas o columnas en el Diccionario de Datos ALMA.
NO consulta el servidor - solo busca en la base de datos local.

**Incluye trazabilidad:** Muestra fecha de mapeo/actualizacion de cada resultado.

## Uso
```
/diccionario-buscar <termino>
/diccionario-buscar paciente
/diccionario-buscar PA_Adm
```

## Instrucciones
Segun el termino de busqueda, ejecutar consultas SQLite:

### Buscar tablas:
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    SELECT s.nombre as schema, t.nombre, t.descripcion,
           (SELECT COUNT(*) FROM columnas c WHERE c.tabla_id = t.id) as cols,
           t.fecha_mapeo, t.fecha_actualizacion
    FROM tablas t
    JOIN schemas s ON t.schema_id = s.id
    WHERE t.nombre LIKE '%TERMINO%' OR t.descripcion LIKE '%TERMINO%'
    ORDER BY t.nombre
    LIMIT 20
''')
for row in cur.fetchall():
    fecha = row[5] or row[4] or '?'
    print(f'{row[0]}.{row[1]} ({row[3]} cols) [{fecha[:10]}] - {row[2] or \"-\"}')
conn.close()
"
```

### Buscar columnas:
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
cur.execute('''
    SELECT s.nombre || \".\" || t.nombre as tabla, c.nombre, c.tipo_dato, c.descripcion
    FROM columnas c
    JOIN tablas t ON c.tabla_id = t.id
    JOIN schemas s ON t.schema_id = s.id
    WHERE c.nombre LIKE '%TERMINO%' OR c.descripcion LIKE '%TERMINO%'
    ORDER BY c.nombre
    LIMIT 20
''')
for row in cur.fetchall():
    print(f'{row[0]}.{row[1]} ({row[2]}) - {row[3] or \"-\"}')
conn.close()
"
```

Reemplazar TERMINO con lo que busque el usuario.
