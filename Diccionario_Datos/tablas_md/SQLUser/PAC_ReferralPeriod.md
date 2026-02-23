# SQLUser.PAC_ReferralPeriod

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFPER_RowId | bigint | PK |  | NO | - |
| Q22Q1 | - |  |  | SI | Date |
| Q22Q2 | - |  |  | SI | Time |
| Q22Q3 | - |  |  | SI | Site inspection |
| Q22Q4 | - |  |  | SI | Peri-tube skin integrity |
| Q22Q5 | - |  |  | SI | Predisposing factors notes |
| Q22Q6 | - |  |  | SI | Site cleaned |
| Q22Q7 | - |  |  | SI | Tube rotated 360 degrees |
| Q22Q8 | - |  |  | SI | Tube patent |
| Q22Q9 | - |  |  | SI | Assessment notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFPER_Code | varchar |  |  | NO | Code |
| REFPER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFPER_CreatedDate | date |  |  | SI | Created Date |
| REFPER_CreatedTime | time |  |  | SI | Created Time |
| REFPER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFPER_DateFrom | date |  |  | SI | Date From |
| REFPER_DateTo | date |  |  | SI | Date To |
| REFPER_Desc | varchar |  |  | NO | Description |
| REFPER_Factor | double |  |  | SI | Factor |
| REFPER_Owner | varchar |  |  | SI | Owner |
| REFPER_UpdatedDate | date |  |  | SI | Updated Date |
| REFPER_UpdatedTime | time |  |  | SI | Updated Time |
| REFPER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*