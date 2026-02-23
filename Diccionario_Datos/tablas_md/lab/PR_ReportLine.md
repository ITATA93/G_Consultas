# lab.PR_ReportLine

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRPRL_ParRef | double | PK |  | NO | PR_Report Parent Reference |
| PRPRL_ChildSub | numeric |  |  | NO | ChildSub |
| PRPRL_Line | varchar |  |  | SI | Line |
| PRPRL_RowID | varchar |  |  | NO | - |
| PRPRL_Section | varchar |  |  | NO | Section |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*