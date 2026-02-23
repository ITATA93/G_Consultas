# lab.MR_CaseViewConsents

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCVC_ParRef | varchar | PK |  | NO | MR_CaseView Parent Reference |
| MRCVC_Consent_DR | varchar |  | FK | SI | Consent |
| MRCVC_DocumentDR | varchar |  | FK | SI | Document |
| MRCVC_OrderNumber | double |  |  | NO | Order Number |
| MRCVC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*