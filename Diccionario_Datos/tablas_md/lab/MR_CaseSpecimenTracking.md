# lab.MR_CaseSpecimenTracking

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCST_ParRef | varchar | PK |  | NO | MR_Case Parent Reference |
| MRCST_Comments | varchar |  |  | SI | Comments |
| MRCST_Date | date |  |  | SI | Date |
| MRCST_DateExpected | date |  |  | SI | Date Expected |
| MRCST_LocationCurrent | varchar |  |  | SI | Location Current |
| MRCST_OrderNumber | double |  |  | NO | Order Number |
| MRCST_OrganType | varchar |  |  | SI | Type of Specimen |
| MRCST_Release | varchar |  |  | SI | Release without return |
| MRCST_RowID | varchar |  |  | NO | - |
| MRCST_Status | varchar |  |  | SI | Status |
| MRCST_Time | time |  |  | SI | Time |
| MRCST_Type | varchar |  |  | SI | Type |
| MRCST_User | varchar |  |  | SI | User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*