# SQLUser.AR_Bill

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARBIL_RowId | bigint | PK |  | NO | - |
| ARBIL_AddDate | date |  |  | SI | Add Date |
| ARBIL_AddTime | time |  |  | SI | Add Time |
| ARBIL_AddUserID | bigint |  |  | SI | Add User ID |
| ARBIL_AdmType | varchar |  |  | SI | Patient Admission Type (same as PAADM_Type) |
| ARBIL_Amount | double |  |  | NO | Invoice Amount |
| ARBIL_Date | date |  |  | NO | Invoice Date |
| ARBIL_DateCashFlow | date |  |  | SI | Expected Payment Date |
| ARBIL_DateDue | date |  |  | SI | Invoice Due Date |
| ARBIL_DateEnd | date |  |  | SI | Invoice End Date (needed?) |
| ARBIL_DateStart | date |  |  | SI | Invoice Start Date (needed?) |
| ARBIL_Debtor_DR | bigint |  | FK | SI | Not Used Des Ref to ARCDR |
| ARBIL_DocFeeFlag | varchar |  |  | SI | Doctor Fee Processing Flag |
| ARBIL_FinPer_DR | varchar |  | FK | NO | Financial Period - des ref to CTFPR |
| ARBIL_GlBatch | varchar |  |  | SI | GL Batch |
| ARBIL_Location_DR | bigint |  | FK | SI | des ref to CTLOC (invoice dept) |
| ARBIL_No | double |  |  | NO | Bill Number |
| ARBIL_OsAmt | double |  |  | SI | Outstanding Amount |
| ARBIL_PAPER_DR | bigint |  | FK | SI | des ref to PAPER |
| ARBIL_PayAmt | double |  |  | SI | Payment Amount |
| ARBIL_PrintCount | double |  |  | SI | Print Count |
| ARBIL_RcFlg | varchar |  |  | SI | Archive Flag |
| ARBIL_Remark | varchar |  |  | SI | Remarks |
| ARBIL_Status | varchar |  |  | SI | Billing Status |
| ARBIL_Type | varchar |  |  | NO | Bill Type |
| Q01 | - |  |  | SI | Indicación Parto Operatorio |
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