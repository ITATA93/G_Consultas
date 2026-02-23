# lab.MR_CaseBodyTrackingConsents

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCBTC_ParRef | varchar | PK |  | NO | MR_CaseBodyTracking Parent Reference |
| MRCBTC_Consent_DR | varchar |  | FK | SI | Consent |
| MRCBTC_DocumentDR | varchar |  | FK | SI | Document |
| MRCBTC_OrderNumber | double |  |  | NO | Order Number |
| MRCBTC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*