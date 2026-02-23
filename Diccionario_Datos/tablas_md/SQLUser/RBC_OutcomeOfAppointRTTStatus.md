# SQLUser.RBC_OutcomeOfAppointRTTStatus

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTTST_ParRef | bigint | PK |  | NO | RBC_OutcomeOfAppoint Parent Reference |
| RTTST_Childsub | double |  |  | NO | Childsub |
| RTTST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTTST_CreatedDate | date |  |  | SI | Created Date |
| RTTST_CreatedTime | time |  |  | SI | Created Time |
| RTTST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTTST_RefTreatStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| RTTST_RowId | varchar |  |  | NO | - |
| RTTST_UpdatedDate | date |  |  | SI | Updated Date |
| RTTST_UpdatedTime | time |  |  | SI | Updated Time |
| RTTST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*