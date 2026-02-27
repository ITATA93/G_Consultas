import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from herramientas.python.db_config import conectar_alma

def test_query():
    print("Iniciando prueba liviana de Pabellón...")
    try:
        conn = conectar_alma()
        print("Conectado a ALMA (LIVE-CLOV).")

        sql_path = Path(__file__).resolve().parent.parent.parent / "Consultas_live" / "consulta_consolidada_pabellon.sql"
        with open(sql_path, "r", encoding="utf-8") as f:
            sql_query = f.read()

        print("Ejecutando consulta...")
        cursor = conn.cursor()
        cursor.execute(sql_query)

        # Print column names
        columns = [column[0] for column in cursor.description]
        print("\nColumnas encontradas:", ", ".join(columns[:5]), "...")

        # Fetch up to 5 rows
        rows = cursor.fetchmany(5)
        print(f"\nSe obtuvieron {len(rows)} resultados de muestra:")
        for idx, row in enumerate(rows):
            print(f"--- Fila {idx + 1} ---")
            for col_name, value in zip(columns, row):
                if value:
                    print(f"  {col_name}: {str(value)[:50]}")

        cursor.close()
        conn.close()
        print("\nPrueba finalizada exitosamente.")

    except Exception as e:
        print(f"Error al ejecutar: {e}")

if __name__ == "__main__":
    test_query()
