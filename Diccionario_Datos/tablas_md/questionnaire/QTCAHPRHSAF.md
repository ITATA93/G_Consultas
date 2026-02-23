# questionnaire.QTCAHPRHSAF

> Shoulder Assessment

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Hand dominance |
| Q02 | varchar |  |  | SI | Occupation |
| Q03 | varchar |  |  | SI | Are you having pain in your shoulder? |
| Q05 | varchar |  |  | SI | Is your pain? |
| Q06 | varchar |  |  | SI | How bad is your pain today  |
| Q07 | varchar |  |  | SI | Check the words that best describe the character o... |
| Q08 | varchar |  |  | SI | What time of the day is your pain worst? |
| Q09 | varchar |  |  | SI | Does the pain wake you from sleep? |
| Q10 | varchar |  |  | SI | What makes your pain better |
| Q11 | varchar |  |  | SI | Other |
| Q12 | varchar |  |  | SI | What makes your pain worse |
| Q13 | varchar |  |  | SI | Other |
| Q14 | date |  |  | SI | Date problem began (approximate) |
| Q15 | varchar |  |  | SI | Pain Progress |
| Q16 | varchar |  |  | SI | Describe your current problem |
| Q17 | date |  |  | SI | Date of Re-injury |
| Q18 | varchar |  |  | SI | Does your shoulder feel unstable (as if it is goin... |
| Q19 | varchar |  |  | SI | How unstable is your shoulder |
| Q19A | varchar |  |  | SI | (0 very stable - 10 very unstable) |
| Q20 | varchar |  |  | SI | Is your problem a result of an injury? |
| Q21 | varchar |  |  | SI | What caused your injury? |
| Q22 | varchar |  |  | SI | Other |
| Q23 | varchar |  |  | SI | Do you notice any of the following symptoms when m... |
| Q24 | varchar |  |  | SI | Do you have numbness and/or tingling around the sh... |
| Q27 | varchar |  |  | SI | Medical history |
| Q28 | varchar |  |  | SI | Previous surgery |
| Q29 | varchar |  |  | SI | Previous physical therapy treatment  |
| Q30 | varchar |  |  | SI | X-ray |
| Q31 | varchar |  |  | SI | Report |
| Q32 | varchar |  |  | SI | Posture |
| Q33 | varchar |  |  | SI | Atrophy |
| Q34 | varchar |  |  | SI | Comment |
| Q35 | varchar |  |  | SI | Swelling |
| Q36 | varchar |  |  | SI | Comment |
| Q37 | varchar |  |  | SI | Temp |
| Q38 | varchar |  |  | SI | Location |
| Q39 | varchar |  |  | SI | Scars |
| Q40 | varchar |  |  | SI | Location |
| Q43 | varchar |  |  | SI | Apley scratch test |
| Q44 | varchar |  |  | SI | Painful arc |
| Q45 | varchar |  |  | SI | Comment  |
| Q53 | varchar |  |  | SI | Other special test |
| Q54 | varchar |  |  | SI | Diagnosis |
| Q55 | varchar |  |  | SI | Problems list |
| Q56 | varchar |  |  | SI | Rehabilitation potential |
| Q57 | varchar |  |  | SI | Family / patient involved in and verbalized unders... |
| Q58 | varchar |  |  | SI | Comment |
| Q59 | varchar |  |  | SI | Patient was instructed in shoulder model as it per... |
| Q60 | varchar |  |  | SI | Comment |
| Q61 | varchar |  |  | SI | Short term goals |
| Q62 | varchar |  |  | SI | Long term goals |
| Q63 | varchar |  |  | SI | Treatment |
| Q64 | varchar |  |  | SI | Other |
| Q65 | numeric |  |  | SI | Number of treatments per week |
| Q66 | numeric |  |  | SI | Number of weeks |
| Q67 | varchar |  |  | SI | Re-Evaluation  |
| Q68 | varchar |  |  | SI | Other |
| Q69 | varchar |  |  | SI | Patient goals |
| Q72 | varchar |  |  | SI | Patient self evaluation |
| Q73 | varchar |  |  | SI | Therapist assessment |
| Q74 | varchar |  |  | SI | Observation |
| Q75 | varchar |  |  | SI | Palpation |
| Q76 | date |  |  | SI | Date |
| Q77 | time |  |  | SI | Time |
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