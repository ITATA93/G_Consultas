"""
db_config.py - Modulo centralizado de configuracion de conexiones.

Uso:
    from herramientas.python.db_config import ALMA_CONFIG, SIDRA_CONFIG, conectar_alma, conectar_sidra

O si se ejecuta desde un subdirectorio profundo:
    import sys; sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
    from herramientas.python.db_config import ALMA_CONFIG, SIDRA_CONFIG
"""
import os
from pathlib import Path

# Buscar .env subiendo directorios hasta encontrarlo
def _find_env():
    """Busca .env subiendo desde este archivo hasta la raiz del proyecto."""
    p = Path(__file__).resolve().parent
    for _ in range(5):
        env = p / '.env'
        if env.exists():
            return env
        p = p.parent
    return None

try:
    from dotenv import load_dotenv
    env_path = _find_env()
    if env_path:
        load_dotenv(env_path)
except ImportError:
    pass  # Si dotenv no esta instalado, usa variables de entorno del sistema

# ============================================
# CONFIGURACION ALMA (InterSystems IRIS)
# ============================================
ALMA_CONFIG = {
    'hostname': os.environ.get('ALMA_HOST', '10.63.180.25'),
    'port': int(os.environ.get('ALMA_PORT', '51773')),
    'namespace': os.environ.get('ALMA_NAMESPACE', 'LIVE-CLOV'),
    'username': os.environ.get('ALMA_USER', ''),
    'password': os.environ.get('ALMA_PASS', '')
}

# ============================================
# CONFIGURACION SIDRA (SQL Server)
# ============================================
SIDRA_CONFIG = {
    'server': os.environ.get('SIDRA_HOST', '10.67.119.135'),
    'port': int(os.environ.get('SIDRA_PORT', '1433')),
    'database': os.environ.get('SIDRA_DATABASE', 'DB_SIDRA_TEST'),
    'username': os.environ.get('SIDRA_USER', ''),
    'password': os.environ.get('SIDRA_PASS', '')
}

# ============================================
# RUTAS DEL PROYECTO
# ============================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def conectar_alma():
    """Conecta a ALMA/TrakCare (InterSystems IRIS)."""
    import iris
    return iris.connect(**ALMA_CONFIG)


def conectar_sidra(timeout=30, autocommit=True):
    """Conecta a SIDRA (SQL Server) con ODBC."""
    import pyodbc
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SIDRA_CONFIG['server']};"
        f"DATABASE={SIDRA_CONFIG['database']};"
        f"UID={SIDRA_CONFIG['username']};"
        f"PWD={SIDRA_CONFIG['password']};"
        "Encrypt=no;TrustServerCertificate=yes"
    )
    return pyodbc.connect(conn_str, timeout=timeout, autocommit=autocommit)


def sidra_conn_str():
    """Retorna el connection string ODBC para SIDRA (sin conectar)."""
    return (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SIDRA_CONFIG['server']};"
        f"DATABASE={SIDRA_CONFIG['database']};"
        f"UID={SIDRA_CONFIG['username']};"
        f"PWD={SIDRA_CONFIG['password']};"
        "Encrypt=no;TrustServerCertificate=yes"
    )
