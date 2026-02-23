# SQLUser.ARC_SurchTimeDepend

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TIME_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| Q08Q1 | - |  |  | SI | Código |
| Q08Q2 | - |  |  | SI | Descripción |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TIME_AuxInstype_DR | bigint |  | FK | SI | Des Ref AuxInstype |
| TIME_Childsub | double |  |  | NO | Childsub |
| TIME_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TIME_CreatedDate | date |  |  | SI | Created Date |
| TIME_CreatedTime | time |  |  | SI | Created Time |
| TIME_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TIME_DOWFrom | double |  |  | SI | Day Of Week From |
| TIME_DOWTo | double |  |  | SI | Day Of Week To |
| TIME_DateFrom | date |  |  | SI | Date From |
| TIME_DateTo | date |  |  | SI | Date To |
| TIME_EpisodeType | varchar |  |  | SI | Admission Type |
| TIME_FixedAmt | double |  |  | SI | Fixed Amt |
| TIME_FixedTimeAmt | double |  |  | SI | Fixed Time Amount |
| TIME_FixedTimeBlock | double |  |  | SI | Fixed Time Block |
| TIME_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| TIME_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| TIME_Name | varchar |  |  | SI | Description |
| TIME_Perc | double |  |  | SI | % Charge |
| TIME_PublicHol | varchar |  |  | SI | PublicHol  |
| TIME_RowId | varchar |  |  | NO | - |
| TIME_TimeFrom | time |  |  | SI | Time From |
| TIME_TimeTo | time |  |  | SI | Time To |
| TIME_UpdatedDate | date |  |  | SI | Updated Date |
| TIME_UpdatedTime | time |  |  | SI | Updated Time |
| TIME_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| TIME_VisitType | varchar |  |  | SI | Visit Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*