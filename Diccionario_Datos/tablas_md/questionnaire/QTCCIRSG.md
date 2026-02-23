# questionnaire.QTCCIRSG

> Cumulative Illness Rating Scale-Geriatric (CIRS-G) (Miller et al., 1992)

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cumulative Illness Rating Scale-Geriatric (CIRS-G) (Miller et al., 1992)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Heart |
| Q04 | varchar |  |  | SI | Vascular |
| Q05 | varchar |  |  | SI | Haematopoietic |
| Q06 | varchar |  |  | SI | Respiratory |
| Q07 | varchar |  |  | SI | Eyes, ears, nose, throat, and larynx |
| Q08 | varchar |  |  | SI | Upper gastrointestinal |
| Q09 | varchar |  |  | SI | Lower gastrointestinal |
| Q10 | varchar |  |  | SI | Liver |
| Q11 | varchar |  |  | SI | Renal |
| Q12 | varchar |  |  | SI | Genitourinary |
| Q13 | varchar |  |  | SI | Musculoskeletal or integument |
| Q14 | varchar |  |  | SI | Neurological |
| Q15 | varchar |  |  | SI | Endocrine or metabolic, and breast |
| Q16 | varchar |  |  | SI | Psychiatric illness |
| Q17 | varchar |  |  | SI | Scoring |
| Q18 | varchar |  |  | SI | Total Number of Categories Endorsed |
| Q19 | varchar |  |  | SI | Total Score |
| Q20 | varchar |  |  | SI | Severity Index: (Total Score / Total Number of Cat... |
| Q21 | varchar |  |  | SI | Number of Categories at Level 3 Severity |
| Q22 | varchar |  |  | SI | Number of Categories at Level 4 Severity |
| Q23 | varchar |  |  | SI | Refer to the scoring to see if patient's total sco... |
| Q24 | varchar |  |  | SI | Guidelines |
| Q25 | varchar |  |  | SI | Rating strategy |
| Q26 | varchar |  |  | SI | 0 - No problem |
| Q27 | varchar |  |  | SI | 1 - Current mild problem OR past significant probl... |
| Q28 | varchar |  |  | SI | 2 - Moderate disability or mobility OR requires fi... |
| Q29 | varchar |  |  | SI | 3 - Severe OR constant significant disability OR u... |
| Q30 | varchar |  |  | SI | 4 - Extremely severe OR immediate treatment requir... |
| Q31 | varchar |  |  | SI | Provenance |
| Q32 | varchar |  |  | SI | Reference |
| Q33 | varchar |  |  | SI | Miller MD, Paradis CF, Houck PR, Mazumdar S, Stack... |
| Q34 | varchar |  |  | SI | Psychiatry Res 1992;41:237248. |
| Q35 | varchar |  |  | SI | Cumulative Illness Rating Scale-Geriatric (CIRS-G)... |
| Q36 | varchar |  |  | SI | Refer to the scoring to see if patient's total sco... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*