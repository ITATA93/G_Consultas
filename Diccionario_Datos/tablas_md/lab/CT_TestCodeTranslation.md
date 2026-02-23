# lab.CT_TestCodeTranslation

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCF_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCF_Description | varchar |  |  | SI | Description |
| CTTCF_Language_DR | bigint |  | FK | NO | Language DR |
| CTTCF_RowID | varchar |  |  | NO | - |
| CTTCF_Units | varchar |  |  | SI | CTTCF_Units |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*