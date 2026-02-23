"""
batch_migrate.py - Migra TODAS las credenciales hardcodeadas a db_config.py
Ejecutar: python herramientas/batch_migrate.py
"""
import re
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Credenciales a buscar
ALMA_CREDS = ["'18233087-6'", "'sd260710sd'"]
SIDRA_CREDS = ["'hkEVC9AFVjFeRTkp'"]

# Bloque de import para db_config
IMPORT_BLOCK_CONSULTAS = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import {imports}
"""

IMPORT_BLOCK_HERRAMIENTAS_SUB = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import {imports}
"""

IMPORT_BLOCK_EXPORTACIONES = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import {imports}, PROJECT_ROOT
"""

IMPORT_BLOCK_EXPORTACIONES_SUB = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from herramientas.python.db_config import {imports}, PROJECT_ROOT
"""

IMPORT_BLOCK_DICCIONARIO = """from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from herramientas.python.db_config import {imports}, PROJECT_ROOT
"""


def get_import_block(filepath, imports):
    """Determina el bloque de import correcto segun la ubicacion del archivo."""
    rel = filepath.resolve().relative_to(PROJECT_ROOT.resolve())
    parts = rel.parts
    
    imports_str = ', '.join(imports)
    
    if parts[0] == 'Consultas_live':
        return IMPORT_BLOCK_CONSULTAS.format(imports=imports_str)
    elif parts[0] == 'Diccionario_Datos':
        return IMPORT_BLOCK_DICCIONARIO.format(imports=imports_str)
    elif parts[0] == 'Exportaciones' and len(parts) > 2:
        return IMPORT_BLOCK_EXPORTACIONES_SUB.format(imports=imports_str)
    elif parts[0] == 'Exportaciones':
        return IMPORT_BLOCK_EXPORTACIONES.format(imports=imports_str)
    elif parts[0] == 'herramientas' and len(parts) > 2:
        return IMPORT_BLOCK_HERRAMIENTAS_SUB.format(imports=imports_str)
    else:
        return IMPORT_BLOCK_CONSULTAS.format(imports=imports_str)


def migrate_file(filepath):
    """Migra un archivo Python, reemplazando credenciales."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    original = content
    
    has_alma = any(c in content for c in ALMA_CREDS)
    has_sidra = any(c in content for c in SIDRA_CREDS)
    
    if not has_alma and not has_sidra:
        return None
    
    # Determinar que se necesita importar
    imports = []
    if has_alma:
        imports.append('ALMA_CONFIG')
    if has_sidra:
        imports.append('SIDRA_CONFIG')
    
    # Patron para bloques SIDRA_CONFIG = { ... }
    sidra_block = re.compile(
        r"SIDRA_CONFIG\s*=\s*\{[^}]*'password'\s*:\s*'hkEVC9AFVjFeRTkp'[^}]*\}",
        re.DOTALL
    )
    
    # Patron para bloques ALMA/IRIS CONFIG = { ... }  
    alma_block = re.compile(
        r"(?:IRIS_CONFIG|ALMA_CONFIG)\s*=\s*\{[^}]*'password'\s*:\s*'sd260710sd'[^}]*\}",
        re.DOTALL
    )
    
    # Patron para bloques con ambos (ALMA y SIDRA juntos, como en sync scripts)
    # y tambien bloques sueltos con credenciales en iris.connect()
    iris_connect = re.compile(
        r"iris\.connect\(\s*hostname='10\.63\.180\.25'[^)]*\)",
        re.DOTALL
    )
    
    # Reemplazar bloques de config
    if has_sidra:
        content = sidra_block.sub('# SIDRA_CONFIG cargado desde herramientas/python/db_config.py', content)
    if has_alma:
        content = alma_block.sub('# ALMA_CONFIG cargado desde herramientas/python/db_config.py', content)
        # Tambien reemplazar el iris.connect directo
        content = iris_connect.sub('iris.connect(**ALMA_CONFIG)', content)
    
    # Verificar que se eliminaron las credenciales
    still_has_alma = any(c in content for c in ALMA_CREDS)
    still_has_sidra = any(c in content for c in SIDRA_CREDS)
    
    if still_has_alma or still_has_sidra:
        # Hay credenciales en un formato no reconocido, reemplazar directamente
        content = content.replace("'18233087-6'", "ALMA_CONFIG['username']")
        content = content.replace("'sd260710sd'", "ALMA_CONFIG['password']")
        content = content.replace("'hkEVC9AFVjFeRTkp'", "SIDRA_CONFIG['password']")
    
    # Agregar import block despues de los imports existentes
    # Buscar la ultima linea de import/from existente
    lines = content.split('\n')
    last_import_idx = -1
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from '):
            if 'db_config' not in stripped:  # No contar si ya importa db_config
                last_import_idx = i
    
    # Insertar bloque de import despues del ultimo import
    import_block = get_import_block(filepath, imports)
    
    if 'db_config' not in content:
        if last_import_idx >= 0:
            lines.insert(last_import_idx + 1, import_block)
        else:
            lines.insert(0, import_block)
        content = '\n'.join(lines)
    
    # Corregir rutas legacy c:\_Consultas\ -> PROJECT_ROOT
    content = content.replace(r"r'c:\_Consultas\Diccionario_Datos\diccionario.db'",
                              "str(PROJECT_ROOT / 'Diccionario_Datos' / 'diccionario.db')")
    content = content.replace(r"r'c:\_Consultas\Exportaciones\Usuarios'",
                              "str(PROJECT_ROOT / 'Exportaciones' / 'Usuarios')")
    content = content.replace(r"c:\_Consultas\Exportaciones\Usuarios",
                              "str(PROJECT_ROOT / 'Exportaciones' / 'Usuarios')")
    # Agregar PROJECT_ROOT al import si se usa y no esta
    if 'PROJECT_ROOT' in content and 'PROJECT_ROOT' not in import_block:
        content = content.replace(
            f"from herramientas.python.db_config import {', '.join(imports)}",
            f"from herramientas.python.db_config import {', '.join(imports)}, PROJECT_ROOT"
        )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return imports
    
    return None


def main():
    print("=" * 60)
    print("MIGRACION BATCH DE CREDENCIALES")
    print("=" * 60)
    
    migrated = 0
    errors = 0
    
    for pyfile in sorted(PROJECT_ROOT.rglob('*.py')):
        rel = str(pyfile.relative_to(PROJECT_ROOT))
        if '_archivo' in rel or '__pycache__' in rel:
            continue
        if 'migrate_credentials' in rel or 'batch_migrate' in rel or 'db_config' in rel:
            continue
        
        try:
            result = migrate_file(pyfile)
            if result:
                print(f"  OK: {rel} ({', '.join(result)})")
                migrated += 1
        except Exception as e:
            print(f"  ERROR: {rel} - {e}")
            errors += 1
    
    print(f"\n{'=' * 60}")
    print(f"Migrados: {migrated} archivos")
    print(f"Errores: {errors}")
    print(f"{'=' * 60}")
    
    # Verificar que no quedan credenciales
    print("\nVerificando credenciales residuales...")
    residual = 0
    for pyfile in sorted(PROJECT_ROOT.rglob('*.py')):
        rel = str(pyfile.relative_to(PROJECT_ROOT))
        if '_archivo' in rel or '__pycache__' in rel:
            continue
        if 'batch_migrate' in rel or 'migrate_credentials' in rel:
            continue
        try:
            with open(pyfile, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            for cred in ALMA_CREDS + SIDRA_CREDS:
                if cred in content:
                    print(f"  RESIDUAL: {rel} contiene {cred[:10]}...")
                    residual += 1
                    break
        except:
            pass
    
    if residual == 0:
        print("  LIMPIO - No quedan credenciales hardcodeadas!")
    else:
        print(f"  ATENCION: {residual} archivos aun tienen credenciales")


if __name__ == '__main__':
    main()
