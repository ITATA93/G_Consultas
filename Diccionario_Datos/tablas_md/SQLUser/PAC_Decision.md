# SQLUser.PAC_Decision

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEC_RowId | bigint | PK |  | NO | - |
| DEC_Adjorned | varchar |  |  | SI | Adjorned |
| DEC_Code | varchar |  |  | NO | Code |
| DEC_CreatedDate | date |  |  | SI | Created Date |
| DEC_CreatedTime | time |  |  | SI | Created Time |
| DEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEC_DateFrom | date |  |  | SI | DateFrom |
| DEC_DateTo | date |  |  | SI | DateTo |
| DEC_Desc | varchar |  |  | NO | Description |
| DEC_UpdatedDate | date |  |  | SI | Updated Date |
| DEC_UpdatedTime | time |  |  | SI | Updated Time |
| DEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Presented to Emergency Department (ED) because of ... |
| Q04 | - |  |  | SI | Consider: syncope, seizure or loss of consciousnes... |
| Q05 | - |  |  | SI | Age > 70 years |
| Q06 | - |  |  | SI | Altered mental state |
| Q07 | - |  |  | SI | Consider: disorientation, impaired judgement, poor... |
| Q08 | - |  |  | SI | Impaired mobility |
| Q09 | - |  |  | SI | Consider: Ambulates or transfers with assistive de... |
| Q10 | - |  |  | SI | Ambulates with unsteady gait and no assistance |
| Q11 | - |  |  | SI | Unable to ambulate or transfer |
| Q12 | - |  |  | SI | Nurse judgement |
| Q13 | - |  |  | SI | Consider: bowel or bladder incontinence, diarrhoea... |
| Q14 | - |  |  | SI | Details of judgement |
| Q15 | - |  |  | SI | • Once an ED patient is deemed a high fall risk in... |
| Q16 | - |  |  | SI | • If patient does not have any fall risks identifi... |
| Q17 | - |  |  | SI | If the patient falls in the ED, the patient become... |
| Q18 | - |  |  | SI | • If patient is a high fall risk, fall prevention ... |
| Q19 | - |  |  | SI | The following section is not part of the KINDER 1 ... |
| Q20 | - |  |  | SI | Implement bedside safety plan |
| Q21 | - |  |  | SI | The following actions should be completed in all i... |
| Q22 | - |  |  | SI | Add falls risk against patient's alerts in TrakCar... |
| Q23 | - |  |  | SI | A full falls risk assessment and management plan t... |
| Q24 | - |  |  | SI | Consider criteria for referral to Falls and Balanc... |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | 0 |
| Q28 | - |  |  | SI | No falls risk |
| Q29 | - |  |  | SI | 1 - 5 |
| Q30 | - |  |  | SI | High falls risk |
| Q31 | - |  |  | SI | 0: No falls risk |
| Q32 | - |  |  | SI | 1 - 5: High falls risk |
| Q33 | - |  |  | SI | The KINDER 1 falls risk assessment tool was design... |
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