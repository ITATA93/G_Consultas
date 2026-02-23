# questionnaire.QTCAHPRHGMS

> General MusculoSkeletal Evaluation

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* General MusculoSkeletal Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Occupation |
| Q02 | varchar |  |  | SI | Posture / Stresses |
| Q03 | varchar |  |  | SI | Off work because of current episode |
| Q04 | date |  |  | SI | If Yes, Off work from |
| Q05 | varchar |  |  | SI | Diagnosis |
| Q06 | varchar |  |  | SI | Location of pain |
| Q07 | varchar |  |  | SI | Visual analogue scale score |
| Q08 | date |  |  | SI | Pain started |
| Q09 | varchar |  |  | SI | Current pain |
| Q10 | varchar |  |  | SI | Cause(s) of pain |
| Q11 | varchar |  |  | SI | Pain occurs |
| Q12 | varchar |  |  | SI | Sleep disturbed by pain |
| Q13 | varchar |  |  | SI | Comments - pain |
| Q14 | varchar |  |  | SI | Recurrent problem |
| Q15 | varchar |  |  | SI | If Yes - Previous history and treatment |
| Q16 | varchar |  |  | SI | Current radiology images |
| Q17 | varchar |  |  | SI | Previous radiology images |
| Q18 | varchar |  |  | SI | Comments - history |
| Q19 | varchar |  |  | SI | Current health |
| Q20 | varchar |  |  | SI | Current conditions |
| Q21 | varchar |  |  | SI | Operations / Illnesses |
| Q22 | varchar |  |  | SI | Unexplained weight loss |
| Q23 | varchar |  |  | SI | Past steroid use |
| Q24 | varchar |  |  | SI | Dizziness |
| Q25 | varchar |  |  | SI | Bladder control |
| Q26 | varchar |  |  | SI | Gait |
| Q27 | varchar |  |  | SI | Pain with cough / sneeze |
| Q28 | varchar |  |  | SI | Cognition |
| Q29 | varchar |  |  | SI | Assistive devices |
| Q30 | varchar |  |  | SI | Pattern |
| Q31 | varchar |  |  | SI | Forward head posture |
| Q32 | varchar |  |  | SI | Thoracic kyphosis |
| Q33 | varchar |  |  | SI | Lumbar lordosis |
| Q34 | varchar |  |  | SI | Scoliosis |
| Q35 | varchar |  |  | SI | Lateral shifts |
| Q36 | varchar |  |  | SI | Hips / Knees |
| Q37 | varchar |  |  | SI | Feet |
| Q38 | varchar |  |  | SI | Palpation assessment |
| Q39 | varchar |  |  | SI | Comments - general orthopaedic objective |
| Q40 | varchar |  |  | SI | Flexion / Extention / Rotation right |
| Q42 | varchar |  |  | SI | Special test |
| Q43 | varchar |  |  | SI | Impression |
| Q44 | varchar |  |  | SI | Comments - joint assessment |
| Q45 | varchar |  |  | SI | Goal(s) |
| Q46 | varchar |  |  | SI | Comments - goal(s) |
| Q47 | varchar |  |  | SI | Plan |
| Q48 | varchar |  |  | SI | Comments - Plan |
| Q49 | varchar |  |  | SI | Home exercise program |
| Q50 | numeric |  |  | SI | Number of treatments per week |
| Q51 | numeric |  |  | SI | Number of weeks |
| Q52 | varchar |  |  | SI | History - Pain |
| Q53 | varchar |  |  | SI | History - Other |
| Q54 | varchar |  |  | SI | Gait |
| Q55 | varchar |  |  | SI | Posture |
| Q56 | varchar |  |  | SI | Palpation |
| Q57 | varchar |  |  | SI | Flexion / Extention / Rotation left |
| Q58 | date |  |  | SI | Date |
| Q59 | time |  |  | SI | Time |
| Q60 | varchar |  |  | SI | Patient Preference |
| Q61 | varchar |  |  | SI | Short Term Goal(s) |
| Q62 | varchar |  |  | SI | Long Term Goal(s) |
| Q63 | varchar |  |  | SI | Pain score |
| Q63ObsDR | varchar |  | FK | SI | Pain score DR |
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