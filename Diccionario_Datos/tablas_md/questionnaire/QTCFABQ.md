# questionnaire.QTCFABQ

> Fear Avoidance Beliefs Questionnaire

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fear Avoidance Beliefs Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | My pain was caused by physical activity |
| Q04 | varchar |  |  | SI | Physical activity makes my pain worse |
| Q05 | varchar |  |  | SI | Physical activity might harm my back… |
| Q06 | varchar |  |  | SI | I should not do physical activities which (might) ... |
| Q07 | varchar |  |  | SI | I cannot do physical activities which (might) make... |
| Q08 | varchar |  |  | SI | My pain was caused by my work or by an accident at... |
| Q09 | varchar |  |  | SI | My work aggravated my pain |
| Q10 | varchar |  |  | SI | I have a claim for compensation for my pain |
| Q11 | varchar |  |  | SI | My work is too heavy for me |
| Q12 | varchar |  |  | SI | My work makes, or would make, my pain worse |
| Q13 | varchar |  |  | SI | My work might harm my back |
| Q14 | varchar |  |  | SI | I should not do my normal work with my present pai... |
| Q15 | varchar |  |  | SI | I cannot do my normal work with my present pain |
| Q16 | varchar |  |  | SI | I cannot do my normal work till my pain is treated |
| Q17 | varchar |  |  | SI | I do not think that i will be back to my normal wo... |
| Q18 | varchar |  |  | SI | I do not think that i will ever be able to go back... |
| Q19 | varchar |  |  | SI | George SZ, Fritz JM, Childs JD. Investigation of E... |
| Q20 | varchar |  |  | SI | Physical Activity Subscale (FABQPA; Maximum score ... |
| Q21 | varchar |  |  | SI | Work Subscale (FABQW; Maximum score = 42) |
| Q22 | varchar |  |  | SI | For each statement please select any number from 0... |
| Q23 | varchar |  |  | SI | This instrument quantifies the role of fear-avoida... |
| Q24 | varchar |  |  | SI | J Orthop Sports Phys Ther 2008;38:50–58. |
| Q25 | varchar |  |  | SI | Burton AK, Waddell G, Tillotson KM, Summerton N. I... |
| Q26 | varchar |  |  | SI | Spine. 1999 Dec 1;24(23):2484. |
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