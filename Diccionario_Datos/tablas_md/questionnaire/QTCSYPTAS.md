# questionnaire.QTCSYPTAS

> Sydney Post-Traumatic Amnesia Scale (SYPTAS)

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Sydney Post-Traumatic Amnesia Scale (SYPTAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of injury |
| Q04 | time |  |  | SI | Time of injury |
| Q05 | varchar |  |  | SI | Instructions |
| Q06 | varchar |  |  | SI | How old are you? |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | The SYPTAS is administered daily. |
| Q09 | varchar |  |  | SI | What is your mother's / father's name? |
| Q10 | varchar |  |  | SI | Score |
| Q11 | varchar |  |  | SI | On the first day of testing, all orientation and m... |
| Q12 | varchar |  |  | SI | What is the name of this place? |
| Q13 | varchar |  |  | SI | Score |
| Q14 | varchar |  |  | SI | Hence, the maximal score on the first day of testi... |
| Q15 | varchar |  |  | SI | What photo did you have to remember? |
| Q16 | varchar |  |  | SI | Score |
| Q17 | varchar |  |  | SI | Memory items are only scored from the second day o... |
| Q18 | varchar |  |  | SI | What was her name? |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Orientation&nbsp;sub score |
| Q21 | varchar |  |  | SI | Memory sub score |
| Q22 | varchar |  |  | SI | Total score |
| Q23 | varchar |  |  | SI | Comments |
| Q24 | varchar |  |  | SI | Thus, the maximal score from the second day onward... |
| Q25 | varchar |  |  | SI | On assessment of orientation, each day of testing ... |
| Q26 | varchar |  |  | SI | If they fail to spontaneously answer a question, t... |
| Q27 | varchar |  |  | SI | On assessment of memory, on the first day of testi... |
| Q28 | varchar |  |  | SI | The child is asked to repeat the name after the ex... |
| Q29 | varchar |  |  | SI | The child is asked to remember the face and given ... |
| Q30 | varchar |  |  | SI | On subsequent days, the child is asked to pick the... |
| Q31 | varchar |  |  | SI | If the target face is not identified correctly, th... |
| Q32 | varchar |  |  | SI | If the name is not recalled, a choice of 3 names (... |
| Q33 | varchar |  |  | SI | If the name is not identified correctly, the child... |
| Q34 | varchar |  |  | SI | On subsequent days, the target face and the target... |
| Q35 | varchar |  |  | SI | Lah S, David P, Donohue H, Epps A, Tate R, Brookes... |
| Q36 | varchar |  |  | SI | Lah S, Parry L, Epps A, Brooks N. Sydney Post Trau... |
| Q37 | varchar |  |  | SI | https://www.sydney.edu.au/content/dam/corporate/do... |
| Q38 | varchar |  |  | SI | The Sydney Post-traumatic Amnesia scale (SYPTAS) i... |
| Q39 | varchar |  |  | SI | Score of 5/5 on three consecutive days |
| Q40 | varchar |  |  | SI | Children are deemed to be out of Post-Traumatic Am... |
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