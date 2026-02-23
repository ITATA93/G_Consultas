# questionnaire.QTCAHPRHWHA

> Woman's Health Assessment

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Woman's Health Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Current problem |
| Q02 | varchar |  |  | SI | When problem began? |
| Q03 | varchar |  |  | SI | First episode related to a specific incident? |
| Q04 | varchar |  |  | SI | If yes, specify |
| Q05 | varchar |  |  | SI | Since incident is it |
| Q06 | varchar |  |  | SI | Why or how? |
| Q07 | varchar |  |  | SI | If pain is present rate pain on 0-10 scale |
| Q08 | varchar |  |  | SI | Describe the nature of the pain |
| Q09 | varchar |  |  | SI | Describe previous treatment / exercises |
| Q10 | varchar |  |  | SI | Activities that cause or aggravate your symptoms |
| Q11 | varchar |  |  | SI | Comments on activities (timings, describe etc) |
| Q12 | varchar |  |  | SI | What relieves your symptoms? |
| Q13 | varchar |  |  | SI | Social activities (exclude physical activities) af... |
| Q14 | varchar |  |  | SI | Diet /Fluid intake |
| Q15 | varchar |  |  | SI | Physical activity |
| Q16 | varchar |  |  | SI | Work |
| Q17 | varchar |  |  | SI | Other |
| Q18 | varchar |  |  | SI | Rate the severity of this problem from 0-10 |
| Q18A | varchar |  |  | SI | (0 being no problem and 10 being worst) |
| Q19 | varchar |  |  | SI | Treatment Goals / Concerns |
| Q20 | varchar |  |  | SI | Since onset of symptoms |
| Q21 | varchar |  |  | SI | Since onset comments |
| Q22 | date |  |  | SI | Date of last physical exam |
| Q23 | varchar |  |  | SI | Last physical exam comments |
| Q24 | varchar |  |  | SI | General health |
| Q25 | varchar |  |  | SI | Occupation |
| Q26 | numeric |  |  | SI | Hours per week |
| Q27 | varchar |  |  | SI | On disability or leave |
| Q28 | varchar |  |  | SI | Activity Restrictions?  |
| Q29 | varchar |  |  | SI | Activity / Exercise |
| Q30 | varchar |  |  | SI | Activity / Exercise Comments |
| Q31 | varchar |  |  | SI | Current level of stress |
| Q32 | varchar |  |  | SI | Current psych therapy? |
| Q33 | numeric |  |  | SI | Number of childbirth vaginal deliveries  |
| Q34 | numeric |  |  | SI | Number of Episiotomy |
| Q35 | numeric |  |  | SI | Number of C-Section |
| Q36 | numeric |  |  | SI | Number of difficult childbirth |
| Q37 | varchar |  |  | SI | Prolapse or organ falling out |
| Q38 | varchar |  |  | SI | Vaginal dryness |
| Q39 | varchar |  |  | SI | Painful periods |
| Q40 | varchar |  |  | SI | Menopause |
| Q41 | varchar |  |  | SI | If menopause, when? |
| Q42 | varchar |  |  | SI | Painful vaginal penetration |
| Q43 | varchar |  |  | SI | Pelvic / genital pain |
| Q44 | varchar |  |  | SI | Other |
| Q46 | varchar |  |  | SI | General Health |
| Q47 | varchar |  |  | SI | Mental Health |
| Q48 | varchar |  |  | SI | Obstetric and Gynecology History |
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