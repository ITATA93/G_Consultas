"""
dic_local.py — Diccionario local SQLite para catalogos ALMA.

Almacena catalogos extraidos de ALMA en un SQLite local para evitar
JOINs pesados al servidor live. Los catalogos se importan desde CSV
o directamente desde ALMA (una sola vez, luego se resuelven local).

Uso:
    from herramientas.python.dic_local import DicLocal

    dic = DicLocal()
    dic.importar_csvs()                  # carga CSVs existentes
    dic.resolve("OEC_OrderStatus", 3)    # -> "Ejecutado"
    dic.resolve("SS_Group", 228)         # -> "CLXX.EM.Médico Urgencia"
    dic.resolve("CT_CareProv", 1986)     # -> "DR. PEREZ JUAN" (si se exporto)
"""
import csv
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = PROJECT_ROOT / "data" / "diccionarios.db"
CSV_DIR = PROJECT_ROOT / "docs" / "research" / "catalogos"

# Mapeo: nombre_tabla -> (archivo_csv, col_id, col_desc)
CATALOGO_MAP = {
    "OEC_OrderStatus": ("estados_orden.csv", "RowId", "Desc"),
    "PAC_RequestStatus": ("estados_solicitud_ic.csv", "RowId", "Desc"),
    "PAC_ContMethod": ("metodos_contacto_ic.csv", "RowId", "Desc"),
    "SS_Group": ("grupos_interconsulta.csv", "SSGRP_RowId", "SSGRP_Desc"),
    "ARC_ItmMast_Llamado": ("consultorias_llamado_hova.csv", "ARCIM_RowId", "ARCIM_Desc"),
    "ARC_ItmMast_IC": ("interconsultas_internas_hova.csv", "ARCIM_RowId", "ARCIM_Desc"),
    "ARC_ItmMast_Tele": ("teleconsultas.csv", "ARCIM_RowId", "ARCIM_Desc"),
    "ARC_ItmMast_Eval": ("evaluaciones.csv", "ARCIM_RowId", "ARCIM_Desc"),
}


class DicLocal:
    """Diccionario local SQLite para catalogos ALMA."""

    def __init__(self, db_path=None):
        self.db_path = Path(db_path) if db_path else DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.execute("PRAGMA journal_mode=WAL")

    def close(self):
        self.conn.close()

    # ------------------------------------------------------------------
    # Importar CSV -> SQLite
    # ------------------------------------------------------------------
    def importar_csv(self, tabla, csv_path, col_id, col_desc):
        """Importa un CSV a una tabla normalizada (id, code, desc, raw)."""
        path = Path(csv_path)
        if not path.exists():
            print(f"[SKIP] {path} no existe")
            return 0

        self.conn.execute(f"""
            CREATE TABLE IF NOT EXISTS [{tabla}] (
                id   TEXT PRIMARY KEY,
                desc TEXT NOT NULL
            )
        """)
        self.conn.execute(f"DELETE FROM [{tabla}]")

        count = 0
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rid = row.get(col_id, "").strip()
                rdesc = row.get(col_desc, "").strip()
                if rid:
                    self.conn.execute(
                        f"INSERT OR REPLACE INTO [{tabla}] (id, desc) VALUES (?, ?)",
                        (rid, rdesc),
                    )
                    count += 1
        self.conn.commit()
        print(f"[OK] {tabla}: {count} registros <- {path.name}")
        return count

    def importar_csvs(self):
        """Importa todos los CSVs conocidos del directorio de catalogos."""
        total = 0
        for tabla, (csv_name, col_id, col_desc) in CATALOGO_MAP.items():
            csv_path = CSV_DIR / csv_name
            total += self.importar_csv(tabla, csv_path, col_id, col_desc)
        print(f"\nTotal: {total} registros importados a {self.db_path}")
        return total

    def importar_alma_catalogo(self, tabla, query, col_id, col_desc, csv_name=None):
        """Exporta un catalogo desde ALMA y lo importa al SQLite local.

        Args:
            tabla: nombre de la tabla local
            query: SQL a ejecutar en ALMA
            col_id: nombre de la columna ID en el resultado
            col_desc: nombre de la columna descripcion en el resultado
            csv_name: opcional, guardar CSV en catalogos/
        """
        from herramientas.python.db_config import conectar_alma

        conn_alma = conectar_alma()
        cur = conn_alma.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cols = [d[0] for d in cur.description]
        conn_alma.close()

        idx_id = cols.index(col_id)
        idx_desc = cols.index(col_desc)

        self.conn.execute(f"""
            CREATE TABLE IF NOT EXISTS [{tabla}] (
                id   TEXT PRIMARY KEY,
                desc TEXT NOT NULL
            )
        """)
        self.conn.execute(f"DELETE FROM [{tabla}]")

        for row in rows:
            rid = str(row[idx_id]).strip() if row[idx_id] is not None else ""
            rdesc = str(row[idx_desc]).strip() if row[idx_desc] is not None else ""
            if rid:
                self.conn.execute(
                    f"INSERT OR REPLACE INTO [{tabla}] (id, desc) VALUES (?, ?)",
                    (rid, rdesc),
                )
        self.conn.commit()

        # Guardar CSV si se pidio
        if csv_name:
            csv_path = CSV_DIR / csv_name
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(cols)
                for row in rows:
                    w.writerow(row)
            print(f"[OK] {tabla}: {len(rows)} registros (ALMA -> SQLite + {csv_name})")
        else:
            print(f"[OK] {tabla}: {len(rows)} registros (ALMA -> SQLite)")

        return len(rows)

    # ------------------------------------------------------------------
    # Resolver ID -> Descripcion
    # ------------------------------------------------------------------
    def resolve(self, tabla, row_id):
        """Resuelve un ID a su descripcion. Retorna None si no existe."""
        if row_id is None:
            return None
        cur = self.conn.execute(
            f"SELECT desc FROM [{tabla}] WHERE id = ?", (str(row_id),)
        )
        row = cur.fetchone()
        return row[0] if row else None

    def resolve_many(self, tabla, row_ids):
        """Resuelve una lista de IDs. Retorna dict {id: desc}."""
        if not row_ids:
            return {}
        placeholders = ",".join("?" for _ in row_ids)
        cur = self.conn.execute(
            f"SELECT id, desc FROM [{tabla}] WHERE id IN ({placeholders})",
            [str(x) for x in row_ids if x is not None],
        )
        return {row[0]: row[1] for row in cur.fetchall()}

    def tablas(self):
        """Lista las tablas del diccionario local y su conteo."""
        cur = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        )
        result = {}
        for (name,) in cur.fetchall():
            count = self.conn.execute(f"SELECT COUNT(*) FROM [{name}]").fetchone()[0]
            result[name] = count
        return result

    def dump(self, tabla, limit=20):
        """Muestra registros de una tabla local."""
        cur = self.conn.execute(f"SELECT id, desc FROM [{tabla}] LIMIT ?", (limit,))
        rows = cur.fetchall()
        print(f"--- {tabla} ({len(rows)} mostrados) ---")
        for rid, rdesc in rows:
            print(f"  {rid:>12s}  {rdesc}")
        return rows


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
if __name__ == "__main__":
    import sys

    dic = DicLocal()

    if len(sys.argv) > 1 and sys.argv[1] == "import":
        dic.importar_csvs()
    elif len(sys.argv) > 1 and sys.argv[1] == "tables":
        for t, c in dic.tablas().items():
            print(f"  {t:30s} {c:>6d} registros")
    elif len(sys.argv) > 1 and sys.argv[1] == "dump":
        tabla = sys.argv[2] if len(sys.argv) > 2 else "OEC_OrderStatus"
        dic.dump(tabla)
    else:
        print("Uso: python dic_local.py [import|tables|dump <tabla>]")

    dic.close()
