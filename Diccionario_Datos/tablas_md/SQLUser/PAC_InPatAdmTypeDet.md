# SQLUser.PAC_InPatAdmTypeDet

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_InPatAdmissionType Parent Reference |
| ChildQ17DR | - |  |  | SI | Child Reference: Nurse goals |
| DET_AdmReason | varchar |  |  | SI | AdmReason |
| DET_AdmSource | varchar |  |  | SI | AdmSource |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_QualificationStatus | varchar |  |  | SI | QualificationStatus |
| DET_RowId | varchar |  |  | NO | - |
| DET_Sex | varchar |  |  | SI | Sex |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Healthcare figure |
| Q14Q2 | - |  |  | SI | Plan |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*