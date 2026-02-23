# lab.MR_CaseBodyTracking

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCBT_ParRef | varchar | PK |  | NO | MR_Case Parent Reference |
| MRCBT_Comments | varchar |  |  | SI | Comments |
| MRCBT_Date | date |  |  | SI | Date |
| MRCBT_DateExpected | date |  |  | SI | Date Expected |
| MRCBT_LocationCurrent | varchar |  |  | SI | Location Current |
| MRCBT_LocationTransfer | varchar |  |  | SI | Location Transfer |
| MRCBT_MethodTransfer | varchar |  |  | SI | Method Transfer |
| MRCBT_OrderNumber | double |  |  | NO | Order Number |
| MRCBT_RowID | varchar |  |  | NO | - |
| MRCBT_Temporary | varchar |  |  | SI | Temporary |
| MRCBT_Time | time |  |  | SI | Time |
| MRCBT_TimeExpected | time |  |  | SI | Time Expected |
| MRCBT_Type | varchar |  |  | SI | Type |
| MRCBT_User | varchar |  |  | SI | User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*