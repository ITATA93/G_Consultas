# SQLUser.ORC_OperatingStaffRole

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPSTFRL_RowId | bigint | PK |  | NO | - |
| OPSTFRL_Code | varchar |  |  | NO | Code |
| OPSTFRL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPSTFRL_CreatedDate | date |  |  | SI | Created Date |
| OPSTFRL_CreatedTime | time |  |  | SI | Created Time |
| OPSTFRL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPSTFRL_DateFrom | date |  |  | SI | Date From |
| OPSTFRL_DateTo | date |  |  | SI | Date To |
| OPSTFRL_Desc | varchar |  |  | NO | Description |
| OPSTFRL_NonCPAttendee | varchar |  |  | SI | Non CP Attendee |
| OPSTFRL_Owner | varchar |  |  | SI | Owner |
| OPSTFRL_Surgeon | varchar |  |  | SI | Surgeon |
| OPSTFRL_UpdatedDate | date |  |  | SI | Updated Date |
| OPSTFRL_UpdatedTime | time |  |  | SI | Updated Time |
| OPSTFRL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q12Q1 | - |  |  | SI | Time |
| Q12Q2 | - |  |  | SI | Heart rate (/min) |
| Q12Q3 | - |  |  | SI | Systolic BP (mmHg) |
| Q12Q4 | - |  |  | SI | Diastolic BP (mmHg) |
| Q12Q5 | - |  |  | SI | ECG result |
| Q12Q6 | - |  |  | SI | Patient symptoms |
| Q12Q7 | - |  |  | SI | Other details |
| Q12Q8 | - |  |  | SI | Medication given post testing |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*