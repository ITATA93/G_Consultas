import pyodbc

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

def main():
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SIDRA_CONFIG['server']};"
            f"DATABASE={SIDRA_CONFIG['database']};"
            f"UID={SIDRA_CONFIG['username']};"
            f"PWD={SIDRA_CONFIG['password']}"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        print("Checking schema for ALMA_Reportes.CAL_RiesgoETE...")
        
        sql = """
        SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'ALMA_Reportes' AND TABLE_NAME = 'CAL_RiesgoETE'
        """
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(f"{row[0]}: {row[1]} ({row[2]})")
            
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
