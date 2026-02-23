# SQLUser.PA_WaitingListAdm

**Schema:** SQLUser
**Columnas:** 52
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADM_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| ADM_AdmBookingNumber | varchar |  |  | SI | AdmBookingNumber |
| ADM_AdmDate | date |  |  | SI | Adm Date |
| ADM_AdmPointLoc_DR | bigint |  | FK | SI | Des Ref AdmPointLoc |
| ADM_AdmissionCateg_DR | bigint |  | FK | SI | Des Ref to AdmissionCateg |
| ADM_AdmissionPoint_DR | bigint |  | FK | SI | Des Ref AdmissionPoint |
| ADM_AuditResponseDueDate | date |  |  | SI | Audit Response Due Date |
| ADM_AuthoriseUser_DR | bigint |  | FK | SI | Des Ref AuthoriseUser |
| ADM_BloodDonation | varchar |  |  | SI | BloodDonation |
| ADM_BloodDonationDate | date |  |  | SI | Blood Donation Date |
| ADM_BookSystem_DR | bigint |  | FK | SI | Des Ref BookSystem_DR |
| ADM_BookingDate | date |  |  | SI | Booking Date |
| ADM_BookingNumber | varchar |  |  | SI | Booking Number |
| ADM_CancelComment | varchar |  |  | SI | Cancel Comment |
| ADM_CancelDate | date |  |  | SI | Cancel Date |
| ADM_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| ADM_CancelTime | time |  |  | SI | Cancel Time |
| ADM_Childsub | double |  |  | NO | Childsub |
| ADM_Comment | varchar |  |  | SI | Comment |
| ADM_Comments | varchar |  |  | SI | Comments |
| ADM_CommentsCancelLetter | varchar |  |  | SI | Comments Cancel Letter |
| ADM_Confirmation | varchar |  |  | SI | Confirmation |
| ADM_ConfirmationByDate | date |  |  | SI | Confirmation By Date |
| ADM_EdcAgreedDate | date |  |  | SI | EdcAgreedDate |
| ADM_EstTheatreTime | double |  |  | SI | EstTheatreTime |
| ADM_FlaggedPatient | varchar |  |  | SI | Flagged Patient |
| ADM_FreeTextReasonTTG | varchar |  |  | SI | Free Text Reason for Booking Past TTG |
| ADM_IntendedBed_DR | varchar |  | FK | SI | Des Ref IntendedBed |
| ADM_IntendedWard_DR | bigint |  | FK | SI | Des Ref IntendedWard_DR |
| ADM_InterpreterReqd | varchar |  |  | SI | Interpreter Reqd |
| ADM_LastAuditDate | date |  |  | SI | LastAuditDate |
| ADM_OperDate | date |  |  | SI | Operation Date |
| ADM_OperTime | time |  |  | SI | Operation Time |
| ADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ADM_ParentWard_DR | bigint |  | FK | SI | Des Ref ParentWard |
| ADM_PatInterest | varchar |  |  | SI | Patient Interest |
| ADM_PreopDate | date |  |  | SI | Preop Date |
| ADM_PreopTime | time |  |  | SI | Preop Time |
| ADM_ProcFreeText | varchar |  |  | SI | ProcFreeText |
| ADM_ReasonBookPastTTG_DR | bigint |  | FK | SI | Reason for Booking Past TTG |
| ADM_ReasonGroup_DR | bigint |  | FK | SI | Des Ref ReasonGroup |
| ADM_ReverseCancelEffDate | date |  |  | SI | Reverse Cancel Effective Date |
| ADM_RowId | varchar |  |  | NO | - |
| ADM_SpecialRequirements | varchar |  |  | SI | Special Requirements |
| ADM_TheatreType_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ADM_Time | time |  |  | SI | Time |
| ADM_Transport_DR | bigint |  | FK | SI | Des Ref Transport |
| ADM_UpdateDate | date |  |  | SI | UpdateDate |
| ADM_UpdateTime | time |  |  | SI | UpdateTime |
| ADM_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| ADM_User_DR | bigint |  | FK | SI | Des Ref User |
| ADM_VisitStatus | varchar |  |  | SI | Visit Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*