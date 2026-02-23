# questionnaire.QTCMHBPRS

> Brief Psychiatric Rating Scale

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Brief Psychiatric Rating Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please enter the score for the term which best des... |
| Q02 | varchar |  |  | SI | Degree of concern over present bodily health. Rate... |
| Q03 | varchar |  |  | SI | Worry, fear, or over-concern for present or future... |
| Q04 | varchar |  |  | SI | Deficiency in relating to the interviewer and to t... |
| Q05 | varchar |  |  | SI | Rate only the degree to which the patient gives th... |
| Q06 | varchar |  |  | SI | Degree to which the thought processes are confused... |
| Q07 | varchar |  |  | SI | Rate on the basis of integration of the verbal pro... |
| Q08 | varchar |  |  | SI | Over-concern or remorse for past behavior. |
| Q09 | varchar |  |  | SI | Rate on the basis of the patient’s subjective expe... |
| Q10 | varchar |  |  | SI | Physical and motor manifestations of tension “nerv... |
| Q11 | varchar |  |  | SI | Tension should be rated solely on the basis of phy... |
| Q12 | varchar |  |  | SI | Unusual and unnatural motor benavior, the type of ... |
| Q13 | varchar |  |  | SI | Rate only abnormality of movements; do not rate si... |
| Q14 | varchar |  |  | SI | Exaggerated self-opinion, conviction of unusual ab... |
| Q15 | varchar |  |  | SI | Rate only on the basis of patient’s statements abo... |
| Q16 | varchar |  |  | SI | Despondency in mood, sadness. Rate only degree of ... |
| Q17 | varchar |  |  | SI | Animosity, contempt, belligerence, disdain for oth... |
| Q18 | varchar |  |  | SI | Rate solely on the basis of the verbal report of f... |
| Q19 | varchar |  |  | SI | (Rate attitude toward interviewer under “uncoopera... |
| Q20 | varchar |  |  | SI | Brief (delusional or otherwise) that others have n... |
| Q21 | varchar |  |  | SI | On the basis of verbal report, rate only those sus... |
| Q22 | varchar |  |  | SI | Perceptions without normal external stimulus corre... |
| Q23 | varchar |  |  | SI | Rate only those experiences which are reported to ... |
| Q24 | varchar |  |  | SI | Reduction in energy level evidenced in slowed move... |
| Q25 | varchar |  |  | SI | Evidence of resistance, unfriendliness, resentment... |
| Q26 | varchar |  |  | SI | Rate only on the basis of the patient’s attitude a... |
| Q27 | varchar |  |  | SI | Unusual, odd, strange or bizarre thought content. ... |
| Q28 | varchar |  |  | SI | Reduced emotional tone, apparent lack of normal fe... |
| Q29 | varchar |  |  | SI | Heightened emotional tone, agitation, increased re... |
| Q30 | varchar |  |  | SI | Confusion or lack of proper association for person... |
| Q31 | varchar |  |  | SI | Score |
| Q32 | varchar |  |  | SI | Classification |
| Q33 | varchar |  |  | SI | The score range is between 0 - 126 |
| Q34 | varchar |  |  | SI | The BPRS score is the sum total of each question i... |
| Q35 | varchar |  |  | SI | The Brief Psychiatric Rating Scale (BPRS) is a rat... |
| Q36 | varchar |  |  | SI | The BPRS consists of 18 symptom constructs and tak... |
| Q37 | varchar |  |  | SI | The rater should enter a number ranging from 1 (no... |
| Q38 | varchar |  |  | SI | 0 - 126 |
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