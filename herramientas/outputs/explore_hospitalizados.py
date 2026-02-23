"""FINAL: SUBSTRING directo sobre stream property + global char stream"""
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from herramientas.python.db_config import conectar_alma

def run(conn, name, sql, raw=True):
    print(f"\n{'='*70}")
    print(f"{name}")
    print('='*70)
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        cols = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        print(f"Filas: {len(rows)}  |  Columnas: {cols}")
        for row in rows[:5]:
            for i, c in enumerate(cols):
                v = row[i]
                s = str(v) if v is not None else 'NULL'
                if len(s) > 500:
                    s = s[:497] + '...'
                print(f"  {c}: {s}")
            print()
        cursor.close()
    except Exception as e:
        print(f"  ERROR: {e}")

iris = conectar_alma()

# Segun docs IRIS: SUBSTRING funciona sobre CLOB/stream nativos
# Pero NOT_NotesHTMLPlainText es bigint (referencia), no stream nativo
# Necesitamos buscar si hay un campo stream nativo en la clase

# 1. Verificar tipos de datos reales via INFORMATION_SCHEMA
run(iris, "1. Tipos datos reales de campos Notes", """
    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'MR_NursingNotes'
    AND COLUMN_NAME IN ('NOT_Notes', 'NOT_Notes1', 'NOT_RTFNotes', 'NOT_RTFNotes1',
        'NOT_NotesHTMLPlainText', 'NOT_NotesHTMLRichText', 'NOT_ClinNoteText')
    ORDER BY COLUMN_NAME
""")

# 2. Buscar campo NOT_ClinNoteText que es "Text Result" 
run(iris, "2. NOT_ClinNoteText (QUESTextResultDR?) en NursingNotes", """
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'MR_NursingNotes'
    AND COLUMN_NAME LIKE '%Text%'
""")

# 3. Buscar TODAS las columnas tipo longvarchar o longvarbinary
run(iris, "3. Columnas tipo long en MR_NursingNotes", """
    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'MR_NursingNotes'
    AND DATA_TYPE IN ('longvarchar', 'longvarbinary', 'clob')
""")

# 4. Probar campo QUESTextResultDR 
run(iris, "4. QUESTextResultDR (Text Result) de Cat=4 hoy", """
    SELECT TOP 3
        nn.NOT_RowId,
        nn.QUESTextResultDR AS TEXT_RESULT
    FROM SQLUser.MR_NursingNotes nn
    WHERE nn.NOT_ClinNotesCat_DR = 4
    AND nn.NOT_Date = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)
""")

# 5. Intentar con columna en posicion Q01-Q25 (que puede contener texto)
run(iris, "5. Columnas Q* que puedan tener texto del plan", """
    SELECT TOP 1
        nn.NOT_RowId,
        nn.Q01, nn.Q02, nn.Q03, nn.Q04, nn.Q05, nn.Q07
    FROM SQLUser.MR_NursingNotes nn
    WHERE nn.NOT_ClinNotesCat_DR = 4
    AND nn.NOT_Date = DATEDIFF('dd', '1840-12-31', CURRENT_DATE)
""")

# 6. Probar la notacion stream con doble indirection
run(iris, "6. SUBSTRING sobre websys.Document.docData directo", """
    SELECT TOP 1
        SUBSTRING(doc.docData, 1, 2000) AS TXT
    FROM websys.Document doc
    WHERE doc.ID = 1800539
""")

# 7. Probar clase directa con %OpenId
run(iris, "7. Buscar tablas con nursing notes text / lookup", """
    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE '%NursingNote%'
    ORDER BY TABLE_NAME
""")

iris.close()
print("\nDONE")
