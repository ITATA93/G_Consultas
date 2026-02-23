"""
Buscar tablas de ordenes (OE_) en LIVE
"""
import iris
from datetime import datetime

# ALMA_CONFIG cargado desde herramientas/python/db_config.py

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    log("Conectando a LIVE...")
    conn = iris.connect(**ALMA_CONFIG)
    cursor = conn.cursor()

    # Buscar tablas OE_
    log("\n=== TABLAS OE_ (Order Entry) ===")
    cursor.execute("""
        SELECT TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = 'SQLUser'
        AND TABLE_NAME LIKE 'OE_%'
        ORDER BY TABLE_NAME
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]}")

    # Contar registros en tablas clave
    log("\n=== CONTEO TABLAS CLAVE ===")
    tablas = ['OE_OrdItem', 'OE_OrdCat', 'OE_OrdSubCat', 'OE_OrdSet', 'OE_OrdGrp']
    for tabla in tablas:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM SQLUser.{tabla}")
            count = cursor.fetchone()[0]
            log(f"  {tabla}: {count} registros")
        except Exception as e:
            log(f"  {tabla}: NO EXISTE")

    # Ver estructura de OE_OrdCat
    log("\n=== MUESTRA OE_OrdCat (Categorias) ===")
    try:
        cursor.execute("SELECT TOP 20 * FROM SQLUser.OE_OrdCat")
        cols = [d[0] for d in cursor.description]
        print(f"  Columnas: {cols}")
        for row in cursor.fetchall():
            print(f"  {row}")
    except Exception as e:
        log(f"  Error: {e}")

    # Ver estructura de OE_OrdItem
    log("\n=== MUESTRA OE_OrdItem (Items) TOP 10 ===")
    try:
        cursor.execute("SELECT TOP 10 * FROM SQLUser.OE_OrdItem")
        cols = [d[0] for d in cursor.description]
        print(f"  Columnas: {cols[:10]}...")  # Solo primeras 10 columnas
    except Exception as e:
        log(f"  Error: {e}")

    conn.close()
    log("\nCompletado")

if __name__ == "__main__":
    main()
