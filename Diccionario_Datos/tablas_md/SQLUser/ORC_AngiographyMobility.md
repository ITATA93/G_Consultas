# SQLUser.ORC_AngiographyMobility

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANGMOB_RowId | bigint | PK |  | NO | - |
| ANGMOB_Code | varchar |  |  | NO | Code |
| ANGMOB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANGMOB_CreatedDate | date |  |  | SI | Created Date |
| ANGMOB_CreatedTime | time |  |  | SI | Created Time |
| ANGMOB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANGMOB_DateFrom | date |  |  | SI | Date From |
| ANGMOB_DateTo | date |  |  | SI | Date To |
| ANGMOB_Desc | varchar |  |  | NO | Description |
| ANGMOB_Owner | varchar |  |  | SI | Owner |
| ANGMOB_UpdatedDate | date |  |  | SI | Updated Date |
| ANGMOB_UpdatedTime | time |  |  | SI | Updated Time |
| ANGMOB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Pitch |
| Q02 | - |  |  | SI | Pitch Level (+/-) |
| Q03 | - |  |  | SI | Pitch Breaks |
| Q04 | - |  |  | SI | Monopitch |
| Q05 | - |  |  | SI | Voice Tremor |
| Q06 | - |  |  | SI | Myoclonus |
| Q07 | - |  |  | SI | Diplophonia |
| Q08 | - |  |  | SI | Loudness |
| Q10 | - |  |  | SI | Overall Loudness (+/-) |
| Q11 | - |  |  | SI | Excess Loudness Variation |
| Q12 | - |  |  | SI | Loudness Decay |
| Q13 | - |  |  | SI | Altering Loudness |
| Q14 | - |  |  | SI | Monoloudness |
| Q15 | - |  |  | SI | Voice Quality |
| Q16 | - |  |  | SI | Harsh Voice |
| Q17 | - |  |  | SI | Hoarse (Wet) |
| Q18 | - |  |  | SI | Breathy Voice (Continuous) |
| Q19 | - |  |  | SI | Breathy Voice (Transient) |
| Q20 | - |  |  | SI | Strained-Strangled Voice |
| Q21 | - |  |  | SI | Voice Stoppages |
| Q22 | - |  |  | SI | Glottal Fry |
| Q23 | - |  |  | SI | Resonance (& Intraoral Pressure) |
| Q24 | - |  |  | SI | Hypernasality |
| Q25 | - |  |  | SI | Hyponasality |
| Q26 | - |  |  | SI | Nasal Emission |
| Q27 | - |  |  | SI | Respiration |
| Q28 | - |  |  | SI | Forced Inspiration-Expiration |
| Q29 | - |  |  | SI | Audible Inspiration |
| Q30 | - |  |  | SI | Inhalatory Stridor |
| Q31 | - |  |  | SI | Grunt at end of Expiration |
| Q32 | - |  |  | SI | Prosody |
| Q33 | - |  |  | SI | Rate (+/-) |
| Q34 | - |  |  | SI | Short Phrases |
| Q35 | - |  |  | SI | Increased Rate in Segments |
| Q36 | - |  |  | SI | Reduced Stress |
| Q37 | - |  |  | SI | Variable Rate |
| Q38 | - |  |  | SI | Prolonged Intervals |
| Q39 | - |  |  | SI | Inappropriate Silences |
| Q40 | - |  |  | SI | Short Rushes of Speech |
| Q41 | - |  |  | SI | Exaggerated Stress |
| Q42 | - |  |  | SI | Excess & Equal Stress |
| Q43 | - |  |  | SI | Articulation |
| Q44 | - |  |  | SI | Imprecise Consonants |
| Q45 | - |  |  | SI | Prolonged Phonemes |
| Q46 | - |  |  | SI | Irregular Articulatory Breakdowns |
| Q47 | - |  |  | SI | Distorted Vowels |
| Q48 | - |  |  | SI | Other |
| Q49 | - |  |  | SI | Slow Alternating Motion Rate |
| Q50 | - |  |  | SI | Fast Alternating Motion Rate |
| Q51 | - |  |  | SI | Irregular Alternating Motion Rate |
| Q52 | - |  |  | SI | Simple Vocal Tic |
| Q53 | - |  |  | SI | Palilalia (Autoecholaelic Utterance) |
| Q54 | - |  |  | SI | Coprolalia (Involuntary Swearing) |
| Q55 | - |  |  | SI | Comments |
| Q56 | - |  |  | SI | Deviant Speech Characteristics - Dysarthria Rating... |
| Q57 | - |  |  | SI | Assign a value of 0-4 to each dimension listed abo... |
| Q58 | - |  |  | SI | If required (for pitch level and overall loudness)... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*