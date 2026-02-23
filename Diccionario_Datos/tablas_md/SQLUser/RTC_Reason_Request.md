# SQLUser.RTC_Reason_Request

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REA_RowId | bigint | PK |  | NO | - |
| REA_AdmissionType | varchar |  |  | SI | AdmissionType |
| REA_Code | varchar |  |  | NO | Code |
| REA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REA_Colour | varchar |  |  | SI | Colour |
| REA_CreatedDate | date |  |  | SI | Created Date |
| REA_CreatedTime | time |  |  | SI | Created Time |
| REA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REA_DateFrom | date |  |  | SI | Date From |
| REA_DateTo | date |  |  | SI | Date To |
| REA_Desc | varchar |  |  | NO | Description |
| REA_ExpTimeKeepRecord | double |  |  | SI | Expected Time to Keep Record |
| REA_Owner | varchar |  |  | SI | Owner |
| REA_Priority_No | double |  |  | SI | Priority No |
| REA_ReturnToOffice | varchar |  |  | SI | Return To Office |
| REA_UpdatedDate | date |  |  | SI | Updated Date |
| REA_UpdatedTime | time |  |  | SI | Updated Time |
| REA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*