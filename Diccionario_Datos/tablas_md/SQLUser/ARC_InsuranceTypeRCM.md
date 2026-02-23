# SQLUser.ARC_InsuranceTypeRCM

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IRCM_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| IRCM_Childsub | double |  |  | NO | Childsub |
| IRCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IRCM_CreatedDate | date |  |  | SI | Created Date |
| IRCM_CreatedTime | time |  |  | SI | Created Time |
| IRCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IRCM_DateFrom | date |  |  | SI | Date From |
| IRCM_DateTo | date |  |  | SI | Date To |
| IRCM_EpisSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| IRCM_EpisodeType | varchar |  |  | SI | Episode Type |
| IRCM_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| IRCM_MaxSubDays | double |  |  | SI | Max Submission Days |
| IRCM_PayDaysInitSub | double |  |  | SI | Payment due days for Initial Submission |
| IRCM_PayDaysReSub | double |  |  | SI | Payment due days for Resubmission |
| IRCM_PayorCode | varchar |  |  | SI | Payor Code |
| IRCM_PostOffice | varchar |  |  | SI | Post Office |
| IRCM_RowId | varchar |  |  | NO | - |
| IRCM_UpdatedDate | date |  |  | SI | Updated Date |
| IRCM_UpdatedTime | time |  |  | SI | Updated Time |
| IRCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q82Q1 | - |  |  | SI | Evaluación |
| Q82Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*