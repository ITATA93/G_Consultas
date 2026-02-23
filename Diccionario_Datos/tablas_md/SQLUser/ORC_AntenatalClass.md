# SQLUser.ORC_AntenatalClass

**Schema:** SQLUser
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTCLA_RowId | bigint | PK |  | NO | - |
| ANTCLA_Code | varchar |  |  | NO | Code |
| ANTCLA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANTCLA_CreatedDate | date |  |  | SI | Created Date |
| ANTCLA_CreatedTime | time |  |  | SI | Created Time |
| ANTCLA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANTCLA_DateFrom | date |  |  | SI | Date From |
| ANTCLA_DateTo | date |  |  | SI | Date To |
| ANTCLA_Desc | varchar |  |  | NO | Description |
| ANTCLA_Owner | varchar |  |  | SI | Owner |
| ANTCLA_UpdatedDate | date |  |  | SI | Updated Date |
| ANTCLA_UpdatedTime | time |  |  | SI | Updated Time |
| ANTCLA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of Assessment |
| Q02 | - |  |  | SI | Speech Pathologist |
| Q03 | - |  |  | SI | Case History |
| Q04 | - |  |  | SI | Difficulty |
| Q05 | - |  |  | SI | Do you have any difficulty with your speech? |
| Q06 | - |  |  | SI | Description |
| Q07 | - |  |  | SI | How would you describe your speech? |
| Q08 | - |  |  | SI | How is it different? (loudness, rate, effort, prec... |
| Q09 | - |  |  | SI | What did your speech sound like before? |
| Q10 | - |  |  | SI | Onset |
| Q11 | - |  |  | SI | How long have you had this problem? |
| Q12 | - |  |  | SI | Has it changed? |
| Q13 | - |  |  | SI | Who first noticed it? |
| Q14 | - |  |  | SI | Has it ever returned to normal? |
| Q15 | - |  |  | SI | Did you develop any other difficulties at the same... |
| Q16 | - |  |  | SI | Does medication impact on your speech? |
| Q17 | - |  |  | SI | Perception |
| Q18 | - |  |  | SI | Has anyone ever commented or had trouble understan... |
| Q19 | - |  |  | SI | Compensation |
| Q20 | - |  |  | SI | Does anything make your speech better / worse |
| Q21 | - |  |  | SI | What have you done to compensate for your speech d... |
| Q22 | - |  |  | SI | Have you had any help with your speech in the past... |
| Q23 | - |  |  | SI | Cause / Prognosis |
| Q24 | - |  |  | SI | Have you seen any other specialists? |
| Q25 | - |  |  | SI | What have you been told about your speech changes ... |
| Q26 | - |  |  | SI | Do you have any thoughts about what has caused the... |
| Q27 | - |  |  | SI | Other |
| Q28 | - |  |  | SI | Level of Education |
| Q29 | - |  |  | SI | Communication History |
| Q30 | - |  |  | SI | Swallowing History |
| Q31 | - |  |  | SI | Cogntive |
| Q32 | - |  |  | SI | Hearing |
| Q33 | - |  |  | SI | Physical Impairments |
| Q34 | - |  |  | SI | Level of Concern / Consequences (ICF) |
| Q35 | - |  |  | SI | Does your speech prevent you from doing anything o... |
| Q36 | - |  |  | SI | Goals |
| Q37 | - |  |  | SI | Do you want to change your speech? |
| Q38 | - |  |  | SI | What would you like to change most? |
| Q39 | - |  |  | SI | What do you want to get back to doing? |
| Q40 | - |  |  | SI | Bulbar Assessment |
| Q41 | - |  |  | SI | Cranial Nerves V |
| Q42 | - |  |  | SI | At rest, symmetry, ROM, sensation |
| Q43 | - |  |  | SI | Cranial Nerves VII |
| Q44 | - |  |  | SI | Facial symmetry at rest –upper / lower |
| Q45 | - |  |  | SI | Lip range of movement lateralization in exaggerate... |
| Q46 | - |  |  | SI | Lip range of movement pucker |
| Q47 | - |  |  | SI | Lip rate of movement “ oo-ee” (10 reps) |
| Q48 | - |  |  | SI | Lip strength – blow air into cheeks hold (15 secs) |
| Q49 | - |  |  | SI | Cranial Nerves IX-X |
| Q50 | - |  |  | SI | Cough |
| Q51 | - |  |  | SI | If cough is weak is it due to |
| Q52 | - |  |  | SI | Other describe |
| Q53 | - |  |  | SI | Taste sensation |
| Q54 | - |  |  | SI | Palatal movement: timing, elevation, symmetry |
| Q55 | - |  |  | SI | Phonation (remember to attempt all tasks 3 times) |
| Q56 | - |  |  | SI | Maximum phonation time ah |
| Q57 | - |  |  | SI | Maximum phonation time s |
| Q58 | - |  |  | SI | Maximum phonation time z |
| Q59 | - |  |  | SI | s:z ratio |
| Q60 | - |  |  | SI | Volume: count to 5 increasing in volume on each nu... |
| Q61 | - |  |  | SI | Pitch: sing a scale (6+ notes) |
| Q62 | - |  |  | SI | Voice quality |
| Q63 | - |  |  | SI | Voice quality note |
| Q64 | - |  |  | SI | Cranial Nerves XII |
| Q65 | - |  |  | SI | At rest (fasciculation, resting tremor). |
| Q66 | - |  |  | SI | On movement (strength, rate, range of movement, co... |
| Q67 | - |  |  | SI | Dentition / oral health |
| Q68 | - |  |  | SI | Respiratory system / co-ordination: at rest / spee... |
| Q69 | - |  |  | SI | Swallowing |
| Q70 | - |  |  | SI | Other comments |
| Q71 | - |  |  | SI | Alternating motion rates (p, t, k, ptk – rate per ... |
| Q72 | - |  |  | SI | Repetition of monosyllables |
| Q73 | - |  |  | SI | Repetition of phrases |
| Q74 | - |  |  | SI | Passage reading (Grandfather passage) |
| Q75 | - |  |  | SI | Conversational speech |
| Q76 | - |  |  | SI | Articulation |
| Q77 | - |  |  | SI | Prosody |
| Q78 | - |  |  | SI | Intelligibility |
| Q79 | - |  |  | SI | Impression / dysarthria diagnosis |
| Q80 | - |  |  | SI | Recommendations |
| Q81 | - |  |  | SI | Plan |
| Q82 | - |  |  | SI | ENT investigation indicated? |
| Q83 | - |  |  | SI | Referrals made |
| Q84 | - |  |  | SI | Education provided (verbal and handouts) |
| Q85 | - |  |  | SI | Intervention program |
| Q86 | - |  |  | SI | (Who? When? How long? What? Did it help) |
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