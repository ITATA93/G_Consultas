# questionnaire.QTCSDSCL

> The Sleep Disorders Checklist (SDS-CL-17)

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Sleep Disorders Checklist (SDS-CL-17)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Over the past year |
| Q04 | varchar |  |  | SI | In takes me 30 minutes or more to fall asleep. |
| Q05 | varchar |  |  | SI | I am awake 30 minutes or more during the night. |
| Q06 | varchar |  |  | SI | I am awake 30 minutes or more prior to my schedule... |
| Q07 | varchar |  |  | SI | I am tired, fatigued or sleepy during the day. |
| Q08 | varchar |  |  | SI | I sleep better if i go to bed before 9:00 pm and w... |
| Q09 | varchar |  |  | SI | I sleep better if i go to bed late (after 1:00 am)... |
| Q10 | varchar |  |  | SI | I fall asleep at inappropriate times or places. |
| Q11 | varchar |  |  | SI | I have been told that i snore. |
| Q12 | varchar |  |  | SI | I wake up during the night choking or gasping. |
| Q13 | varchar |  |  | SI | I have been told i stop breathing when i sleep. |
| Q14 | varchar |  |  | SI | I feel uncomfortable sensations in my legs, especi... |
| Q15 | varchar |  |  | SI | I have an urge to move my legs that is worse in th... |
| Q16 | varchar |  |  | SI | I wake up frequently during the night for no reaso... |
| Q17 | varchar |  |  | SI | I have experienced sudden muscle weakness when lau... |
| Q18 | varchar |  |  | SI | I have been told that i walk, talk, eat or act str... |
| Q19 | varchar |  |  | SI | I have nightmares. |
| Q20 | varchar |  |  | SI | For no reason, i awaken suddenly, startled, and fe... |
| Q21 | varchar |  |  | SI | Subscale |
| Q22 | varchar |  |  | SI | Insomnia |
| Q23 | varchar |  |  | SI | Circadian rythm |
| Q24 | varchar |  |  | SI | Narcolepsy |
| Q25 | varchar |  |  | SI | Obstructive sleep apnea |
| Q26 | varchar |  |  | SI | Restless legs syndrome |
| Q27 | varchar |  |  | SI | Parasomnias |
| Q28 | varchar |  |  | SI | Condition |
| Q29 | varchar |  |  | SI | Insomnia |
| Q30 | varchar |  |  | SI | Circadian rhythm disorder |
| Q31 | varchar |  |  | SI | Narcolepsy |
| Q32 | varchar |  |  | SI | Obstructive sleep apnea |
| Q33 | varchar |  |  | SI | Restless leg syndrome |
| Q34 | varchar |  |  | SI | Parasomnias |
| Q35 | varchar |  |  | SI | Score range |
| Q36 | varchar |  |  | SI | 0 to 12 |
| Q37 | varchar |  |  | SI | 0 to 6 |
| Q38 | varchar |  |  | SI | 0 to 6 |
| Q39 | varchar |  |  | SI | 0 to 12 |
| Q40 | varchar |  |  | SI | 0 to 9 |
| Q41 | varchar |  |  | SI | 0 to 9 |
| Q42 | varchar |  |  | SI | Cut-point for further screening |
| Q43 | varchar |  |  | SI | &gt;5 (sensitivity 0.70, specificity 0.64) |
| Q44 | varchar |  |  | SI | - |
| Q45 | varchar |  |  | SI | &gt;1 (sensitivity 0.88, specificity 0.68) |
| Q46 | varchar |  |  | SI | &gt;3 (sensitivity 0.74, specificity 0.67) |
| Q47 | varchar |  |  | SI | &gt;3 (sensitivity 0.75, specificity 0.80) |
| Q48 | varchar |  |  | SI | - |
| Q49 | varchar |  |  | SI | The sleep disorders checklist (sds-cl-17) is an in... |
| Q50 | varchar |  |  | SI | (insomnia, obstructive sleep apnoea, restless legs... |
| Q51 | varchar |  |  | SI | Source: klingman kj, jungquist cr, perlis ml. intr... |
| Q52 | varchar |  |  | SI | The Sleep Disorders Checklist (SDS-CL-17) is an in... |
| Q53 | varchar |  |  | SI | Please refer to the score table in the guidelines |
| Q54 | varchar |  |  | SI | (insomnia, obstructive sleep apnoea, restless legs... |
| Q55 | varchar |  |  | SI | Insomnia |
| Q56 | varchar |  |  | SI | Circadian rythm |
| Q57 | varchar |  |  | SI | Narcolepsy |
| Q58 | varchar |  |  | SI | Obstructive sleep apnea |
| Q59 | varchar |  |  | SI | Restless legs syndrome |
| Q60 | varchar |  |  | SI | Parasomnias |
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