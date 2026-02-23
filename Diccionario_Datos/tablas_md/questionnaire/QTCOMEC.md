# questionnaire.QTCOMEC

> Oral Motor Exam Checklist

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Oral Motor Exam Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of examination |
| Q02 | time |  |  | SI | Time of examination |
| Q03 | varchar |  |  | SI | Non-Speech |
| Q04 | varchar |  |  | SI | I. Facial Musculature - (Sensory - CN V) (Motor - ... |
| Q05 | varchar |  |  | SI | At rest |
| Q06 | varchar |  |  | SI | Squinting |
| Q07 | varchar |  |  | SI | Raise eyebrows |
| Q08 | varchar |  |  | SI | Facial weakness |
| Q09 | varchar |  |  | SI | Other |
| Q10 | varchar |  |  | SI | II. Labial Musculature -  |
| Q11 | varchar |  |  | SI | (Sensory - CN V) (Motor - CN VII) |
| Q12 | varchar |  |  | SI | At rest |
| Q13 | varchar |  |  | SI | Smile (show teeth) |
| Q14 | varchar |  |  | SI | Pursing |
| Q15 | varchar |  |  | SI | Smile to pursing |
| Q16 | varchar |  |  | SI | Close lips and puff cheeks |
| Q17 | varchar |  |  | SI | Close lips as tightly as possible |
| Q18 | varchar |  |  | SI | Close lips and resist pulling |
| Q19 | varchar |  |  | SI | Other |
| Q20 | varchar |  |  | SI | III. Mandibular Musculature - |
| Q21 | varchar |  |  | SI | (Sensory / Motor CN V) |
| Q22 | varchar |  |  | SI | At rest |
| Q23 | varchar |  |  | SI | Open jaw wide |
| Q24 | varchar |  |  | SI | Move jaw side to side |
| Q25 | varchar |  |  | SI | Resist examiner's attempt to force the lower jaw o... |
| Q26 | varchar |  |  | SI | Resist examiner's attempt to close the jaw while p... |
| Q27 | varchar |  |  | SI | Pathologic reflex |
| Q28 | varchar |  |  | SI | Other |
| Q29 | varchar |  |  | SI | IV. Tongue Musculature -  |
| Q30 | varchar |  |  | SI | (Sensory CN VII (taste ant) 2/3, XI (post 1/3)) (M... |
| Q31 | varchar |  |  | SI | At rest |
| Q32 | varchar |  |  | SI | Tongue Protrusion |
| Q33 | varchar |  |  | SI | Tongue lateralization |
| Q34 | varchar |  |  | SI | Tongue elevation |
| Q35 | varchar |  |  | SI | Tongue strength |
| Q36 | varchar |  |  | SI | Patient reports change in taste |
| Q37 | varchar |  |  | SI | Other |
| Q38 | varchar |  |  | SI | V. Palato-pharyngeal Musculature - |
| Q39 | varchar |  |  | SI | (Sensory / Motor CN X) |
| Q40 | varchar |  |  | SI | At rest |
| Q41 | varchar |  |  | SI | Take a deep breath and let it out through mouth |
| Q42 | varchar |  |  | SI | Say 'ah, ah, ah' |
| Q43 | varchar |  |  | SI | Gag reflex |
| Q44 | varchar |  |  | SI | Dry swallow |
| Q45 | varchar |  |  | SI | Voluntary cough |
| Q46 | varchar |  |  | SI | Shortness of breath |
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