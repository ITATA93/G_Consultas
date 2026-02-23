---
name: Buscar Diccionario Datos
description: Herramienta rápida para buscar tablas y columnas en el diccionario local SQLite sin conexión al servidor.
---

# Skill: Buscar Diccionario de Datos

## 🔍 Descripción
Permite consultar la base de datos `diccionario.db` localmente para encontrar tablas, columnas o descripciones que coincidan con un término.

## ⚙️ Cómo usar

### 1. Búsqueda de Tablas
Para encontrar tablas por nombre o descripción:

```powershell
python -c "
import sqlite3
import sys

# CONFIGURACION
DB_PATH = r'c:\_Consultas\Diccionario_Datos\diccionario.db'
TERM = 'TERMINO_A_BUSCAR' # <--- CAMBIAR ESTO

try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print(f'\n--- Resultados TABLAS para: {TERM} ---')
    cur.execute('''
        SELECT s.nombre, t.nombre, t.descripcion
        FROM tablas t
        JOIN schemas s ON t.schema_id = s.id
        WHERE t.nombre LIKE ? OR t.descripcion LIKE ?
        ORDER BY t.nombre LIMIT 20
    ''', ('%'+TERM+'%', '%'+TERM+'%'))
    
    rows = cur.fetchall()
    if not rows: print('No se encontraron tablas.')
    for r in rows:
        print(f'{r[0]}.{r[1]} \n    desc: {r[2]}')
        
    conn.close()
except Exception as e:
    print(f'Error: {e}')
"
```

### 2. Búsqueda de Columnas
Para encontrar qué tabla contiene una columna específica (ej: "Rut", "Diagnosis"):

```powershell
python -c "
import sqlite3
import sys

# CONFIGURACION
DB_PATH = r'c:\_Consultas\Diccionario_Datos\diccionario.db'
TERM = 'TERMINO_A_BUSCAR' # <--- CAMBIAR ESTO

try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print(f'\n--- Resultados COLUMNAS para: {TERM} ---')
    cur.execute('''
        SELECT s.nombre, t.nombre, c.nombre, c.descripcion
        FROM columnas c
        JOIN tablas t ON c.tabla_id = t.id
        JOIN schemas s ON t.schema_id = s.id
        WHERE c.nombre LIKE ? OR c.descripcion LIKE ?
        ORDER BY t.nombre, c.nombre LIMIT 20
    ''', ('%'+TERM+'%', '%'+TERM+'%'))
    
    rows = cur.fetchall()
    if not rows: print('No se encontraron columnas.')
    for r in rows:
        print(f'{r[0]}.{r[1]} -> {r[2]} ({r[3]})')

    conn.close()
except Exception as e:
    print(f'Error: {e}')
"
```
