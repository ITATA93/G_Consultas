# lab.MR_CaseSpecimenTrackingConsents

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCSTC_ParRef | varchar | PK |  | NO | MR_CaseSpecimenTracking Parent Reference |
| MRCSTC_Consent_DR | varchar |  | FK | SI | Consent |
| MRCSTC_DocumentDR | varchar |  | FK | SI | Document |
| MRCSTC_OrderNumber | double |  |  | NO | Order Number |
| MRCSTC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*