# questionnaire.QTCAHSPLAH

> Articulation Case History (Paeds)

**Schema:** questionnaire
**Columnas:** 115
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Articulation Case History (Paeds)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Case History |
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
| Q44 | varchar |  |  | SI | Articulation Assessment |
| Q45 | varchar |  |  | SI | Formal Articulation Test (JAT) Revealed the Follow... |
| Q46 | varchar |  |  | SI | Extra 1.1 |
| Q47 | varchar |  |  | SI | Extra 1.2 |
| Q48 | varchar |  |  | SI | Extra 1.3 |
| Q49 | varchar |  |  | SI | Extra 1.4 |
| Q50 | varchar |  |  | SI | Extra 1.5 |
| Q51 | varchar |  |  | SI | Extra 1.6 |
| Q52 | varchar |  |  | SI | Stimulable Speech Sounds |
| Q53 | varchar |  |  | SI | Extra 2.1 |
| Q54 | varchar |  |  | SI | Extra 2.2 |
| Q55 | varchar |  |  | SI | Extra 2.3 |
| Q56 | varchar |  |  | SI | Extra 2.4 |
| Q57 | varchar |  |  | SI | Extra 2.5 |
| Q58 | varchar |  |  | SI | Extra 2.6 |
| Q59 | varchar |  |  | SI | Phonological Process |
| Q60 | varchar |  |  | SI | Comment |
| Q61 | varchar |  |  | SI | Diagnosis |
| Q62 | bit |  |  | SI | Within Normal Limits |
| Q63 | varchar |  |  | SI | Articulation Delay |
| Q64 | varchar |  |  | SI | Articulation & Phonological Disorder |
| Q65 | varchar |  |  | SI | Speech Intelligibility |
| Q66 | varchar |  |  | SI | Comment |
| Q67 | varchar |  |  | SI | Plan |
| Q68 | bit |  |  | SI | Discharge |
| Q69 | bit |  |  | SI | Report to Follow |
| Q70 | bit |  |  | SI | Counselling |
| Q71 | bit |  |  | SI | To be Able to Produce Misarticulated Sounds Correc... |
| Q72 | bit |  |  | SI | Home-Based Articulation Training Program |
| Q73 | varchar |  |  | SI | Comment |
| Q74 | bit |  |  | SI | Home-Based Articulation Training Program |
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