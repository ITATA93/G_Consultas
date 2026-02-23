# questionnaire.QTCAHSPLSLH

> Speech-Language Case History (Paeds)

**Schema:** questionnaire
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Speech-Language Case History (Paeds)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Language Case History |
| Q02 | varchar |  |  | SI | Source of Referral |
| Q03 | varchar |  |  | SI | Source of Referral Comment |
| Q04 | varchar |  |  | SI | Medical History |
| Q05 | varchar |  |  | SI | Medical History |
| Q06 | varchar |  |  | SI | Medications |
| Q07 | varchar |  |  | SI | Vision |
| Q08 | varchar |  |  | SI | Vision Comment |
| Q09 | varchar |  |  | SI | Hearing History |
| Q10 | varchar |  |  | SI | Results |
| Q11 | varchar |  |  | SI | Hearing Aids |
| Q12 | varchar |  |  | SI | Hearing History Comment |
| Q13 | varchar |  |  | SI | Parent Relation |
| Q14 | varchar |  |  | SI | Family History of Communication Problems |
| Q15 | varchar |  |  | SI | Family History Comment |
| Q16 | varchar |  |  | SI | Prior Assessment |
| Q17 | varchar |  |  | SI | Speech Therapy Sessions |
| Q18 | varchar |  |  | SI | Psychology or Psychatric Diagnosis |
| Q19 | varchar |  |  | SI | Comment |
| Q20 | varchar |  |  | SI | Developmental History |
| Q21 | varchar |  |  | SI | Motor Assessment |
| Q22 | varchar |  |  | SI | Speech |
| Q23 | varchar |  |  | SI | Educational History |
| Q24 | varchar |  |  | SI | Educational History |
| Q25 | varchar |  |  | SI | Enrolled |
| Q26 | varchar |  |  | SI | Academic Performance |
| Q27 | varchar |  |  | SI | Social Interaction History |
| Q28 | varchar |  |  | SI | Interaction with Others |
| Q29 | varchar |  |  | SI | Usually Interacts with |
| Q30 | varchar |  |  | SI | Using Objects & Playing |
| Q31 | varchar |  |  | SI | Behavioral History |
| Q32 | varchar |  |  | SI | Behaviors |
| Q33 | varchar |  |  | SI | Imitation |
| Q34 | varchar |  |  | SI | Behavioral Observations during Testing |
| Q35 | varchar |  |  | SI | Cooperativeness during Session |
| Q36 | varchar |  |  | SI | Attention |
| Q37 | varchar |  |  | SI | Sitting Tolerance |
| Q38 | varchar |  |  | SI | Oral Motor Examination |
| Q39 | varchar |  |  | SI | Structure |
| Q40 | varchar |  |  | SI | Structure Comment |
| Q41 | varchar |  |  | SI | Function |
| Q42 | varchar |  |  | SI | Function Comment |
| Q43 | varchar |  |  | SI | Comment |
| Q44 | varchar |  |  | SI | Language Assessment |
| Q45 | varchar |  |  | SI | Prelinguistic Skills |
| Q46 | varchar |  |  | SI | Turn Taking |
| Q47 | varchar |  |  | SI | Language |
| Q48 | varchar |  |  | SI | Joint Attention |
| Q49 | varchar |  |  | SI | Follows Commands |
| Q50 | varchar |  |  | SI | Use of Objects Appropriately |
| Q51 | varchar |  |  | SI | Responds to Name - Receptively |
| Q52 | varchar |  |  | SI | Responds to Name - Expressively |
| Q53 | varchar |  |  | SI | Family |
| Q54 | varchar |  |  | SI | Possessive |
| Q55 | varchar |  |  | SI | Negative |
| Q56 | varchar |  |  | SI | Groups - Receptively |
| Q57 | varchar |  |  | SI | Groups - Expressively |
| Q58 | varchar |  |  | SI | WH Questions - Receptively |
| Q59 | varchar |  |  | SI | WH Questions - Expressively |
| Q60 | varchar |  |  | SI | Numbers & Letters - Receptively |
| Q61 | varchar |  |  | SI | Numbers & Letters - Expressively |
| Q62 | varchar |  |  | SI | Categorization |
| Q63 | varchar |  |  | SI | Categorization |
| Q64 | varchar |  |  | SI | Sentences |
| Q65 | varchar |  |  | SI | Syntactic Structure |
| Q66 | varchar |  |  | SI | Speech Intelligibility |
| Q67 | varchar |  |  | SI | Setences Comment |
| Q68 | varchar |  |  | SI | Diagnosis |
| Q69 | bit |  |  | SI | WNL Receptive & Expressive Language Skills   |
| Q70 | varchar |  |  | SI | Language Delay |
| Q71 | varchar |  |  | SI | Receptively |
| Q72 | varchar |  |  | SI | Expressively |
| Q73 | varchar |  |  | SI | Language Disorder |
| Q74 | varchar |  |  | SI | Receptively |
| Q75 | varchar |  |  | SI | Expressively |
| Q76 | varchar |  |  | SI | Comment |
| Q77 | varchar |  |  | SI | Treatment Plan |
| Q78 | bit |  |  | SI | Discharge |
| Q79 | bit |  |  | SI | Report to Follow |
| Q80 | bit |  |  | SI | Counselling |
| Q81 | varchar |  |  | SI | To be Enrolled in |
| Q82 | bit |  |  | SI | To Improve Receptive and Expressive Language Abili... |
| Q83 | bit |  |  | SI | Home-Based Language Stimulation Instructions were ... |
| Q84 | varchar |  |  | SI | Next Session Goals |
| Q85 | varchar |  |  | SI | Comment |
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