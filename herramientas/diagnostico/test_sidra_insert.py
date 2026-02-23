import pyodbc
import os
from datetime import datetime

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
        conn = pyodbc.connect(conn_str, autocommit=True)
        cursor = conn.cursor()
        
        print("Intentando INSERT directo...")
        
        sql = """
        INSERT INTO ALMA_Reportes.CAL_RiesgoETE (
            ID_Row, Paciente_RUN, Paciente_Nombre, Episodio_Admision, 
            Fecha_Admision, Ubicacion_Actual, Tiene_Caprini, Form_ID, 
            Form_Fecha, Form_Usuario, Edad, Tipo_Cirugia, Evento_Reciente, 
            Enf_Venosa_Coagulacion, Movilidad, Antecedentes_Otros, 
            Score_Total, Clasificacion_Riesgo, Fecha_Proceso
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, GETDATE())
        """
        
        # Data de prueba (Dummy)
        params = (
            'TEST_ROW_001', '12345678', 'JUAN PEREZ', 'EPISODIO_TEST', 
            datetime.now(), 'UBICACION TEST', 1, 'FORM_TEST', 
            datetime.now(), 'USUARIO TEST', 'TEST', 'TEST', 0, 0, 'TEST', 'TEST', 3, 'TEST'
        )
        
        cursor.execute(sql, params)
        print("INSERT ejecutado.")
        
        count = cursor.execute("SELECT COUNT(*) FROM ALMA_Reportes.CAL_RiesgoETE WHERE ID_Row = 'TEST_ROW_001'").fetchone()[0]
        print(f"Verificacion (Count TEST): {count}")
        
        if count > 0:
            cursor.execute("DELETE FROM ALMA_Reportes.CAL_RiesgoETE WHERE ID_Row = 'TEST_ROW_001'")
            print("Limpieza ejecutada.")
            
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
