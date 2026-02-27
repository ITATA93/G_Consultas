import sqlite3

db_path = r"c:\01_HOSPITAL_PRIVADO\G_Consultas\Diccionario_Datos\diccionario.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

with open(r"c:\01_HOSPITAL_PRIVADO\G_Consultas\search_results.txt", "w", encoding="utf-8") as f:
    def search_term(term):
        f.write(f"\n=== SEARCHING FOR '{term}' ===\n")

        query_tablas = f"""
        SELECT nombre, nombre_completo, descripcion, descripcion_es
        FROM tablas
        WHERE nombre LIKE '%{term}%'
           OR nombre_completo LIKE '%{term}%'
           OR descripcion LIKE '%{term}%'
           OR descripcion_es LIKE '%{term}%'
        """
        cur.execute(query_tablas)
        tables = cur.fetchall()
        f.write(f"--- TABLES MATCHING '{term}' ({len(tables)}) ---\n")
        for t in tables[:100]:
            f.write(str(t) + "\n")

        query_columnas = f"""
        SELECT t.nombre_completo, c.nombre, c.descripcion, c.descripcion_es
        FROM columnas c
        JOIN tablas t ON c.tabla_id = t.id
        WHERE c.nombre LIKE '%{term}%'
           OR c.descripcion LIKE '%{term}%'
           OR c.descripcion_es LIKE '%{term}%'
        """
        cur.execute(query_columnas)
        columns = cur.fetchall()
        f.write(f"--- COLUMNS MATCHING '{term}' ({len(columns)}) ---\n")
        for c in columns[:100]:
            f.write(str(c) + "\n")

    search_term('llamad')
    search_term('consultori')

conn.close()
