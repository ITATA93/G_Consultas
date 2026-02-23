# SQLUser.ORC_AngiographyProcedure

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANGPRO_RowId | bigint | PK |  | NO | - |
| ANGPRO_Code | varchar |  |  | NO | Code |
| ANGPRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANGPRO_CreatedDate | date |  |  | SI | Created Date |
| ANGPRO_CreatedTime | time |  |  | SI | Created Time |
| ANGPRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANGPRO_DateFrom | date |  |  | SI | Date From |
| ANGPRO_DateTo | date |  |  | SI | Date To |
| ANGPRO_Desc | varchar |  |  | NO | Description |
| ANGPRO_Owner | varchar |  |  | SI | Owner |
| ANGPRO_UpdatedDate | date |  |  | SI | Updated Date |
| ANGPRO_UpdatedTime | time |  |  | SI | Updated Time |
| ANGPRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Language Case History |
| Q02 | - |  |  | SI | Source of Referral |
| Q03 | - |  |  | SI | Source of Referral Comment |
| Q04 | - |  |  | SI | Medical History |
| Q05 | - |  |  | SI | Medical History |
| Q06 | - |  |  | SI | Medications |
| Q07 | - |  |  | SI | Vision |
| Q08 | - |  |  | SI | Vision Comment |
| Q09 | - |  |  | SI | Hearing History |
| Q10 | - |  |  | SI | Results |
| Q11 | - |  |  | SI | Hearing Aids |
| Q12 | - |  |  | SI | Hearing History Comment |
| Q13 | - |  |  | SI | Parent Relation |
| Q14 | - |  |  | SI | Family History of Communication Problems |
| Q15 | - |  |  | SI | Family History Comment |
| Q16 | - |  |  | SI | Prior Assessment |
| Q17 | - |  |  | SI | Speech Therapy Sessions |
| Q18 | - |  |  | SI | Psychology or Psychatric Diagnosis |
| Q19 | - |  |  | SI | Comment |
| Q20 | - |  |  | SI | Developmental History |
| Q21 | - |  |  | SI | Motor Assessment |
| Q22 | - |  |  | SI | Speech |
| Q23 | - |  |  | SI | Educational History |
| Q24 | - |  |  | SI | Educational History |
| Q25 | - |  |  | SI | Enrolled |
| Q26 | - |  |  | SI | Academic Performance |
| Q27 | - |  |  | SI | Social Interaction History |
| Q28 | - |  |  | SI | Interaction with Others |
| Q29 | - |  |  | SI | Usually Interacts with |
| Q30 | - |  |  | SI | Using Objects & Playing |
| Q31 | - |  |  | SI | Behavioral History |
| Q32 | - |  |  | SI | Behaviors |
| Q33 | - |  |  | SI | Imitation |
| Q34 | - |  |  | SI | Behavioral Observations during Testing |
| Q35 | - |  |  | SI | Cooperativeness during Session |
| Q36 | - |  |  | SI | Attention |
| Q37 | - |  |  | SI | Sitting Tolerance |
| Q38 | - |  |  | SI | Oral Motor Examination |
| Q39 | - |  |  | SI | Structure |
| Q40 | - |  |  | SI | Structure Comment |
| Q41 | - |  |  | SI | Function |
| Q42 | - |  |  | SI | Function Comment |
| Q43 | - |  |  | SI | Comment |
| Q44 | - |  |  | SI | Language Assessment |
| Q45 | - |  |  | SI | Prelinguistic Skills |
| Q46 | - |  |  | SI | Turn Taking |
| Q47 | - |  |  | SI | Language |
| Q48 | - |  |  | SI | Joint Attention |
| Q49 | - |  |  | SI | Follows Commands |
| Q50 | - |  |  | SI | Use of Objects Appropriately |
| Q51 | - |  |  | SI | Responds to Name - Receptively |
| Q52 | - |  |  | SI | Responds to Name - Expressively |
| Q53 | - |  |  | SI | Family |
| Q54 | - |  |  | SI | Possessive |
| Q55 | - |  |  | SI | Negative |
| Q56 | - |  |  | SI | Groups - Receptively |
| Q57 | - |  |  | SI | Groups - Expressively |
| Q58 | - |  |  | SI | WH Questions - Receptively |
| Q59 | - |  |  | SI | WH Questions - Expressively |
| Q60 | - |  |  | SI | Numbers & Letters - Receptively |
| Q61 | - |  |  | SI | Numbers & Letters - Expressively |
| Q62 | - |  |  | SI | Categorization |
| Q63 | - |  |  | SI | Categorization |
| Q64 | - |  |  | SI | Sentences |
| Q65 | - |  |  | SI | Syntactic Structure |
| Q66 | - |  |  | SI | Speech Intelligibility |
| Q67 | - |  |  | SI | Setences Comment |
| Q68 | - |  |  | SI | Diagnosis |
| Q69 | - |  |  | SI | WNL Receptive & Expressive Language Skills |
| Q70 | - |  |  | SI | Language Delay |
| Q71 | - |  |  | SI | Receptively |
| Q72 | - |  |  | SI | Expressively |
| Q73 | - |  |  | SI | Language Disorder |
| Q74 | - |  |  | SI | Receptively |
| Q75 | - |  |  | SI | Expressively |
| Q76 | - |  |  | SI | Comment |
| Q77 | - |  |  | SI | Treatment Plan |
| Q78 | - |  |  | SI | Discharge |
| Q79 | - |  |  | SI | Report to Follow |
| Q80 | - |  |  | SI | Counselling |
| Q81 | - |  |  | SI | To be Enrolled in |
| Q82 | - |  |  | SI | To Improve Receptive and Expressive Language Abili... |
| Q83 | - |  |  | SI | Home-Based Language Stimulation Instructions were ... |
| Q84 | - |  |  | SI | Next Session Goals |
| Q85 | - |  |  | SI | Comment |
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