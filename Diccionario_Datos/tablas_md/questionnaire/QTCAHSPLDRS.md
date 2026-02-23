# questionnaire.QTCAHSPLDRS

> Dysarthria Rating Scale

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dysarthria Rating Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pitch |
| Q02 | varchar |  |  | SI | Pitch Level (+/-) |
| Q03 | varchar |  |  | SI | Pitch Breaks |
| Q04 | varchar |  |  | SI | Monopitch |
| Q05 | varchar |  |  | SI | Voice Tremor |
| Q06 | varchar |  |  | SI | Myoclonus |
| Q07 | varchar |  |  | SI | Diplophonia |
| Q08 | varchar |  |  | SI | Loudness |
| Q10 | varchar |  |  | SI | Overall Loudness (+/-) |
| Q11 | varchar |  |  | SI | Excess Loudness Variation |
| Q12 | varchar |  |  | SI | Loudness Decay |
| Q13 | varchar |  |  | SI | Altering Loudness |
| Q14 | varchar |  |  | SI | Monoloudness |
| Q15 | varchar |  |  | SI | Voice Quality |
| Q16 | varchar |  |  | SI | Harsh Voice |
| Q17 | varchar |  |  | SI | Hoarse (Wet) |
| Q18 | varchar |  |  | SI | Breathy Voice (Continuous) |
| Q19 | varchar |  |  | SI | Breathy Voice (Transient) |
| Q20 | varchar |  |  | SI | Strained-Strangled Voice |
| Q21 | varchar |  |  | SI | Voice Stoppages |
| Q22 | varchar |  |  | SI | Glottal Fry |
| Q23 | varchar |  |  | SI | Resonance (& Intraoral Pressure) |
| Q24 | varchar |  |  | SI | Hypernasality |
| Q25 | varchar |  |  | SI | Hyponasality |
| Q26 | varchar |  |  | SI | Nasal Emission |
| Q27 | varchar |  |  | SI | Respiration |
| Q28 | varchar |  |  | SI | Forced Inspiration-Expiration |
| Q29 | varchar |  |  | SI | Audible Inspiration |
| Q30 | varchar |  |  | SI | Inhalatory Stridor |
| Q31 | varchar |  |  | SI | Grunt at end of Expiration |
| Q32 | varchar |  |  | SI | Prosody |
| Q33 | varchar |  |  | SI | Rate (+/-) |
| Q34 | varchar |  |  | SI | Short Phrases |
| Q35 | varchar |  |  | SI | Increased Rate in Segments |
| Q36 | varchar |  |  | SI | Reduced Stress |
| Q37 | varchar |  |  | SI | Variable Rate |
| Q38 | varchar |  |  | SI | Prolonged Intervals |
| Q39 | varchar |  |  | SI | Inappropriate Silences |
| Q40 | varchar |  |  | SI | Short Rushes of Speech |
| Q41 | varchar |  |  | SI | Exaggerated Stress |
| Q42 | varchar |  |  | SI | Excess & Equal Stress |
| Q43 | varchar |  |  | SI | Articulation |
| Q44 | varchar |  |  | SI | Imprecise Consonants |
| Q45 | varchar |  |  | SI | Prolonged Phonemes |
| Q46 | varchar |  |  | SI | Irregular Articulatory Breakdowns |
| Q47 | varchar |  |  | SI | Distorted Vowels |
| Q48 | varchar |  |  | SI | Other |
| Q49 | varchar |  |  | SI | Slow Alternating Motion Rate |
| Q50 | varchar |  |  | SI | Fast Alternating Motion Rate |
| Q51 | varchar |  |  | SI | Irregular Alternating Motion Rate |
| Q52 | varchar |  |  | SI | Simple Vocal Tic |
| Q53 | varchar |  |  | SI | Palilalia (Autoecholaelic Utterance) |
| Q54 | varchar |  |  | SI | Coprolalia (Involuntary Swearing) |
| Q55 | varchar |  |  | SI | Comments |
| Q56 | varchar |  |  | SI | Deviant Speech Characteristics - Dysarthria Rating... |
| Q57 | varchar |  |  | SI | Assign a value of 0-4 to each dimension listed abo... |
| Q58 | varchar |  |  | SI | If required (for pitch level and overall loudness)... |
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