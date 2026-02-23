# SQLUser.PAC_WLNumberSetup

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLNS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | The RSVT is applicable to infants with the followi... |
| Q02 | - |  |  | SI | • 33-35 completed weeks gestational age infants AN... |
| Q03 | - |  |  | SI | • Who are aged <= 6 months at the start of/or duri... |
| Q04 | - |  |  | SI | Risk Factors |
| Q05 | - |  |  | SI | Birth month is October, November, or December |
| Q06 | - |  |  | SI | Infant to attend daycare or siblings attend daycar... |
| Q07 | - |  |  | SI | More than five individuals in the home including t... |
| Q08 | - |  |  | SI | Small for gestational age (birth weight less than ... |
| Q09 | - |  |  | SI | Immediate family (mother, father, sibling) history... |
| Q10 | - |  |  | SI | Sex is male |
| Q11 | - |  |  | SI | Two or more smokers, use of bakhoor and/or shisha ... |
| Q12 | - |  |  | SI | 0 - 48 = Low Risk |
| Q13 | - |  |  | SI | 49 - 100 =  Eligible to receive injection Palivizu... |
| Q14 | - |  |  | SI | The Respiratory Syncytial Virus Risk Scoring Tool ... |
| Q15 | - |  |  | SI | which allows care providers to guide judicious RSV... |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Classification |
| Q18 | - |  |  | SI | 0 - 48 |
| Q19 | - |  |  | SI | Low risk |
| Q20 | - |  |  | SI | 0 - 48: Low risk |
| Q21 | - |  |  | SI | 49 - 100 |
| Q22 | - |  |  | SI | Eligible to receive injection palivizumab |
| Q23 | - |  |  | SI | 49 - 100: Eligible to receive injection palivizuma... |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
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
| WLNS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WLNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLNS_Counter_DR | bigint |  | FK | SI | Des Ref Counter |
| WLNS_CreatedDate | date |  |  | SI | Created Date |
| WLNS_CreatedTime | time |  |  | SI | Created Time |
| WLNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLNS_DateFrom | date |  |  | SI | DateFrom |
| WLNS_DateTo | date |  |  | SI | DateTo |
| WLNS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| WLNS_Owner | varchar |  |  | SI | Owner |
| WLNS_UpdatedDate | date |  |  | SI | Updated Date |
| WLNS_UpdatedTime | time |  |  | SI | Updated Time |
| WLNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLNS_WaitListType_DR | bigint |  | FK | SI | Des Ref WaitListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*