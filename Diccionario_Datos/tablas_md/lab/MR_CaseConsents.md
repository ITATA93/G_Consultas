# lab.MR_CaseConsents

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCC_ParRef | varchar | PK |  | NO | MR_Case Parent Reference |
| MRCC_Date | date |  |  | SI | Date |
| MRCC_DateWithdrawn | date |  |  | SI | Date Withdrawn |
| MRCC_Fate | varchar |  |  | SI | Fate of Material |
| MRCC_OrderNumber | double |  |  | NO | Order Number |
| MRCC_Person | varchar |  |  | SI | Person giving consent |
| MRCC_Relationship | varchar |  |  | SI | Relationship |
| MRCC_RelationshipWithdrawn | varchar |  |  | SI | Relationship Withdrawn |
| MRCC_Required | varchar |  |  | SI | Required |
| MRCC_RowID | varchar |  |  | NO | - |
| MRCC_Time | time |  |  | SI | Time |
| MRCC_TimeWithdrawn | time |  |  | SI | Time Withdrawn |
| MRCC_Type | varchar |  |  | SI | Type |
| MRCC_User | varchar |  |  | SI | User |
| MRCC_UserWithdrawn | varchar |  |  | SI | User Withdrawn |
| MRCC_Withdrawn | varchar |  |  | SI | Withdrawn |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*