"""
Sincronizacion de Reporte Riesgo ETE (Caprini)
Origen: TrakCare (IRIS) -> Destino: SIDRA (SQL Server)
Frecuencia: Diaria (Recurre ultimas 24-48 horas)

Logica:
1. Buscar ingresos vigentes o recientes.
2. Cruzar con formularios Caprini (QTCCSVT).
3. Verificar si el puntaje (Q45) fue calculado.
"""

import iris
import pyodbc
from datetime import datetime, timedelta, time, date
from pathlib import Path

# Cargar .env desde la raiz del proyecto
try:
    from dotenv import load_dotenv
    import os
    load_dotenv(Path(__file__).resolve().parent.parent / '.env')
except ImportError:
    import os
    pass  # Si dotenv no esta instalado, usa variables de entorno del sistema

# ============================================
# CONFIGURACION (desde .env o valores por defecto)
# ============================================
ALMA_CONFIG = {
    'hostname': os.environ.get('ALMA_HOST', '10.63.180.25'),
    'port': int(os.environ.get('ALMA_PORT', '51773')),
    'namespace': os.environ.get('ALMA_NAMESPACE', 'LIVE-CLOV'),
    'username': os.environ.get('ALMA_USER', ''),
    'password': os.environ.get('ALMA_PASS', '')
}

SIDRA_CONFIG = {
    'server': os.environ.get('SIDRA_HOST', '10.67.119.135'),
    'database': os.environ.get('SIDRA_DATABASE', 'DB_SIDRA_TEST'),
    'username': os.environ.get('SIDRA_USER', ''),
    'password': os.environ.get('SIDRA_PASS', '')
}

# Esquema y Tabla solicitada: ALMA.REP.CAL.RiesgoETE
# Normalizaremos a Schema: ALMA_Reportes, Tabla: CAL_RiesgoETE
SCHEMA_DESTINO = "ALMA_Reportes"
TABLA_DESTINO = "CAL_RiesgoETE"

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def conectar_alma():
    return iris.connect(**ALMA_CONFIG)

def conectar_sidra():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SIDRA_CONFIG['server']};"
        f"DATABASE={SIDRA_CONFIG['database']};"
        f"UID={SIDRA_CONFIG['username']};"
        f"PWD={SIDRA_CONFIG['password']};"
        "Encrypt=no;TrustServerCertificate=yes"
    )
    return pyodbc.connect(conn_str, timeout=30, autocommit=True)

def preparar_destino(cursor):
    """Crea esquema y tabla si no existen"""
    
    # Crear esquema si no existe
    cursor.execute(f"""
        IF NOT EXISTS (SELECT * FROM sys.schemas WHERE name = '{SCHEMA_DESTINO}')
        BEGIN
            EXEC('CREATE SCHEMA [{SCHEMA_DESTINO}]')
        END
    """)

    # Crear tabla (revisar estructura)
    # Se incluye ID compuesto por Episodio + FechaFormulario para evitar duplicados exactos
    sql_create = f"""
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES 
                       WHERE TABLE_SCHEMA = '{SCHEMA_DESTINO}' AND TABLE_NAME = '{TABLA_DESTINO}')
        BEGIN
            CREATE TABLE {SCHEMA_DESTINO}.{TABLA_DESTINO} (
                ID_Row VARCHAR(100) PRIMARY KEY, -- ID unico (Episodio + ID Form)
                Paciente_RUN VARCHAR(20),
                Paciente_Nombre VARCHAR(200),
                Episodio_Admision VARCHAR(30),
                Fecha_Admision DATETIME,
                Ubicacion_Actual VARCHAR(100),
                
                -- Datos Formulario Caprini
                Tiene_Caprini BIT,           -- 1 si existe formulario
                Form_ID VARCHAR(30),         -- ID interno formulario
                Form_Fecha DATETIME,         -- Fecha de evaluacion
                Form_Usuario VARCHAR(100),   -- Quien evaluo
                
                -- Variables Caprini
                Edad INT,                    -- Q01
                Tipo_Cirugia VARCHAR(MAX),   -- Q02
                Evento_Reciente BIT,         -- Q03
                Enf_Venosa_Coagulacion BIT,  -- Q04
                Movilidad VARCHAR(MAX),      -- Q05
                Antecedentes_Otros VARCHAR(MAX), -- Q06
                
                -- Resultados
                Score_Total INT,             -- Q45
                Clasificacion_Riesgo VARCHAR(100), -- Q46
                
                -- Metadata
                Fecha_Proceso DATETIME DEFAULT GETDATE()
            )
        END
    """
    cursor.execute(sql_create)
    log(f"Tabla destino {SCHEMA_DESTINO}.{TABLA_DESTINO} verificada.")

def extraer_y_cargar(cursor_alma, cursor_sidra):
    """
    Consulta ingresos recientes y sus formularios Caprini.
    Estrategia:
    1. Buscar ingresos (PA_Adm) con fecha de admision en los ultimos 5 dias (para asegurar) 
       O que esten vigentes (Current)
    2. Left Join con questionnaire.QTCCSVT
    """
    
    # Rango de busqueda: Pacientes admitidos recientemente o formularios creados recientemente.
    # Optimizacion: Buscamos formularios creados/modificados en las ultimas 48 horas
    # y traemos los datos del paciente asociado.
    
    # Calculo de Fecha Mumps (Dias desde 1840-12-31)
    # Fecha Base Mumps: 1840-12-31
    base_mumps = datetime(1840, 12, 31).date()
    today = datetime.now().date()
    
    # Ventana de 5 dias
    target_date = today - timedelta(days=5)
    
    # Convertir a entero Mumps
    mumps_day = (target_date - base_mumps).days
    
    log(f"Fecha Target: {target_date} -> Mumps: {mumps_day}")

    sql_query = f"""
    SELECT 
        Q.ID,                        -- 0
        Pat.PAPMI_ID,                -- 1 RUN (Corregido de PAPMI_No)
        Pat.PAPMI_Name,              -- 2 Nombre
        Pat.PAPMI_Name2,             -- 3 Apellido P
        Adm.PAADM_AdmNo,             -- 4 Numero Episodio
        Adm.PAADM_AdmDate,           -- 5 Fecha Adm
        Adm.PAADM_AdmTime,           -- 6 Hora Adm
        Loc.CTLOC_Desc,              -- 7 Ubicacion
        Q.QUESDate,                  -- 8 Fecha Form
        Q.QUESTime,                  -- 9 Hora Form
        SSU.SSUSR_Name,              -- 10 Usuario
        Q.Q01,                       -- 11 Edad
        Q.Q02,                       -- 12 Tipo Cirugia
        Q.Q03,                       -- 13 Evento Reciente
        Q.Q04,                       -- 14 Enf Venosa
        Q.Q05,                       -- 15 Movilidad
        Q.Q06,                       -- 16 Otros
        Q.QUESScore,                 -- 17 Score (Corregido)
        NULL AS Clasificacion        -- 18 Clasificacion (No disponible en Q46)
    FROM questionnaire.QTCEEVRIEST Q
    JOIN SQLUser.PA_Adm Adm ON Q.QUESPAAdmDR = Adm.PAADM_RowId
    JOIN SQLUser.PA_PatMas Pat ON Adm.PAADM_PAPMI_DR = Pat.PAPMI_RowId
    LEFT JOIN SQLUser.CT_Loc Loc ON Adm.PAADM_DepCode_DR = Loc.CTLOC_RowId
    LEFT JOIN SQLUser.SS_User SSU ON Q.QUESUserDR = SSU.SSUSR_RowId
    WHERE Q.QUESDate >= {mumps_day}
    """
    
    log("Ejecutando consulta en IRIS (Formularios Caprini QTCEEVRIEST)...")
    cursor_alma.execute(sql_query)
    rows = cursor_alma.fetchall()
    log(f"Registros encontrados: {len(rows)}")
    if len(rows) > 0:
        log(f"Ejemplo fila 0: {rows[0]}")
    
    if not rows:
        return

    # Preparar Upsert en SIDRA
    # Usaremos MERGE o DELETE/INSERT. Por simplicidad en script: DELETE del dia e INSERT.
    
    sql_upsert = f"""
    MERGE {SCHEMA_DESTINO}.{TABLA_DESTINO} AS Target
    USING (VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)) 
       AS Source (ID_Row, Paciente_RUN, Paciente_Nombre, Episodio_Admision, Fecha_Admision, Ubicacion_Actual,
                  Tiene_Caprini, Form_ID, Form_Fecha, Form_Usuario,
                  Edad, Tipo_Cirugia, Evento_Reciente, Enf_Venosa_Coagulacion, Movilidad, Antecedentes_Otros,
                  Score_Total, Clasificacion_Riesgo)
    ON (Target.ID_Row = Source.ID_Row)
    WHEN MATCHED THEN
        UPDATE SET
            Paciente_RUN = Source.Paciente_RUN, -- Forzar actualizacion de RUN
            Form_Fecha = Source.Form_Fecha,
            Score_Total = Source.Score_Total,
            Clasificacion_Riesgo = Source.Clasificacion_Riesgo,
            Fecha_Proceso = GETDATE()
    WHEN NOT MATCHED THEN
        INSERT (ID_Row, Paciente_RUN, Paciente_Nombre, Episodio_Admision, Fecha_Admision, Ubicacion_Actual,
                Tiene_Caprini, Form_ID, Form_Fecha, Form_Usuario,
                Edad, Tipo_Cirugia, Evento_Reciente, Enf_Venosa_Coagulacion, Movilidad, Antecedentes_Otros,
                Score_Total, Clasificacion_Riesgo, Fecha_Proceso)
        VALUES (Source.ID_Row, Source.Paciente_RUN, Source.Paciente_Nombre, Source.Episodio_Admision, Source.Fecha_Admision, Source.Ubicacion_Actual,
                Source.Tiene_Caprini, Source.Form_ID, Source.Form_Fecha, Source.Form_Usuario,
                Source.Edad, Source.Tipo_Cirugia, Source.Evento_Reciente, Source.Enf_Venosa_Coagulacion, Source.Movilidad, Source.Antecedentes_Otros,
                Source.Score_Total, Source.Clasificacion_Riesgo, GETDATE());
    """
    
    count = 0
    
    def get_dt(date_val, time_val):
        """Combina fecha y hora manejando multiples formatos de IRIS (Date, Mumps int, String)"""
        if not date_val: return None
        
        # 1. Normalizar Fecha
        d = None
        if isinstance(date_val, (datetime, date)):
             d = date_val if isinstance(date_val, date) else date_val.date()
        elif isinstance(date_val, int) or (isinstance(date_val, str) and date_val.isdigit()):
             # Conversion Mumps (Dias desde 1840-12-31)
             try:
                 days = int(date_val)
                 d = datetime(1840, 12, 31).date() + timedelta(days=days)
             except: pass
             
        if not d: return None # No se pudo procesar fecha
        
        # 2. Normalizar Hora
        t = datetime.min.time() # Default midnight
        if time_val is not None:
            if isinstance(time_val, time):
                t = time_val
            elif isinstance(time_val, datetime):
                t = time_val.time()
            elif isinstance(time_val, str):
                try:
                    # Intentar HH:MM:SS
                    t = datetime.strptime(time_val, "%H:%M:%S").time()
                except: pass
            elif isinstance(time_val, int) or (isinstance(time_val, str) and time_val.isdigit()):
                # Segundos desde medianoche
                try:
                   secs = int(time_val)
                   t = (datetime.min + timedelta(seconds=secs)).time()
                except: pass
                
        return datetime.combine(d, t)

    def safe_int(val):
        try:
            if val is None: return 0
            if isinstance(val, int): return val
            if isinstance(val, float): return int(val)
            # Extracc digits only if mixed string? No, safest is 0 if not clean int
            # or try cleaning
            s = str(val).strip()
            if not s: return 0
            if s.isdigit(): return int(s)
            # return 0 if alphanumeric garbage
            return 0
        except:
            return 0

    for r in rows:
        try:
            # Procesar Fechas ...
            adm_dt = get_dt(r[5], r[6])
            form_dt = get_dt(r[8], r[9])
            
            # Formatos
            run = str(r[1])
            nombre_full = f"{r[2]} {r[3]}"
            
            # ID Unico
            id_row = f"{str(r[4])}_{str(r[0])}" 
            
            # Sanitizacion para columnas INT
            edad = safe_int(r[11])
            score = safe_int(r[17])
            
            # Clasificacion calculada simple si no viene
            clasificacion = "No Clasificado"
            if r[17]: # Usa raw para clasificacion si es posible parsear float
                try: 
                    s = float(r[17])
                    if s <= 1: clasificacion = "Bajo Riesgo"
                    elif s <= 2: clasificacion = "Riesgo Moderado"
                    elif s <= 4: clasificacion = "Alto Riesgo"
                    else: clasificacion = "Alto Riesgo" # Fixed Typo
                except: pass

            params = (
                id_row, run, nombre_full, str(r[4]), adm_dt, str(r[7]),
                1, str(r[0]), form_dt, str(r[10]),
                edad,            # Edad (Sanitized)
                str(r[12]),      # Tipo Cirugia
                1 if r[13] else 0, 
                1 if r[14] else 0,
                str(r[15]),
                str(r[16]),
                score,           # Score (Sanitized)
                clasificacion 
            )
            
            cursor_sidra.execute(sql_upsert, params)
            count += 1
        except Exception as e:
            log(f"Error procesando fila {r[0]}: {e}")
            
    log(f"Sincronizados {count} registros exitosamente.")

def main():
    log("=== INICIO SYNC CAPRINI ===")
    try:
        conn_alma = conectar_alma()
        log("Conectado a ALMA (IRIS)")
        
        conn_sidra = conectar_sidra()
        log("Conectado a SIDRA (SQL Server)")
        
        preparar_destino(conn_sidra.cursor())
        extraer_y_cargar(conn_alma.cursor(), conn_sidra.cursor())
        
        conn_alma.close()
        conn_sidra.close()
        log("=== FIN PROCESO ===")
        
    except Exception as e:
        log(f"ERROR CRITICO: {e}")

if __name__ == "__main__":
    main()
