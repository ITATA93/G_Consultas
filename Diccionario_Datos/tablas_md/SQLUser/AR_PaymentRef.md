# SQLUser.AR_PaymentRef

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYREF_RowId | bigint | PK |  | NO | - |
| PAYREF_AssignUser_DR | bigint |  | FK | SI | Des Ref User |
| PAYREF_Date1 | date |  |  | SI | Date1 |
| PAYREF_Date2 | date |  |  | SI | Date2 |
| PAYREF_Date3 | date |  |  | SI | Date3 |
| PAYREF_Date4 | date |  |  | SI | Date4 |
| PAYREF_Date5 | date |  |  | SI | Date5 |
| PAYREF_DateCreated | date |  |  | SI | Date Created |
| PAYREF_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAYREF_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAYREF_Number1 | double |  |  | SI | Number1 |
| PAYREF_Number2 | double |  |  | SI | Number2 |
| PAYREF_Number3 | double |  |  | SI | Number3 |
| PAYREF_Number4 | double |  |  | SI | Number4 |
| PAYREF_Number5 | double |  |  | SI | Number5 |
| PAYREF_PayRefStatus_DR | bigint |  | FK | SI | Des Ref Payment Reference Status |
| PAYREF_PaymRefAmount | double |  |  | SI | Payment Reference Amount |
| PAYREF_PaymRefNumber | varchar |  |  | SI | Payment Reference Number |
| PAYREF_PaymRefReceiptedAmount | double |  |  | SI | Payment Reference Receipted Amount |
| PAYREF_ProcessDate | date |  |  | SI | Process Date |
| PAYREF_ProcessTime | date |  |  | SI | Process Time |
| PAYREF_ProcessUser_DR | bigint |  | FK | SI | Des Ref User |
| PAYREF_Text1 | varchar |  |  | SI | Text1 |
| PAYREF_Text2 | varchar |  |  | SI | Text2 |
| PAYREF_Text3 | varchar |  |  | SI | Text3 |
| PAYREF_Text4 | varchar |  |  | SI | Text4 |
| PAYREF_Text5 | varchar |  |  | SI | Text5 |
| PAYREF_TimeCreated | time |  |  | SI | Time Created |
| QMHDEndedDate | - |  |  | SI | EndedDate |
| QMHDEndedTime | - |  |  | SI | EndedTime |
| QMHDOutcome | - |  |  | SI | MHCDetentionOutcome |
| QMHDetention | - |  |  | SI | MHDetention |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*