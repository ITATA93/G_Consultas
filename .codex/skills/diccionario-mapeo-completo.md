# Skill: diccionario-mapeo-completo

## Descripcion
Ejecuta el mapeo completo por niveles de prioridad.
Llama secuencialmente: sync -> generar-md -> verificar actividad (opcional).
El usuario define cuando ejecutar cada nivel.

## Uso
```
/diccionario-mapeo-completo --nivel 0           # Catalogos CT_*
/diccionario-mapeo-completo --nivel 1           # Core PA_*, MR_*
/diccionario-mapeo-completo --nivel 2           # Modulos (questionnaire, lab)
/diccionario-mapeo-completo --nivel 3           # Resto
/diccionario-mapeo-completo --schema SQLUser    # Schema especifico
/diccionario-mapeo-completo --progreso          # Ver estado actual
```

## Niveles de Prioridad

| Nivel | Contenido | Tablas aprox |
|-------|-----------|--------------|
| 0 | Catalogos: CT_*, ARC_*, PAC_*Type* | ~800 |
| 1 | Core: PA_*, MR_*, OE_* (SQLUser) | ~600 |
| 2 | Modulos: questionnaire, lab, websys | ~3,500 |
| 3 | Resto de schemas | ~6,700 |

## Instrucciones

### Nivel 0: Catalogos (bajo riesgo)
```bash
cd "c:\_Consultas\Diccionario_Datos" && \
echo "=== NIVEL 0: CATALOGOS ===" && \
python sincronizar_todo.py --schema SQLUser && \
python generar_md_tablas.py --schema SQLUser --tabla CT_ && \
python generar_md_tablas.py --schema SQLUser --tabla ARC_ && \
python generar_md_tablas.py --schema SQLUser --tabla PAC_ && \
echo "Nivel 0 completado"
```

### Nivel 1: Core clinico
```bash
cd "c:\_Consultas\Diccionario_Datos" && \
echo "=== NIVEL 1: CORE CLINICO ===" && \
python sincronizar_todo.py --schema SQLUser && \
python generar_md_tablas.py --schema SQLUser --tabla PA_ && \
python generar_md_tablas.py --schema SQLUser --tabla MR_ && \
python generar_md_tablas.py --schema SQLUser --tabla OE_ && \
echo "Nivel 1 completado"
```

### Nivel 2: Modulos especificos
```bash
cd "c:\_Consultas\Diccionario_Datos" && \
echo "=== NIVEL 2: MODULOS ===" && \
python sincronizar_todo.py --schema questionnaire && \
python generar_md_tablas.py --schema questionnaire && \
python sincronizar_todo.py --schema lab && \
python generar_md_tablas.py --schema lab && \
python sincronizar_todo.py --schema websys && \
python generar_md_tablas.py --schema websys && \
echo "Nivel 2 completado"
```

### Nivel 3: Resto (ejecutar en partes)
```bash
cd "c:\_Consultas\Diccionario_Datos" && \
echo "=== NIVEL 3: RESTO ===" && \
python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()
# Schemas pendientes (excluir ya procesados)
cur.execute('''
    SELECT s.nombre, COUNT(*) as tablas
    FROM schemas s
    JOIN tablas t ON t.schema_id = s.id
    WHERE s.nombre NOT IN ('SQLUser', 'questionnaire', 'lab', 'websys', 'INFORMATION_SCHEMA')
    GROUP BY s.nombre
    ORDER BY tablas ASC
    LIMIT 10
''')
print('Schemas pendientes (menor a mayor):')
for schema, count in cur.fetchall():
    print(f'  {schema}: {count} tablas')
print()
print('Ejecutar: python sincronizar_todo.py --schema <nombre>')
"
```

### Ver progreso general
```bash
cd "c:\_Consultas\Diccionario_Datos" && python -c "
import sqlite3
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

print('=== PROGRESO DE MAPEO ===')
print()

# Por schema
cur.execute('''
    SELECT s.nombre,
           COUNT(*) as total,
           SUM(CASE WHEN t.fecha_actualizacion IS NOT NULL THEN 1 ELSE 0 END) as mapeadas
    FROM schemas s
    LEFT JOIN tablas t ON t.schema_id = s.id
    GROUP BY s.nombre
    HAVING total > 50
    ORDER BY total DESC
    LIMIT 15
''')
print(f'{\"Schema\":<25} {\"Total\":>8} {\"Mapeadas\":>10} {\"Estado\":>10}')
print('-' * 55)
for schema, total, mapeadas in cur.fetchall():
    pct = (mapeadas / total * 100) if total > 0 else 0
    estado = 'OK' if pct == 100 else f'{pct:.0f}%'
    print(f'{schema:<25} {total:>8} {mapeadas:>10} {estado:>10}')

# Totales
print()
cur.execute('SELECT COUNT(*) FROM tablas')
total = cur.fetchone()[0]
cur.execute('SELECT COUNT(*) FROM tablas WHERE fecha_actualizacion IS NOT NULL')
mapeadas = cur.fetchone()[0]
print(f'TOTAL: {mapeadas:,} / {total:,} tablas ({mapeadas/total*100:.1f}%)')
"
```

## Secuencia recomendada

1. **Primero**: `/diccionario-mapeo-completo --progreso` (ver estado)
2. **Nivel 0**: Catalogos (seguro, rapido)
3. **Nivel 1**: Core clinico (importante)
4. **Nivel 2**: Modulos uno por uno
5. **Nivel 3**: Resto en batches pequeños

## Notas
- Cada nivel es independiente, ejecutar cuando convenga
- El sync actualiza la BD, generar-md crea los documentos
- Verificar `/diccionario-stats` despues de cada nivel
- Si hay error, continuar con el siguiente schema
