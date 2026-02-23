import sqlite3
import os

DB_PATH = r'c:/_Repositorio/AG_Proyectos/AG_Consultas/Diccionario_Datos/diccionario.db'
OUT_FILE = r'c:/_Repositorio/AG_Proyectos/AG_Consultas/herramientas/schema_dump.txt'

def main():
    if not os.path.exists(DB_PATH):
        with open(OUT_FILE, 'w') as f:
            f.write(f"Error: DB not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(OUT_FILE, 'w') as f:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        f.write(f"Tablas: {tables}\n\n")

        for t in tables:
            f.write(f"--- Schema of {t} ---\n")
            cursor.execute(f"PRAGMA table_info({t})")
            cols = cursor.fetchall()
            for c in cols:
                f.write(f"{c}\n")
            f.write("\n")

    conn.close()

if __name__ == '__main__':
    main()
