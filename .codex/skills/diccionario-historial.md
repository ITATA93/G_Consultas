# Skill: diccionario-historial

## Descripcion
Muestra el historial de sincronizaciones del Diccionario de Datos.
Permite ver cuando se hicieron las ultimas sincronizaciones y sus estadisticas.

## Uso
```
/diccionario-historial
/diccionario-historial --limite 5
```

## Instrucciones
Ejecutar:

```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

# Metadata
print('=== METADATA ===')
cur.execute('SELECT clave, valor, actualizado FROM metadata')
for clave, valor, fecha in cur.fetchall():
    print(f'{clave}: {valor} (actualizado: {fecha})')

# Historial
print()
print('=== HISTORIAL DE SINCRONIZACIONES ===')
cur.execute('''
    SELECT fecha, tipo, schemas_total, tablas_total, columnas_total,
           tablas_nuevas, tablas_actualizadas, duracion_seg
    FROM sync_log
    ORDER BY id DESC
    LIMIT 10
''')
for row in cur.fetchall():
    fecha, tipo, schemas, tablas, cols, nuevas, actualizadas, dur = row
    print(f'{fecha} [{tipo}] - {tablas} tablas, {cols} cols (nuevas: {nuevas}, act: {actualizadas}) [{dur:.1f}s]')

conn.close()
"
```

## Informacion mostrada
- Version del diccionario
- Fecha de ultima sincronizacion con servidor
- Fecha de ultima exportacion
- Ultimas 10 sincronizaciones con:
  - Fecha y hora
  - Tipo (servidor/local)
  - Total de tablas y columnas
  - Tablas nuevas y actualizadas
  - Duracion de la operacion
