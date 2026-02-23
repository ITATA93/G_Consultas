# SQLUser.PAC_DelDecisionMaker

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSMKR_RowId | bigint | PK |  | NO | - |
| DSMKR_Code | varchar |  |  | NO | Code |
| DSMKR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSMKR_CreatedDate | date |  |  | SI | Created Date |
| DSMKR_CreatedTime | time |  |  | SI | Created Time |
| DSMKR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSMKR_DateFrom | date |  |  | SI | Date From |
| DSMKR_DateTo | date |  |  | SI | Date To |
| DSMKR_Desc | varchar |  |  | NO | Desc |
| DSMKR_Owner | varchar |  |  | SI | Owner |
| DSMKR_UpdatedDate | date |  |  | SI | Updated Date |
| DSMKR_UpdatedTime | time |  |  | SI | Updated Time |
| DSMKR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | The questions concern the patient's level of funct... |
| Q04 | - |  |  | SI | please indicate the degree of difficulty the patie... |
| Q05 | - |  |  | SI | last week |
| Q06 | - |  |  | SI | due to his/her knee problem. |
| Q07 | - |  |  | SI | Rising from bed |
| Q08 | - |  |  | SI | Putting on socks / stockings |
| Q09 | - |  |  | SI | Rising from sitting |
| Q10 | - |  |  | SI | Bending to floor |
| Q11 | - |  |  | SI | Twisting / Pivoting on your injured knee |
| Q12 | - |  |  | SI | Kneeling |
| Q13 | - |  |  | SI | Squatting |
| Q14 | - |  |  | SI | Each item is scored from 0 to 4, with 0 representi... |
| Q15 | - |  |  | SI | KOOS-PS scale scores are transformed so the KOOS-P... |
| Q16 | - |  |  | SI | extreme difficulty (0) |
| Q17 | - |  |  | SI | to |
| Q18 | - |  |  | SI | no difficulty (100). |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 - 100 |
| Q22 | - |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
| Q23 | - |  |  | SI | 0 - 100: Scores range from 0 to 100 with a score o... |
| Q24 | - |  |  | SI | No difficulty |
| Q25 | - |  |  | SI | 0: Extreme difficulty |
| Q26 | - |  |  | SI | 100: No difficulty |
| Q27 | - |  |  | SI | The Knee Injury and Osteoarthritis Outcome Score (... |
| Q28 | - |  |  | SI | KOOS-PS Score |
| Q29 | - |  |  | SI | KOOS-PS Score |
| Q30 | - |  |  | SI | KOOS Score (Display only) |
| Q31 | - |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
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