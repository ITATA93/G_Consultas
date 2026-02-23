# SQLUser.CT_Override

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| OVR_ClassName | varchar |  |  | NO | Name of Class being overriden |
| OVR_LastUpdateDate | date |  |  | SI | Last Update Date |
| OVR_LastUpdateTime | time |  |  | SI | Last Update Time |
| OVR_RowID | varchar |  |  | NO | Id of actual entry being overriden
Exported as GU... |
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
| Q44 | - |  |  | SI | Articulation Assessment |
| Q45 | - |  |  | SI | Formal Articulation Test (JAT) Revealed the Follow... |
| Q46 | - |  |  | SI | Extra 1.1 |
| Q47 | - |  |  | SI | Extra 1.2 |
| Q48 | - |  |  | SI | Extra 1.3 |
| Q49 | - |  |  | SI | Extra 1.4 |
| Q50 | - |  |  | SI | Extra 1.5 |
| Q51 | - |  |  | SI | Extra 1.6 |
| Q52 | - |  |  | SI | Stimulable Speech Sounds |
| Q53 | - |  |  | SI | Extra 2.1 |
| Q54 | - |  |  | SI | Extra 2.2 |
| Q55 | - |  |  | SI | Extra 2.3 |
| Q56 | - |  |  | SI | Extra 2.4 |
| Q57 | - |  |  | SI | Extra 2.5 |
| Q58 | - |  |  | SI | Extra 2.6 |
| Q59 | - |  |  | SI | Phonological Process |
| Q60 | - |  |  | SI | Comment |
| Q61 | - |  |  | SI | Diagnosis |
| Q62 | - |  |  | SI | Within Normal Limits |
| Q63 | - |  |  | SI | Articulation Delay |
| Q64 | - |  |  | SI | Articulation & Phonological Disorder |
| Q65 | - |  |  | SI | Speech Intelligibility |
| Q66 | - |  |  | SI | Comment |
| Q67 | - |  |  | SI | Plan |
| Q68 | - |  |  | SI | Discharge |
| Q69 | - |  |  | SI | Report to Follow |
| Q70 | - |  |  | SI | Counselling |
| Q71 | - |  |  | SI | To be Able to Produce Misarticulated Sounds Correc... |
| Q72 | - |  |  | SI | Home-Based Articulation Training Program |
| Q73 | - |  |  | SI | Comment |
| Q74 | - |  |  | SI | Home-Based Articulation Training Program |
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