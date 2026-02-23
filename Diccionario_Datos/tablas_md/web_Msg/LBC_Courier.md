# web_Msg.LBC_Courier

**Schema:** web_Msg
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCC_Code | varchar |  |  | SI | Code
Required by User.LBCCourier. |
| LBCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCC_Confidential | varchar |  |  | SI | Confidential |
| LBCC_ConfidentialLabSite_DR | bigint |  | FK | SI | Confidential Site
The LabSite for which the couri... |
| LBCC_CourierBatch_DR | bigint |  | FK | SI | Courier Batch
The Batch definition (type C) to us... |
| LBCC_CreatedDate | date |  |  | SI | Created Date |
| LBCC_CreatedTime | time |  |  | SI | Created Time |
| LBCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCC_Desc | varchar |  |  | SI | Description
Required by User.LBCCourier. |
| LBCC_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCC_Owner | varchar |  |  | SI | Owner |
| LBCC_QuickPrintBatch_DR | bigint |  | FK | SI | QuickPrint Batch
The QuickPrint Batch definition ... |
| LBCC_RowID | varchar |  |  | SI | - |
| LBCC_SinglePatientBatch_DR | bigint |  | FK | SI | SinglePatient Batch
The Single-Patient Batch defi... |
| LBCC_Timeslot | integer |  |  | SI | The Timeslot interval for creating Doctors Reports... |
| LBCC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*