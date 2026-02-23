# SQLUser.RBC_SessionType

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SESS_RowId | bigint | PK |  | NO | - |
| SESS_Code | varchar |  |  | NO | Code |
| SESS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SESS_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| SESS_ConvertPeriod | double |  |  | SI | ConvertPeriod(mins) |
| SESS_CreatedDate | date |  |  | SI | Created Date |
| SESS_CreatedTime | time |  |  | SI | Created Time |
| SESS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SESS_DateFrom | date |  |  | SI | Date From |
| SESS_DateTo | date |  |  | SI | Date To |
| SESS_Desc | varchar |  |  | NO | Description |
| SESS_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| SESS_EnableByDefault | varchar |  |  | SI | Enable By Default |
| SESS_GenFrequency | double |  |  | SI | GenFrequency |
| SESS_GenPeriod | varchar |  |  | SI | GenPeriod |
| SESS_NumberOfDays | double |  |  | SI | Number Of Days |
| SESS_Owner | varchar |  |  | SI | Owner |
| SESS_ReleaseDays | double |  |  | SI | ReleaseDays |
| SESS_SessionType_DR | bigint |  | FK | SI | Des Ref Session Type |
| SESS_UpdatedDate | date |  |  | SI | Updated Date |
| SESS_UpdatedTime | time |  |  | SI | Updated Time |
| SESS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*