# SQLUser.AR_PatBillPaymRef

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYMREF_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| PAYMREF_BillClaimStatus_DR | bigint |  | FK | SI | Des Ref to ARCBillClaimStatus |
| PAYMREF_Childsub | double |  |  | NO | Childsub |
| PAYMREF_ClaimRADenialComments | varchar |  |  | SI | Claim RA Denial Comments |
| PAYMREF_ClaimRAIDPayor | varchar |  |  | SI | Claim RA ID Payor |
| PAYMREF_ClaimRARefAmount | double |  |  | SI | Claim RA Reference Amount |
| PAYMREF_DateCreated | date |  |  | SI | Date Created |
| PAYMREF_PaymentRef_DR | bigint |  | FK | SI | Des Ref to ARPaymentRef |
| PAYMREF_RASettlementDate | date |  |  | SI | RA Settlement Date |
| PAYMREF_ReasonClaimDenial_DR | bigint |  | FK | SI | Des Ref to ARCReasonForClaimDenial |
| PAYMREF_RemitAdviceClaim_DR | varchar |  | FK | SI | Des Ref to ARRemittanceAdviceClaim |
| PAYMREF_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Memoria 1 |
| Q02 | - |  |  | SI | Le leeré una lista de 5 palabras, Ud. debe recorda... |
| Q03 | - |  |  | SI | Primer intento |
| Q04 | - |  |  | SI | Segundo intento |
| Q05 | - |  |  | SI | Fluidez verbal |
| Q06 | - |  |  | SI | Diga el mayor número posible de palabras que comie... |
| Q07 | - |  |  | SI | No pueden ser nombres propios ni tampoco palabras ... |
| Q08 | - |  |  | SI | Total palabras |
| Q09 | - |  |  | SI | Resultado |
| Q10 | - |  |  | SI | Orientación |
| Q11 | - |  |  | SI | Dígame por favor el |
| Q12 | - |  |  | SI | Memoria 2: recuerdo diferido |
| Q13 | - |  |  | SI | Recuerde las 5 palabras que le dije hace un moment... |
| Q14 | - |  |  | SI | 1. Recuerdo libres |
| Q15 | - |  |  | SI | 2. Recuerdo con clave semántica (no se puntúan) |
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