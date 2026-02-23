# questionnaire.QTCAHSPLSPD

> Speech Pathology Dysarthria Assessment

**Schema:** questionnaire
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Speech Pathology Dysarthria Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Assessment |
| Q02 | varchar |  |  | SI | Speech Pathologist |
| Q03 | varchar |  |  | SI | Case History |
| Q04 | varchar |  |  | SI | Difficulty |
| Q05 | varchar |  |  | SI | Do you have any difficulty with your speech? |
| Q06 | varchar |  |  | SI | Description |
| Q07 | varchar |  |  | SI | How would you describe your speech? |
| Q08 | varchar |  |  | SI | How is it different? (loudness, rate, effort, prec... |
| Q09 | varchar |  |  | SI | What did your speech sound like before? |
| Q10 | varchar |  |  | SI | Onset |
| Q11 | varchar |  |  | SI | How long have you had this problem? |
| Q12 | varchar |  |  | SI | Has it changed? |
| Q13 | varchar |  |  | SI | Who first noticed it? |
| Q14 | varchar |  |  | SI | Has it ever returned to normal? |
| Q15 | varchar |  |  | SI | Did you develop any other difficulties at the same... |
| Q16 | varchar |  |  | SI | Does medication impact on your speech? |
| Q17 | varchar |  |  | SI | Perception |
| Q18 | varchar |  |  | SI | Has anyone ever commented or had trouble understan... |
| Q19 | varchar |  |  | SI | Compensation |
| Q20 | varchar |  |  | SI | Does anything make your speech better / worse |
| Q21 | varchar |  |  | SI | What have you done to compensate for your speech d... |
| Q22 | varchar |  |  | SI | Have you had any help with your speech in the past... |
| Q23 | varchar |  |  | SI | Cause / Prognosis |
| Q24 | varchar |  |  | SI | Have you seen any other specialists? |
| Q25 | varchar |  |  | SI | What have you been told about your speech changes ... |
| Q26 | varchar |  |  | SI | Do you have any thoughts about what has caused the... |
| Q27 | varchar |  |  | SI | Other |
| Q28 | varchar |  |  | SI | Level of Education |
| Q29 | varchar |  |  | SI | Communication History |
| Q30 | varchar |  |  | SI | Swallowing History |
| Q31 | varchar |  |  | SI | Cogntive |
| Q32 | varchar |  |  | SI | Hearing |
| Q33 | varchar |  |  | SI | Physical Impairments |
| Q34 | varchar |  |  | SI | Level of Concern / Consequences (ICF) |
| Q35 | varchar |  |  | SI | Does your speech prevent you from doing anything o... |
| Q36 | varchar |  |  | SI | Goals |
| Q37 | varchar |  |  | SI | Do you want to change your speech? |
| Q38 | varchar |  |  | SI | What would you like to change most? |
| Q39 | varchar |  |  | SI | What do you want to get back to doing? |
| Q40 | varchar |  |  | SI | Bulbar Assessment |
| Q41 | varchar |  |  | SI | Cranial Nerves V |
| Q42 | varchar |  |  | SI | At rest, symmetry, ROM, sensation |
| Q43 | varchar |  |  | SI | Cranial Nerves VII |
| Q44 | varchar |  |  | SI | Facial symmetry at rest –upper / lower |
| Q45 | varchar |  |  | SI | Lip range of movement lateralization in exaggerate... |
| Q46 | varchar |  |  | SI | Lip range of movement pucker |
| Q47 | varchar |  |  | SI | Lip rate of movement “ oo-ee” (10 reps) |
| Q48 | varchar |  |  | SI | Lip strength – blow air into cheeks hold (15 secs) |
| Q49 | varchar |  |  | SI | Cranial Nerves IX-X |
| Q50 | varchar |  |  | SI | Cough |
| Q51 | varchar |  |  | SI | If cough is weak is it due to |
| Q52 | varchar |  |  | SI | Other describe |
| Q53 | varchar |  |  | SI | Taste sensation |
| Q54 | varchar |  |  | SI | Palatal movement: timing, elevation, symmetry |
| Q55 | varchar |  |  | SI | Phonation (remember to attempt all tasks 3 times) |
| Q56 | varchar |  |  | SI | Maximum phonation time ah |
| Q57 | varchar |  |  | SI | Maximum phonation time s |
| Q58 | varchar |  |  | SI | Maximum phonation time z |
| Q59 | varchar |  |  | SI | s:z ratio |
| Q60 | varchar |  |  | SI | Volume: count to 5 increasing in volume on each nu... |
| Q61 | varchar |  |  | SI | Pitch: sing a scale (6+ notes) |
| Q62 | varchar |  |  | SI | Voice quality |
| Q63 | varchar |  |  | SI | Voice quality note |
| Q64 | varchar |  |  | SI | Cranial Nerves XII |
| Q65 | varchar |  |  | SI | At rest (fasciculation, resting tremor). |
| Q66 | varchar |  |  | SI | On movement (strength, rate, range of movement, co... |
| Q67 | varchar |  |  | SI | Dentition / oral health |
| Q68 | varchar |  |  | SI | Respiratory system / co-ordination: at rest / spee... |
| Q69 | varchar |  |  | SI | Swallowing |
| Q70 | varchar |  |  | SI | Other comments |
| Q71 | varchar |  |  | SI | Alternating motion rates (p, t, k, ptk – rate per ... |
| Q72 | varchar |  |  | SI | Repetition of monosyllables |
| Q73 | varchar |  |  | SI | Repetition of phrases |
| Q74 | varchar |  |  | SI | Passage reading (Grandfather passage) |
| Q75 | varchar |  |  | SI | Conversational speech |
| Q76 | varchar |  |  | SI | Articulation |
| Q77 | varchar |  |  | SI | Prosody |
| Q78 | varchar |  |  | SI | Intelligibility |
| Q79 | varchar |  |  | SI | Impression / dysarthria diagnosis |
| Q80 | varchar |  |  | SI | Recommendations |
| Q81 | varchar |  |  | SI | Plan |
| Q82 | varchar |  |  | SI | ENT investigation indicated? |
| Q83 | varchar |  |  | SI | Referrals made |
| Q84 | varchar |  |  | SI | Education provided (verbal and handouts) |
| Q85 | varchar |  |  | SI | Intervention program |
| Q86 | varchar |  |  | SI | (Who? When? How long? What? Did it help) |
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