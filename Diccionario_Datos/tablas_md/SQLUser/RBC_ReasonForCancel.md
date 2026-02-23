# SQLUser.RBC_ReasonForCancel

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFC_RowId | bigint | PK |  | NO | - |
| RFC_AdmCancelReason_DR | bigint |  | FK | SI | Des Ref AdmCancelReason |
| RFC_Code | varchar |  |  | NO | Code |
| RFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFC_CreatedDate | date |  |  | SI | Created Date |
| RFC_CreatedTime | time |  |  | SI | Created Time |
| RFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFC_DateFrom | date |  |  | SI | Date From |
| RFC_DateTo | date |  |  | SI | Date To |
| RFC_Default | varchar |  |  | SI | Default |
| RFC_Desc | varchar |  |  | NO | Description |
| RFC_Initiator | varchar |  |  | SI | Initiator |
| RFC_NationalCode | varchar |  |  | SI | National Code |
| RFC_OPWLStatusToReinstate_DR | bigint |  | FK | SI | OPWL Status to Reinstate  |
| RFC_Owner | varchar |  |  | SI | Owner |
| RFC_ReasonToChangeOPWLToRemoved_DR | bigint |  | FK | SI | Reason to change OPWL Status to Removed |
| RFC_RemoveContactReminderDates | varchar |  |  | SI | Remove Contact and Reminder Dates |
| RFC_ResetTTGClock | varchar |  |  | SI | Reset TTG Clock |
| RFC_UpdatedDate | date |  |  | SI | Updated Date |
| RFC_UpdatedTime | time |  |  | SI | Updated Time |
| RFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*