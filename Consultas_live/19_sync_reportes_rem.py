"""
Sincronizacion de Reportes REM y Otros: ALMA -> SIDRA
Hospital Dr. Antonio Tirado Lanas - Ovalle

Extrae reportes estadisticos desde TrakCare (ALMA) y los carga en SQL Server (SIDRA).
- Reportes REM (Resumen Estadistico Mensual): 46 tablas QREM*
- Reportes Urgencias: QCLXXBENEUR, QCLXXREPRAU, QCLXXSAMUR
- Reportes Salud Mental: QCLXXFISMUR

Prerequisitos:
  1. Ejecutar 18_crear_schemas_reportes.sql en SIDRA
  2. pip install intersystems-iris pyodbc

Uso:
  python 19_sync_reportes_rem.py                    # Sincronizar todo
  python 19_sync_reportes_rem.py --schema REM      # Solo reportes REM
  python 19_sync_reportes_rem.py --tabla QREMA04E  # Solo una tabla
"""

import iris
import pyodbc
from datetime import datetime
import argparse
import sys

# ============================================
# CONFIGURACION
# ============================================
# ALMA_CONFIG cargado desde herramientas/python/db_config.py

# SIDRA_CONFIG cargado desde herramientas/python/db_config.py

# ============================================
# DEFINICION DE TABLAS POR SCHEMA
# ============================================
TABLAS_REPORTES = {
    'ALMA_Reportes_REM': [
        # REM A01 - Controles en Establecimientos Educacionales
        'QREMA01E', 'QREMA01EI',
        # REM A04 - Consultas de Morbilidad y Regulacion
        'QREMA04E', 'QREMA04E1', 'QREMA04K', 'QREMA04KQQ16', 'QREMA04SE',
        # REM A05 - Servicio Itinerante
        'QREMA05F2',
        # REM A06 - Coordinacion e Informes
        'QREMA06C1', 'QREMA06C2',
        # REM A08 - Urgencias y SAMU
        'QREMA08J', 'QREMA08K',
        # REM A09 - Gestion Dental
        'QREMA09SK',
        # REM A19 - Promocion y Participacion
        'QREMA19AB4', 'QREMA19ASB1', 'QREMA19ASB2',
        'QREMA19BSA', 'QREMA19BSB', 'QREMA19BSC',
        # REM A21 - Hospitalizacion Domiciliaria
        'QREMA21C1', 'QREMA21C2', 'QREMA21C3', 'QREMA21D1', 'QREMA21D2',
        # REM A23 - Morbilidad e Inasistencias
        'QREMA23SG', 'QREMA23SH', 'QREMA23SM2',
        # REM A24 - IVE
        'QREMA24A1',
        # REM A27 - Programa Adultos Mayores
        'QREMA27F', 'QREMA27I', 'QREMA27J',
        # REM A28 - Actividades
        'QREMA28SA12',
        # REM A30 - Telemedicina
        'QREMA30B', 'QREMA30C', 'QREMA30D', 'QREMA30DQQ03', 'QREMA30E',
        # REM A32 - Elige Vida Sana
        'QREMA32R', 'QREMA32S',
        # REM B17 - Farmacia y Tamizaje
        'QREMB17IIJ', 'QREMB17IIM',
        # REM BM18 - Traslados y COVID
        'QREMBM18H', 'QREMBM18J',
        # REM D15 - Reevaluaciones
        'QREMD15F',
        # Otros REM
        'QREM17SL', 'QREM27SL',
    ],
    'ALMA_Reportes_Urgencias': [
        'QCLXXBENEUR',   # Beneficios de Salud en Urgencia
        'QCLXXREPRAU',   # Auditoria Reporte Atencion Urgencia
        'QCLXXSAMUR',    # Solicitud Antimicrobianos Uso Restringido
    ],
    'ALMA_Reportes_SaludMental': [
        'QCLXXFISMUR',   # Ficha Ingreso Salud Mental desde Urgencia
    ],
}

# Alias para filtro por linea de comandos
SCHEMA_ALIASES = {
    'REM': 'ALMA_Reportes_REM',
    'URGENCIAS': 'ALMA_Reportes_Urgencias',
    'SALUDMENTAL': 'ALMA_Reportes_SaludMental',
}

# ============================================
# FUNCIONES AUXILIARES
# ============================================
def log(msg):
    """Imprime mensaje con timestamp"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def conectar_alma():
    """Conecta a ALMA (InterSystems IRIS)"""
    return iris.connect(**ALMA_CONFIG)

def conectar_sidra():
    """Conecta a SIDRA (SQL Server)"""
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SIDRA_CONFIG['server']};"
        f"DATABASE={SIDRA_CONFIG['database']};"
        f"UID={SIDRA_CONFIG['username']};"
        f"PWD={SIDRA_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str, timeout=30, autocommit=True)

def mapear_tipo_iris_sqlserver(tipo_iris, nombre_col):
    """Mapea tipos de datos de IRIS a SQL Server"""
    tipo_str = str(tipo_iris).lower() if tipo_iris else ''

    # ID siempre es BIGINT
    if nombre_col == 'ID':
        return 'BIGINT PRIMARY KEY'

    # Referencias (Foreign Keys)
    if nombre_col.endswith('_DR') or 'RowId' in nombre_col:
        return 'BIGINT'

    # Tipos numericos
    if 'bigint' in tipo_str:
        return 'BIGINT'
    if 'int' in tipo_str and 'bigint' not in tipo_str:
        return 'INT'
    if 'numeric' in tipo_str or 'decimal' in tipo_str or 'float' in tipo_str:
        return 'NUMERIC(18,4)'

    # Tipos fecha/hora
    if 'timestamp' in tipo_str or 'datetime' in tipo_str:
        return 'DATETIME2'
    if 'date' in tipo_str and 'time' not in tipo_str:
        return 'DATE'
    if 'time' in tipo_str and 'date' not in tipo_str:
        return 'TIME'

    # Bit/Boolean
    if 'bit' in tipo_str or 'bool' in tipo_str:
        return 'BIT'

    # Por defecto: varchar
    return 'NVARCHAR(500)'

def schema_existe(cursor_sidra, schema):
    """Verifica si un schema existe en SIDRA"""
    cursor_sidra.execute("""
        SELECT COUNT(*) FROM sys.schemas WHERE name = ?
    """, (schema,))
    return cursor_sidra.fetchone()[0] > 0

def crear_schema(cursor_sidra, schema):
    """Crea un schema en SIDRA si no existe"""
    if not schema_existe(cursor_sidra, schema):
        cursor_sidra.execute(f"EXEC('CREATE SCHEMA {schema}')")
        log(f"  Schema {schema} creado")

def tabla_existe(cursor_sidra, schema, tabla):
    """Verifica si una tabla existe en SIDRA"""
    cursor_sidra.execute("""
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = ? AND TABLE_NAME = ?
    """, (schema, tabla))
    return cursor_sidra.fetchone()[0] > 0

def crear_tabla_dinamica(cursor_alma, cursor_sidra, schema, tabla):
    """Crea tabla en SIDRA basada en estructura de ALMA"""
    # Obtener estructura desde ALMA
    cursor_alma.execute(f"SELECT TOP 1 * FROM questionnaire.{tabla}")

    columnas_def = []
    for desc in cursor_alma.description:
        nombre = desc[0]
        tipo = mapear_tipo_iris_sqlserver(desc[1], nombre)
        columnas_def.append(f"[{nombre}] {tipo}")

    # Crear tabla
    create_sql = f"CREATE TABLE {schema}.{tabla} ({', '.join(columnas_def)})"
    cursor_sidra.execute(create_sql)

    return len(columnas_def)

# ============================================
# FUNCION PRINCIPAL DE SINCRONIZACION
# ============================================
def sync_tabla_reporte(cursor_alma, cursor_sidra, schema, tabla):
    """
    Sincroniza una tabla de reportes de ALMA a SIDRA

    1. SELECT TOP 1000 desde questionnaire.{tabla}
    2. Crear tabla si no existe
    3. TRUNCATE tabla destino
    4. INSERT registros
    5. Retorna cantidad de registros
    """
    tabla_completa = f"{schema}.{tabla}"
    log(f"Sincronizando {tabla_completa}...")

    # 1. Extraer de ALMA (con limite de seguridad)
    query = f"SELECT TOP 1000 * FROM questionnaire.{tabla}"
    try:
        cursor_alma.execute(query)
        columnas = [d[0] for d in cursor_alma.description]
        rows = cursor_alma.fetchall()
    except Exception as e:
        log(f"  ERROR extrayendo de ALMA: {e}")
        return 0

    log(f"  Extraidos: {len(rows)} registros, {len(columnas)} columnas")

    if len(rows) == 0:
        log("  Sin datos para sincronizar")
        return 0

    # 2. Crear schema si no existe
    try:
        crear_schema(cursor_sidra, schema)
    except Exception as e:
        log(f"  ERROR creando schema: {e}")
        return 0

    # 3. Crear tabla si no existe
    if not tabla_existe(cursor_sidra, schema, tabla):
        log(f"  Creando tabla en SIDRA...")
        try:
            num_cols = crear_tabla_dinamica(cursor_alma, cursor_sidra, schema, tabla)
            log(f"  Tabla creada con {num_cols} columnas")
        except Exception as e:
            log(f"  ERROR creando tabla: {e}")
            return 0

    # 4. Limpiar tabla destino (TRUNCATE, no DROP)
    try:
        cursor_sidra.execute(f"TRUNCATE TABLE {tabla_completa}")
    except Exception as e:
        log(f"  ERROR truncando: {e}")
        return 0

    # 5. Insertar registros
    placeholders = ','.join(['?' for _ in columnas])
    cols_escaped = ','.join([f'[{c}]' for c in columnas])
    insert_sql = f"INSERT INTO {tabla_completa} ({cols_escaped}) VALUES ({placeholders})"

    inserted = 0
    errors = 0
    for row in rows:
        try:
            # Convertir valores None/especiales
            values = []
            for val in row:
                if val is None:
                    values.append(None)
                elif isinstance(val, str) and len(val) > 500:
                    values.append(val[:500])  # Truncar strings largos
                else:
                    values.append(val)

            cursor_sidra.execute(insert_sql, values)
            inserted += 1
        except Exception as e:
            errors += 1
            if errors <= 3:  # Solo mostrar primeros errores
                log(f"  ERROR insertando: {str(e)[:100]}")

    if errors > 3:
        log(f"  ... y {errors - 3} errores mas")

    log(f"  Cargados: {inserted} registros")
    return inserted

def actualizar_metadata(cursor_sidra, schema, tabla, count, descripcion=''):
    """Registra o actualiza la sincronizacion en CFG_Queries"""
    try:
        # Verificar si existe
        cursor_sidra.execute("""
            SELECT COUNT(*) FROM ALMA_Meta.CFG_Queries
            WHERE SchemaDestino = ? AND TablaDestino = ?
        """, (schema, tabla))

        if cursor_sidra.fetchone()[0] == 0:
            # Insertar nuevo
            cursor_sidra.execute("""
                INSERT INTO ALMA_Meta.CFG_Queries
                (SchemaDestino, TablaDestino, TipoTabla, ServidorOrigen,
                 BaseDatosOrigen, TablaOrigen, QueryExtraccion, Descripcion,
                 FrecuenciaSinc, UltimaSinc, Registros)
                VALUES (?, ?, 'RPT', 'ALMA', 'LIVE-CLOV', ?, ?, ?, 'Mensual', GETDATE(), ?)
            """, (
                schema, tabla,
                f'questionnaire.{tabla}',
                f'SELECT TOP 1000 * FROM questionnaire.{tabla}',
                descripcion or f'Reporte {tabla}',
                count
            ))
        else:
            # Actualizar existente
            cursor_sidra.execute("""
                UPDATE ALMA_Meta.CFG_Queries
                SET UltimaSinc = GETDATE(), Registros = ?
                WHERE SchemaDestino = ? AND TablaDestino = ?
            """, (count, schema, tabla))
    except Exception as e:
        log(f"  WARN: No se pudo actualizar metadata: {e}")

# ============================================
# MAIN
# ============================================
def main():
    parser = argparse.ArgumentParser(description='Sincronizar reportes ALMA -> SIDRA')
    parser.add_argument('--schema', help='Schema especifico (REM, URGENCIAS, SALUDMENTAL)')
    parser.add_argument('--tabla', help='Tabla especifica (ej: QREMA04E)')
    args = parser.parse_args()

    log("=" * 60)
    log("SINCRONIZACION DE REPORTES: ALMA -> SIDRA")
    log("=" * 60)

    # Conectar
    try:
        conn_alma = conectar_alma()
        cursor_alma = conn_alma.cursor()
        log("Conectado a ALMA (TrakCare/IRIS)")
    except Exception as e:
        log(f"ERROR conectando a ALMA: {e}")
        sys.exit(1)

    try:
        conn_sidra = conectar_sidra()
        cursor_sidra = conn_sidra.cursor()
        log("Conectado a SIDRA (SQL Server)")
    except Exception as e:
        log(f"ERROR conectando a SIDRA: {e}")
        conn_alma.close()
        sys.exit(1)

    # Determinar que sincronizar
    tablas_a_sync = []

    if args.tabla:
        # Buscar tabla especifica
        for schema, tablas in TABLAS_REPORTES.items():
            if args.tabla in tablas:
                tablas_a_sync.append((schema, args.tabla))
                break
        if not tablas_a_sync:
            log(f"ERROR: Tabla '{args.tabla}' no encontrada en la configuracion")
            sys.exit(1)
    elif args.schema:
        # Schema especifico
        schema_name = SCHEMA_ALIASES.get(args.schema.upper(), args.schema)
        if schema_name in TABLAS_REPORTES:
            for tabla in TABLAS_REPORTES[schema_name]:
                tablas_a_sync.append((schema_name, tabla))
        else:
            log(f"ERROR: Schema '{args.schema}' no encontrado")
            sys.exit(1)
    else:
        # Todo
        for schema, tablas in TABLAS_REPORTES.items():
            for tabla in tablas:
                tablas_a_sync.append((schema, tabla))

    log(f"\nTablas a sincronizar: {len(tablas_a_sync)}")
    log("-" * 60)

    # Sincronizar
    total_registros = 0
    tablas_ok = 0
    tablas_error = 0

    for schema, tabla in tablas_a_sync:
        try:
            count = sync_tabla_reporte(cursor_alma, cursor_sidra, schema, tabla)
            if count > 0:
                actualizar_metadata(cursor_sidra, schema, tabla, count)
                tablas_ok += 1
            total_registros += count
        except Exception as e:
            log(f"  ERROR en {schema}.{tabla}: {e}")
            tablas_error += 1

    # Resumen
    log("-" * 60)
    log("RESUMEN")
    log(f"  Tablas procesadas: {tablas_ok + tablas_error}")
    log(f"  Tablas exitosas: {tablas_ok}")
    log(f"  Tablas con error: {tablas_error}")
    log(f"  Total registros: {total_registros}")
    log("=" * 60)
    log("SINCRONIZACION COMPLETADA")

    # Cerrar conexiones
    conn_alma.close()
    conn_sidra.close()

if __name__ == "__main__":
    main()
