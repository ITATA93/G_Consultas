# SQLUser.LBC_InstrumentTestGroup

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINTG_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINTG_Code | varchar |  |  | NO | Test Group Code |
| LBCINTG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINTG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCINTG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCINTG_Desc | varchar |  |  | NO | Test Group Description |
| LBCINTG_RowID | varchar |  |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Typical |
| Q11 | - |  |  | SI | Compliance |
| Q12 | - |  |  | SI | Interest in surroundings |
| Q13 | - |  |  | SI | Fearfulness |
| Q14 | - |  |  | SI | Attention span |
| Q15 | - |  |  | SI | Guideliness |
| Q16 | - |  |  | SI | Normal |
| Q17 | - |  |  | SI | No delay and a maximum of one caution |
| Q18 | - |  |  | SI | Conduct routine rescreening at next well-child vis... |
| Q19 | - |  |  | SI | Suspect |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Two or more cautions and/or one or more delays |
| Q21 | - |  |  | SI | Rescreen in 1-2 weeks to rule out temporary factor... |
| Q3 | - |  |  | SI | Age at the time test |
| Q4 | - |  |  | SI | Denver II paper documentation |
| Q5 | - |  |  | SI | Interpretation of the test |
| Q6 | - |  |  | SI | Interpretation details |
| Q7 | - |  |  | SI | Schedule follow up |
| Q8 | - |  |  | SI | Follow up details |
| Q9 | - |  |  | SI | Test Behaviour |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*