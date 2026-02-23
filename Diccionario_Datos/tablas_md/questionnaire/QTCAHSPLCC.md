# questionnaire.QTCAHSPLCC

> Cognitive Communication Assessment

**Schema:** questionnaire
**Columnas:** 142
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cognitive Communication Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Assessment |
| Q02 | varchar |  |  | SI | Speech Pathologist |
| Q03 | bit |  |  | SI | Three Identifiers Checked |
| Q04 | varchar |  |  | SI | Referral Trigger |
| Q05 | varchar |  |  | SI | A) Receptive Language |
| Q06 | varchar |  |  | SI | Following Commands |
| Q07 | numeric |  |  | SI | 1 Stage |
| Q08 | varchar |  |  | SI | 1 Stage  |
| Q09 | numeric |  |  | SI | 2 Stage  |
| Q10 | varchar |  |  | SI | 2 Stage  |
| Q100 | varchar |  |  | SI | /4 |
| Q101 | varchar |  |  | SI | /1 |
| Q11 | numeric |  |  | SI | 3 Stage |
| Q12 | varchar |  |  | SI | 3 Stage |
| Q13 | varchar |  |  | SI | Comparatives |
| Q14 | numeric |  |  | SI | Comparative Relationships |
| Q15 | varchar |  |  | SI | Comparative Relationships (Notes) |
| Q16 | varchar |  |  | SI | Complex Grammar |
| Q17 | numeric |  |  | SI | Sentence Level Comprehension |
| Q18 | varchar |  |  | SI | Sentence Level Comprehension (Notes) |
| Q19 | varchar |  |  | SI | B) Expressive Language |
| Q20 | varchar |  |  | SI | Naming |
| Q21 | numeric |  |  | SI | Naming Objects |
| Q22 | varchar |  |  | SI | Naming Objects |
| Q23 | numeric |  |  | SI | Naming Pictures |
| Q24 | varchar |  |  | SI | Naming Pictures |
| Q25 | varchar |  |  | SI | Providing Factual Information |
| Q26 | varchar |  |  | SI | Name |
| Q27 | varchar |  |  | SI | Address |
| Q28 | varchar |  |  | SI | General Statement (eg weather) |
| Q29 | varchar |  |  | SI | Verbal Reasoning |
| Q30 | varchar |  |  | SI | Using Narrative |
| Q31 | varchar |  |  | SI | Sequencing |
| Q32 | varchar |  |  | SI | Sentence Structure |
| Q33 | varchar |  |  | SI | Content |
| Q34 | varchar |  |  | SI | C) Reading |
| Q35 | varchar |  |  | SI | Reading Aloud |
| Q36 | numeric |  |  | SI | Single Word |
| Q37 | numeric |  |  | SI | Phrase |
| Q38 | varchar |  |  | SI | Factual Comprehension |
| Q39 | varchar |  |  | SI | Sentence |
| Q40 | varchar |  |  | SI | Paragraph |
| Q41 | varchar |  |  | SI | Inferential Comprehension |
| Q42 | varchar |  |  | SI | Paragraph |
| Q43 | varchar |  |  | SI | D) Writing |
| Q44 | varchar |  |  | SI | Automatic |
| Q45 | varchar |  |  | SI | Name |
| Q46 | varchar |  |  | SI | Address |
| Q47 | varchar |  |  | SI | Numbers |
| Q48 | varchar |  |  | SI | Single Words (List Writing) |
| Q49 | varchar |  |  | SI | Number of Words Written |
| Q50 | varchar |  |  | SI | Relevance |
| Q51 | varchar |  |  | SI | Spelling |
| Q52 | varchar |  |  | SI | Legibility |
| Q53 | varchar |  |  | SI | Sentence |
| Q54 | varchar |  |  | SI | Number of Words in Sentence |
| Q55 | varchar |  |  | SI | Relevance |
| Q56 | varchar |  |  | SI | Spelling |
| Q57 | varchar |  |  | SI | Legibility |
| Q58 | varchar |  |  | SI | Grammar |
| Q59 | varchar |  |  | SI | E) Pragmatics |
| Q60 | varchar |  |  | SI | Non-verbal |
| Q61 | varchar |  |  | SI | Intonation |
| Q62 | varchar |  |  | SI | Facial Expression |
| Q63 | varchar |  |  | SI | Eye Contact |
| Q64 | varchar |  |  | SI | Gestures |
| Q65 | varchar |  |  | SI | Conversational Skills |
| Q66 | varchar |  |  | SI | Initiation |
| Q67 | varchar |  |  | SI | Turn Taking |
| Q68 | varchar |  |  | SI | Verbosity |
| Q69 | varchar |  |  | SI | Linguistic Context |
| Q70 | varchar |  |  | SI | Topic Maintenance |
| Q71 | varchar |  |  | SI | Presupposition |
| Q72 | varchar |  |  | SI | Referencing Skills |
| Q73 | varchar |  |  | SI | Organisation of Narrative |
| Q74 | varchar |  |  | SI | Organisation |
| Q75 | varchar |  |  | SI | Completeness |
| Q76 | varchar |  |  | SI | F) Cognitive Observation |
| Q77 | varchar |  |  | SI | Alertness |
| Q78 | varchar |  |  | SI | Orientation |
| Q79 | varchar |  |  | SI | Insight |
| Q80 | varchar |  |  | SI | Motivation |
| Q81 | varchar |  |  | SI | Initiation |
| Q82 | varchar |  |  | SI | Attention |
| Q83 | varchar |  |  | SI | Speed of Processing |
| Q84 | varchar |  |  | SI | Organisation / Planning |
| Q85 | varchar |  |  | SI | Problem Solving |
| Q86 | varchar |  |  | SI | New Learning |
| Q87 | varchar |  |  | SI | Auditory Memory |
| Q88 | varchar |  |  | SI | Fatigue |
| Q89 | varchar |  |  | SI | Able to Communicate Healthcare Needs |
| Q90 | varchar |  |  | SI | Able to Communicate Healthcare Needs (Notes) |
| Q91 | varchar |  |  | SI | Impression |
| Q92 | varchar |  |  | SI | Plan |
| Q93 | varchar |  |  | SI | /3 |
| Q94 | varchar |  |  | SI | /3 |
| Q95 | varchar |  |  | SI | /3 |
| Q96 | varchar |  |  | SI | /4 |
| Q97 | varchar |  |  | SI | /6 |
| Q98 | varchar |  |  | SI | /4 |
| Q99 | varchar |  |  | SI | /5 |
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