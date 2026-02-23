# questionnaire.QTCGDS

> Geriatric Depression Scale (Short Form)

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Geriatric Depression Scale (Short Form)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Instructions: Choose the best answer for how you f... |
| Q04 | varchar |  |  | SI | Are you basically satisfied with your life? |
| Q05 | varchar |  |  | SI | Have you dropped many of your activities and inter... |
| Q06 | varchar |  |  | SI | Do you feel that your life is empty? |
| Q07 | varchar |  |  | SI | Do you often get bored? |
| Q08 | varchar |  |  | SI | Are you in good spirits most of the time? |
| Q09 | varchar |  |  | SI | Are you afraid that something bad is going to happ... |
| Q10 | varchar |  |  | SI | Do you feel happy most of the time? |
| Q11 | varchar |  |  | SI | Do you often feel helpless? |
| Q12 | varchar |  |  | SI | Do you prefer to stay at home, rather than going o... |
| Q13 | varchar |  |  | SI | Do you feel you have more problems with memory tha... |
| Q14 | varchar |  |  | SI | Do you think it is wonderful to be alive? |
| Q15 | varchar |  |  | SI | Do you feel pretty worthless the way you are now? |
| Q16 | varchar |  |  | SI | Do you feel full of energy? |
| Q17 | varchar |  |  | SI | Do you feel that your situation is hopeless? |
| Q18 | varchar |  |  | SI | Do you think that most people are better off than ... |
| Q19 | varchar |  |  | SI | • Choose the best answer for how you felt over the... |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | Approximated in-hospital mortality rates |
| Q23 | varchar |  |  | SI | 0-5 |
| Q24 | varchar |  |  | SI | Normal |
| Q25 | varchar |  |  | SI | ≥6 |
| Q26 | varchar |  |  | SI | Suggests depression |
| Q27 | varchar |  |  | SI | 0-5: Normal |
| Q28 | varchar |  |  | SI | ≥6: Suggests depression |
| Q29 | varchar |  |  | SI | The Geriatric Depression Scale (GDS) (15 point ver... |
| Q30 | varchar |  |  | SI | • Sheikh JI, Yesavage JA. Geriatric Depression Sca... |
| Q31 | varchar |  |  | SI | • Yesavage JA, Brink TL, Rose TL,&nbsp;et all. Dev... |
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