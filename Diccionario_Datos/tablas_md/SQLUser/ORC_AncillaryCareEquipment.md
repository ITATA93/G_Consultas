# SQLUser.ORC_AncillaryCareEquipment

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANCAEQ_RowId | bigint | PK |  | NO | - |
| ANCAEQ_Code | varchar |  |  | NO | Code |
| ANCAEQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANCAEQ_CreatedDate | date |  |  | SI | Created Date |
| ANCAEQ_CreatedTime | time |  |  | SI | Created Time |
| ANCAEQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANCAEQ_DateFrom | date |  |  | SI | Date From |
| ANCAEQ_DateTo | date |  |  | SI | Date To |
| ANCAEQ_Desc | varchar |  |  | NO | Description |
| ANCAEQ_Owner | varchar |  |  | SI | Owner |
| ANCAEQ_UpdatedDate | date |  |  | SI | Updated Date |
| ANCAEQ_UpdatedTime | time |  |  | SI | Updated Time |
| ANCAEQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Case History |
| Q02 | - |  |  | SI | Source of Referral |
| Q03 | - |  |  | SI | Source of Referral Comment |
| Q04 | - |  |  | SI | Medical History |
| Q05 | - |  |  | SI | Medical History |
| Q06 | - |  |  | SI | Medications |
| Q07 | - |  |  | SI | Vision |
| Q08 | - |  |  | SI | Vision Comment |
| Q09 | - |  |  | SI | Hearing History |
| Q10 | - |  |  | SI | Results |
| Q100 | - |  |  | SI | Short Sentences |
| Q101 | - |  |  | SI | Conversation |
| Q11 | - |  |  | SI | Hearing Aids |
| Q12 | - |  |  | SI | Hearing History Comment |
| Q13 | - |  |  | SI | Parent Relation |
| Q14 | - |  |  | SI | Family History of Communication Problems |
| Q15 | - |  |  | SI | Family History Comment |
| Q16 | - |  |  | SI | Prior Assessment |
| Q17 | - |  |  | SI | Speech Therapy Sessions |
| Q18 | - |  |  | SI | Psychology or Psychatric Diagnosis |
| Q19 | - |  |  | SI | Comment |
| Q20 | - |  |  | SI | Additional History |
| Q21 | - |  |  | SI | Onset of Stuttering |
| Q22 | - |  |  | SI | Patient Awareness of the Problem |
| Q23 | - |  |  | SI | Stuttering Increases During |
| Q24 | - |  |  | SI | Comment |
| Q25 | - |  |  | SI | Child Teased about Stuttering |
| Q26 | - |  |  | SI | Child's Reaction |
| Q27 | - |  |  | SI | Dysfluency is Noted to Specific Speech |
| Q28 | - |  |  | SI | Dysfluency Relapse |
| Q29 | - |  |  | SI | Types of Dysfluency |
| Q30 | - |  |  | SI | Secondary Behaviors |
| Q31 | - |  |  | SI | Specify |
| Q32 | - |  |  | SI | Parents Rating of Patient's Stuttering |
| Q33 | - |  |  | SI | Child has other Communication Problems |
| Q34 | - |  |  | SI | Comment |
| Q35 | - |  |  | SI | Stuttering Assessment |
| Q36 | - |  |  | SI | Behavioral Observation  during Testing |
| Q37 | - |  |  | SI | Cooperativeness during Session |
| Q38 | - |  |  | SI | Attention |
| Q39 | - |  |  | SI | Sitting Tolerance |
| Q40 | - |  |  | SI | Oral Motor  Examination |
| Q41 | - |  |  | SI | Structure |
| Q42 | - |  |  | SI | Structure Comment |
| Q43 | - |  |  | SI | Function |
| Q44 | - |  |  | SI | Function Comment |
| Q45 | - |  |  | SI | Task / CoreBehaviors |
| Q46 | - |  |  | SI | Counting - Whole-Word Repetition (%) |
| Q47 | - |  |  | SI | Counting - Part-Word Repetition (%) |
| Q48 | - |  |  | SI | Counting - Blocks (%) |
| Q49 | - |  |  | SI | Counting - Prolongations (%) |
| Q50 | - |  |  | SI | Counting - Fillers (%) |
| Q51 | - |  |  | SI | Reciting - Whole-Word Repetition (%) |
| Q52 | - |  |  | SI | Reciting - Part-Word Repetition (%) |
| Q53 | - |  |  | SI | Reciting - Blocks (%) |
| Q54 | - |  |  | SI | Reciting - Prolongations (%) |
| Q55 | - |  |  | SI | Reciting - Fillers (%) |
| Q56 | - |  |  | SI | Reading - Whole-Word Repetition (%) |
| Q57 | - |  |  | SI | Reading - Part-Word Repetition (%) |
| Q58 | - |  |  | SI | Reading - Blocks (%) |
| Q59 | - |  |  | SI | Reading - Prolongations (%) |
| Q60 | - |  |  | SI | Reading - Fillers (%) |
| Q61 | - |  |  | SI | Short Sentences - Whole-Word Repetition (%) |
| Q62 | - |  |  | SI | Short Sentences - Part-Word Repetition (%) |
| Q63 | - |  |  | SI | Short Sentences - Blocks (%) |
| Q64 | - |  |  | SI | Short Sentences - Prolongations (%) |
| Q65 | - |  |  | SI | Short Sentences - Fillers |
| Q66 | - |  |  | SI | Conversation - Whole-Word Repetition (%) |
| Q67 | - |  |  | SI | Conversation - Part-Word Repetition (%) |
| Q68 | - |  |  | SI | Conversation - Blocks (%) |
| Q69 | - |  |  | SI | Conversation - Prolongations (%) |
| Q70 | - |  |  | SI | Conversation - Fillers (%) |
| Q71 | - |  |  | SI | Secondary Behaviors |
| Q72 | - |  |  | SI | Secondary Behaviors |
| Q73 | - |  |  | SI | Max Stuttering Moment lasts approx (sec) |
| Q74 | - |  |  | SI | Comment |
| Q75 | - |  |  | SI | Diagnosis |
| Q76 | - |  |  | SI | Normal Dysfluency |
| Q77 | - |  |  | SI | Stuttering |
| Q78 | - |  |  | SI | Comment |
| Q79 | - |  |  | SI | Plan |
| Q80 | - |  |  | SI | Discharge |
| Q81 | - |  |  | SI | Report to Follow |
| Q82 | - |  |  | SI | Counselling |
| Q83 | - |  |  | SI | To Improve Speeh Fluency |
| Q84 | - |  |  | SI | Therapy Technique |
| Q85 | - |  |  | SI | Home-Based Training Program |
| Q86 | - |  |  | SI | Comment |
| Q87 | - |  |  | SI | Whole-Word Repetition (%) |
| Q88 | - |  |  | SI | Part-Word Repetition (%) |
| Q89 | - |  |  | SI | Blocks (%) |
| Q90 | - |  |  | SI | Fillers (%) |
| Q91 | - |  |  | SI | Whole-Word Repetition (%) |
| Q92 | - |  |  | SI | Part-Word Repetition (%) |
| Q93 | - |  |  | SI | Blocks (%) |
| Q94 | - |  |  | SI | Fillers (%) |
| Q95 | - |  |  | SI | Prolongations (%) |
| Q96 | - |  |  | SI | Prolongations (%) |
| Q97 | - |  |  | SI | Counting |
| Q98 | - |  |  | SI | Reciting |
| Q99 | - |  |  | SI | Reading |
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