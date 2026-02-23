# SQLUser.CT_Vat

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTVAT_RowID | bigint | PK |  | NO | - |
| CTVAT_Code | varchar |  |  | NO | VAT Code |
| CTVAT_CreatedDate | date |  |  | SI | Created Date |
| CTVAT_CreatedTime | time |  |  | SI | Created Time |
| CTVAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTVAT_Desc | varchar |  |  | NO | Description |
| CTVAT_NotUseFlag | varchar |  |  | NO | Not Used Flag |
| CTVAT_Rate | double |  |  | NO | VAT Percentage |
| CTVAT_UpdatedDate | date |  |  | SI | Updated Date |
| CTVAT_UpdatedTime | time |  |  | SI | Updated Time |
| CTVAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please enter the score for the term which best des... |
| Q02 | - |  |  | SI | Degree of concern over present bodily health. Rate... |
| Q03 | - |  |  | SI | Worry, fear, or over-concern for present or future... |
| Q04 | - |  |  | SI | Deficiency in relating to the interviewer and to t... |
| Q05 | - |  |  | SI | Rate only the degree to which the patient gives th... |
| Q06 | - |  |  | SI | Degree to which the thought processes are confused... |
| Q07 | - |  |  | SI | Rate on the basis of integration of the verbal pro... |
| Q08 | - |  |  | SI | Over-concern or remorse for past behavior. |
| Q09 | - |  |  | SI | Rate on the basis of the patient’s subjective expe... |
| Q10 | - |  |  | SI | Physical and motor manifestations of tension “nerv... |
| Q11 | - |  |  | SI | Tension should be rated solely on the basis of phy... |
| Q12 | - |  |  | SI | Unusual and unnatural motor benavior, the type of ... |
| Q13 | - |  |  | SI | Rate only abnormality of movements |
| Q14 | - |  |  | SI | Exaggerated self-opinion, conviction of unusual ab... |
| Q15 | - |  |  | SI | Rate only on the basis of patient’s statements abo... |
| Q16 | - |  |  | SI | Despondency in mood, sadness. Rate only degree of ... |
| Q17 | - |  |  | SI | Animosity, contempt, belligerence, disdain for oth... |
| Q18 | - |  |  | SI | Rate solely on the basis of the verbal report of f... |
| Q19 | - |  |  | SI | (Rate attitude toward interviewer under “uncoopera... |
| Q20 | - |  |  | SI | Brief (delusional or otherwise) that others have n... |
| Q21 | - |  |  | SI | On the basis of verbal report, rate only those sus... |
| Q22 | - |  |  | SI | Perceptions without normal external stimulus corre... |
| Q23 | - |  |  | SI | Rate only those experiences which are reported to ... |
| Q24 | - |  |  | SI | Reduction in energy level evidenced in slowed move... |
| Q25 | - |  |  | SI | Evidence of resistance, unfriendliness, resentment... |
| Q26 | - |  |  | SI | Rate only on the basis of the patient’s attitude a... |
| Q27 | - |  |  | SI | Unusual, odd, strange or bizarre thought content. ... |
| Q28 | - |  |  | SI | Reduced emotional tone, apparent lack of normal fe... |
| Q29 | - |  |  | SI | Heightened emotional tone, agitation, increased re... |
| Q30 | - |  |  | SI | Confusion or lack of proper association for person... |
| Q31 | - |  |  | SI | Score |
| Q32 | - |  |  | SI | Classification |
| Q33 | - |  |  | SI | The score range is between 0 - 126 |
| Q34 | - |  |  | SI | The BPRS score is the sum total of each question i... |
| Q35 | - |  |  | SI | The Brief Psychiatric Rating Scale (BPRS) is a rat... |
| Q36 | - |  |  | SI | The BPRS consists of 18 symptom constructs and tak... |
| Q37 | - |  |  | SI | The rater should enter a number ranging from 1 (no... |
| Q38 | - |  |  | SI | 0 - 126 |
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