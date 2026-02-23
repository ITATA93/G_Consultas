# questionnaire.QTCPANSS

> Positive and Negative Syndrome Scale (PANSS)

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Positive and Negative Syndrome Scale (PANSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Delusions |
| Q04 | varchar |  |  | SI | Conceptual disorganization |
| Q05 | varchar |  |  | SI | Hallucinatory behaviour |
| Q06 | varchar |  |  | SI | Excitement |
| Q07 | varchar |  |  | SI | Grandiosity |
| Q08 | varchar |  |  | SI | Suspiciousness / Persecution |
| Q09 | varchar |  |  | SI | Hostility |
| Q10 | varchar |  |  | SI | Blunted affect |
| Q11 | varchar |  |  | SI | Emotional withdrawal |
| Q12 | varchar |  |  | SI | Poor rapport |
| Q13 | varchar |  |  | SI | Passive / Apathetic social withdrawal |
| Q14 | varchar |  |  | SI | Difficulty in abstract thinking |
| Q15 | varchar |  |  | SI | Lack of spontaneity and flow of conversation |
| Q16 | varchar |  |  | SI | Stereotyped thinking |
| Q17 | varchar |  |  | SI | Somatic concern |
| Q18 | varchar |  |  | SI | Anxiety |
| Q19 | varchar |  |  | SI | Guilt feelings |
| Q20 | varchar |  |  | SI | Tension |
| Q21 | varchar |  |  | SI | Mannerisms and posturing |
| Q22 | varchar |  |  | SI | Depression |
| Q23 | varchar |  |  | SI | Motor retardation |
| Q24 | varchar |  |  | SI | Uncooperativeness |
| Q25 | varchar |  |  | SI | Unusual thought content |
| Q26 | varchar |  |  | SI | Disorientation |
| Q27 | varchar |  |  | SI | Poor attention |
| Q28 | varchar |  |  | SI | Lack of judgement and insight |
| Q29 | varchar |  |  | SI | Disturbance of volition |
| Q30 | varchar |  |  | SI | Poor impulse control |
| Q31 | varchar |  |  | SI | Preoccupation |
| Q32 | varchar |  |  | SI | Active social avoidance |
| Q33 | varchar |  |  | SI | As 1 rather than 0 is given as the lowest score fo... |
| Q34 | varchar |  |  | SI | Scores are often given separately for the positive... |
| Q35 | varchar |  |  | SI | Stanley Kay and colleagues tested the scale on 101... |
| Q36 | varchar |  |  | SI | • Positive scale = 18.20 |
| Q37 | varchar |  |  | SI | • Negative scale = 21.01 |
| Q38 | varchar |  |  | SI | • General psychopathology = 37.74 |
| Q39 | varchar |  |  | SI | Subscore positive scale |
| Q40 | varchar |  |  | SI | Subscore negative scale |
| Q41 | varchar |  |  | SI | Subscore general psychopathology |
| Q42 | varchar |  |  | SI | Total score |
| Q43 | varchar |  |  | SI | Score |
| Q44 | varchar |  |  | SI | Classification |
| Q45 | varchar |  |  | SI | The higher the score, the higher the patient's sym... |
| Q46 | varchar |  |  | SI | 30 - 210 |
| Q47 | varchar |  |  | SI | 30 - 210: The higher the score, the higher the pat... |
| Q48 | varchar |  |  | SI | The Positive and Negative Syndrome Scale (PANSS) i... |
| Q49 | varchar |  |  | SI | Subscore positive scale |
| Q50 | varchar |  |  | SI | Minimum score = 7, Maximum score = 49 |
| Q51 | varchar |  |  | SI | Subscore negative scale |
| Q52 | varchar |  |  | SI | Minimum score = 7, Maximum score = 49 |
| Q53 | varchar |  |  | SI | Subscore general psychopathology |
| Q54 | varchar |  |  | SI | Minimum score = 16, Maximum score = 112 |
| Q55 | varchar |  |  | SI | Subscore positive scale |
| Q56 | varchar |  |  | SI | Subscore negative scale |
| Q57 | varchar |  |  | SI | Subscore general psychopathology |
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