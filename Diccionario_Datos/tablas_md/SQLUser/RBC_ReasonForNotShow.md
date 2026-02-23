# SQLUser.RBC_ReasonForNotShow

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNS_RowId | bigint | PK |  | NO | - |
| RNS_Code | varchar |  |  | NO | Code |
| RNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RNS_CreatedDate | date |  |  | SI | Created Date |
| RNS_CreatedTime | time |  |  | SI | Created Time |
| RNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNS_DateFrom | date |  |  | SI | Date From |
| RNS_DateTo | date |  |  | SI | Date To |
| RNS_DefaultDNAReason | varchar |  |  | SI | DefaultDNAReason |
| RNS_Desc | varchar |  |  | NO | Description |
| RNS_InclInNumDNA | varchar |  |  | SI | Included in the Number of Allowed Non Attended App... |
| RNS_NationalCode | varchar |  |  | SI | National Code |
| RNS_OPWLStatusToReinstate_DR | bigint |  | FK | SI | OPWL Status to Reinstate  |
| RNS_Owner | varchar |  |  | SI | Owner |
| RNS_ReasonToChangeOPWLToRemoved_DR | bigint |  | FK | SI | Reason to change OPWL Status to Removed |
| RNS_RemoveContactReminderDates | varchar |  |  | SI | Remove Contact and Reminder Dates |
| RNS_ResetTTGClock | varchar |  |  | SI | Reset TTG Clock |
| RNS_UpdatedDate | date |  |  | SI | Updated Date |
| RNS_UpdatedTime | time |  |  | SI | Updated Time |
| RNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*