# SQLUser.PAC_QualificationStatusDet

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_QualificationStatus Parent Reference |
| DET_AdmReason | varchar |  |  | SI | AdmReason |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_CriteriaForAdm | varchar |  |  | SI | CriteriaForAdm |
| DET_DateFrom | date |  |  | SI | DateFrom |
| DET_DateTo | date |  |  | SI | DateTo |
| DET_InPatAdmType | varchar |  |  | SI | InPatAdmType |
| DET_RowId | varchar |  |  | NO | - |
| DET_SourceOfAdmission | varchar |  |  | SI | SourceOfAdmission |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02Q1 | - |  |  | SI | Skin preparation used |
| Q02Q2 | - |  |  | SI | Body site |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*