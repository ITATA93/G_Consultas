# SQLUser.PAC_NoAutopsyReason

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACAUT_RowID | bigint | PK |  | NO | - |
| PACAUT_Code | varchar |  |  | NO | Code |
| PACAUT_CodeTableTags | varchar |  |  | SI | List of code table tags |
| PACAUT_CreatedDate | date |  |  | SI | Created Date |
| PACAUT_CreatedTime | time |  |  | SI | Created Time |
| PACAUT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACAUT_DateFrom | date |  |  | SI | Effective date for the record |
| PACAUT_DateTo | date |  |  | SI | Last day the record is active |
| PACAUT_Desc | varchar |  |  | NO | Description |
| PACAUT_Owner | varchar |  |  | SI | Owner |
| PACAUT_UpdatedDate | date |  |  | SI | Updated Date |
| PACAUT_UpdatedTime | time |  |  | SI | Updated Time |
| PACAUT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Glasgow Coma Score input |
| Q02 | - |  |  | SI | Age ≥ 80 years |
| Q03 | - |  |  | SI | ICH Volume ≥ 30ml |
| Q04 | - |  |  | SI | Intraventricular Hemorrhage |
| Q05 | - |  |  | SI | Infratentorial Origin of Hemorrhage |
| Q06 | - |  |  | SI | ICH score is primarily used as a clinical grading ... |
| Q07 | - |  |  | SI | Identifies patients with ICH who will attain funct... |
| Q08 | - |  |  | SI | 30-day mortality increases as the (summed) ICH sco... |
| Q09 | - |  |  | SI | Score 0: No mortailty |
| Q10 | - |  |  | SI | Score 1: 13% mortality chances |
| Q11 | - |  |  | SI | Score 2: 26% mortality chances |
| Q12 | - |  |  | SI | Score 3: 72% mortality chances |
| Q13 | - |  |  | SI | Score 4: 97% mortality chances |
| Q14 | - |  |  | SI | Score 5 - 6: 100% mortality chances |
| Q15 | - |  |  | SI | ICH score is primarily used as a clinical grading ... |
| Q16 | - |  |  | SI | This score is often used in conjunction with the F... |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 1 |
| Q22 | - |  |  | SI | 13% mortality chances |
| Q23 | - |  |  | SI | 2 |
| Q24 | - |  |  | SI | 26% mortality chances |
| Q25 | - |  |  | SI | 3 |
| Q26 | - |  |  | SI | 72% mortality chances |
| Q27 | - |  |  | SI | 4 |
| Q28 | - |  |  | SI | 97% mortality chances |
| Q29 | - |  |  | SI | 5 - 6 |
| Q30 | - |  |  | SI | 100% mortality chances |
| Q31 | - |  |  | SI | 0 |
| Q32 | - |  |  | SI | No mortailty |
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