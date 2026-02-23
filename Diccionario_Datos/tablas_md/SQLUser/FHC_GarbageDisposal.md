# SQLUser.FHC_GarbageDisposal

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCGD_RowId | bigint | PK |  | NO | - |
| FHCGD_Code | varchar |  |  | NO | Garbage Disposal Code |
| FHCGD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCGD_CreatedDate | date |  |  | SI | Created Date |
| FHCGD_CreatedTime | time |  |  | SI | Created Time |
| FHCGD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCGD_DateFrom | date |  |  | NO | Date From |
| FHCGD_DateTo | date |  |  | SI | Date To |
| FHCGD_Desc | varchar |  |  | NO | Garbage Disposal Description |
| FHCGD_NationalCode | varchar |  |  | SI | National Code |
| FHCGD_Owner | varchar |  |  | SI | Owner |
| FHCGD_UpdatedDate | date |  |  | SI | Updated Date |
| FHCGD_UpdatedTime | time |  |  | SI | Updated Time |
| FHCGD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Discharge planning guide |
| Q10 | - |  |  | SI | Anticipated discharge destination |
| Q11 | - |  |  | SI | Recommended discharge services |
| Q12 | - |  |  | SI | Does the patient need discharge transport arranged... |
| Q13 | - |  |  | SI | Readmission questions |
| Q14 | - |  |  | SI | Comments |
| Q15 | - |  |  | SI | Question |
| Q16 | - |  |  | SI | What brought you back to the hospital? |
| Q17 | - |  |  | SI | Were you able to follow up with your primary care ... |
| Q18 | - |  |  | SI | Is there anything we/you could have done different... |
| Q1D | - |  |  | SI | Date |
| Q1T | - |  |  | SI | Time |
| Q2 | - |  |  | SI | Barrier to discharge |
| Q3 | - |  |  | SI | Comments |
| Q4 | - |  |  | SI | Strengths |
| Q5 | - |  |  | SI | Support system |
| Q6 | - |  |  | SI | Assistance recommended after discharge |
| Q7 | - |  |  | SI | Comments |
| Q8 | - |  |  | SI | Home care services |
| Q9 | - |  |  | SI | Type of Home care services |
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