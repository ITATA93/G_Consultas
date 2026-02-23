# SQLUser.PAC_ResidenceStatus

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESID_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date and time of fall |
| Q02 | - |  |  | SI | Time of fall |
| Q03 | - |  |  | SI | Location |
| Q04 | - |  |  | SI | Brief description |
| Q05 | - |  |  | SI | Witnessed by |
| Q06 | - |  |  | SI | Clinician |
| Q07 | - |  |  | SI | Please specify |
| Q08 | - |  |  | SI | Injury sustained |
| Q09 | - |  |  | SI | Location of injury |
| Q10 | - |  |  | SI | Type of injury |
| Q11 | - |  |  | SI | Observations attended |
| Q12 | - |  |  | SI | Assess / Reassess with the falls assessment and ma... |
| Q13 | - |  |  | SI | Fall reported to |
| Q14 | - |  |  | SI | Contributing factors |
| Q15 | - |  |  | SI | Any further interventions required? |
| Q16 | - |  |  | SI | Please specify |
| Q17 | - |  |  | SI | Has the patient had a previous fall during this ad... |
| Q18 | - |  |  | SI | Date of last fall |
| Q19 | - |  |  | SI | Fall number |
| Q20 | - |  |  | SI | Multiple falls multidisciplinary review |
| Q21 | - |  |  | SI | Multiple faller interventions discussed / plan rec... |
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
| RESID_Code | varchar |  |  | NO | Code |
| RESID_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESID_CreatedDate | date |  |  | SI | Created Date |
| RESID_CreatedTime | time |  |  | SI | Created Time |
| RESID_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESID_DateFrom | date |  |  | SI | Date From |
| RESID_DateTo | date |  |  | SI | Date To |
| RESID_Desc | varchar |  |  | NO | Description |
| RESID_NationCode | varchar |  |  | SI | National Code |
| RESID_Owner | varchar |  |  | SI | Owner |
| RESID_UpdatedDate | date |  |  | SI | Updated Date |
| RESID_UpdatedTime | time |  |  | SI | Updated Time |
| RESID_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*