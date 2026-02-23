"""
Sincronizar diccionarios clinicos adicionales LIVE -> SIDRA
Version con descubrimiento automatico de columnas
"""
import iris
import pyodbc
from datetime import datetime

# ALMA_CONFIG cargado desde herramientas/python/db_config.py

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# (schema_sidra, tabla_sidra, tabla_live)
DICCIONARIOS = [
    ('ALMA_Clinico', 'DIC_CategoriasOrden', 'OE_OrdCateg'),
    ('ALMA_Clinico', 'DIC_SubcategoriasOrden', 'OE_OrdSubCateg'),
    ('ALMA_Clinico', 'DIC_Prioridades', 'OEC_Priority'),
    ('ALMA_Clinico', 'DIC_CategoriasInterconsulta', 'OEC_ConsultCateg'),
    ('ALMA_Clinico', 'DIC_ItemsOrden', 'OE_OrdItem'),
    ('ALMA_Estructura', 'DIC_TiposVisita', 'PAC_VisitType'),
    ('ALMA_Estructura', 'DIC_TiposCuidado', 'PAC_CareType'),
    ('ALMA_Estructura', 'DIC_TiposAdmision', 'PAC_InPatAdmissionType'),
    ('ALMA_Estructura', 'DIC_TiposPaciente', 'PAC_PatientType'),
    ('ALMA_Estructura', 'DIC_TiposDerivacion', 'PAC_ReferralType'),
]

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def get_columns(cursor, tabla):
    """Obtiene columnas de una tabla en LIVE"""
    cursor.execute(f"SELECT TOP 1 * FROM SQLUser.{tabla}")
    return [d[0] for d in cursor.description]

def create_table_sql(schema, tabla, columns, sample_row):
    """Genera SQL para crear tabla en SIDRA"""
    col_defs = []
    for i, col in enumerate(columns):
        val = sample_row[i] if sample_row else None
        if 'RowId' in col or col.endswith('_DR'):
            col_defs.append(f"{col} INT")
        elif isinstance(val, (int, float)) or 'Num' in col:
            col_defs.append(f"{col} INT")
        else:
            col_defs.append(f"{col} NVARCHAR(500)")
    return f"CREATE TABLE {schema}.{tabla} ({', '.join(col_defs)})"

def main():
    log("Conectando a LIVE...")
    conn_alma = iris.connect(**ALMA_CONFIG)
    cursor_alma = conn_alma.cursor()

    log("Conectando a SIDRA...")
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SIDRA_CONFIG['server']};DATABASE={SIDRA_CONFIG['database']};UID={SIDRA_CONFIG['username']};PWD={SIDRA_CONFIG['password']}"
    conn_sidra = pyodbc.connect(conn_str, autocommit=True)
    cursor_sidra = conn_sidra.cursor()

    total = 0
    for schema, tabla_sidra, tabla_live in DICCIONARIOS:
        tabla_completa = f"{schema}.{tabla_sidra}"
        log(f"\n--- {tabla_sidra} ({tabla_live}) ---")

        # Obtener datos de LIVE
        try:
            cursor_alma.execute(f"SELECT * FROM SQLUser.{tabla_live}")
            columns = [d[0] for d in cursor_alma.description]
            rows = cursor_alma.fetchall()
            log(f"  Extraidos: {len(rows)} registros, {len(columns)} columnas")
        except Exception as e:
            log(f"  ERROR extrayendo: {str(e)[:80]}")
            continue

        if len(rows) == 0:
            log("  Sin datos")
            continue

        # Verificar/crear tabla en SIDRA
        try:
            cursor_sidra.execute(f"SELECT TOP 1 * FROM {tabla_completa}")
        except:
            log(f"  Creando tabla...")
            try:
                # Tomar solo columnas principales (Code, Desc, RowId)
                main_cols = [c for c in columns if 'Code' in c or 'Desc' in c or 'RowId' in c][:5]
                if not main_cols:
                    main_cols = columns[:5]
                col_defs = ', '.join([f"{c} NVARCHAR(500)" for c in main_cols])
                cursor_sidra.execute(f"CREATE TABLE {tabla_completa} ({col_defs})")
                columns = main_cols
            except Exception as e:
                log(f"  ERROR creando: {str(e)[:80]}")
                continue

        # Obtener columnas de SIDRA
        try:
            cursor_sidra.execute(f"SELECT TOP 0 * FROM {tabla_completa}")
            sidra_cols = [d[0] for d in cursor_sidra.description]
        except:
            sidra_cols = columns[:5]

        # Limpiar e insertar
        try:
            cursor_sidra.execute(f"DELETE FROM {tabla_completa}")
            placeholders = ','.join(['?' for _ in sidra_cols])
            sql = f"INSERT INTO {tabla_completa} ({','.join(sidra_cols)}) VALUES ({placeholders})"

            # Mapear columnas LIVE -> SIDRA
            col_indices = []
            for sc in sidra_cols:
                for i, c in enumerate(columns):
                    if c == sc:
                        col_indices.append(i)
                        break
                else:
                    col_indices.append(None)

            inserted = 0
            for row in rows:
                try:
                    values = [row[i] if i is not None else None for i in col_indices]
                    cursor_sidra.execute(sql, values)
                    inserted += 1
                except:
                    pass

            log(f"  Cargados: {inserted} registros")
            total += inserted
        except Exception as e:
            log(f"  ERROR cargando: {str(e)[:80]}")

    log(f"\n{'='*40}")
    log(f"TOTAL: {total} registros")

    conn_alma.close()
    conn_sidra.close()

if __name__ == "__main__":
    main()
