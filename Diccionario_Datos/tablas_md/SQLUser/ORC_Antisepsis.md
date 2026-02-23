# SQLUser.ORC_Antisepsis

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTIS_RowId | bigint | PK |  | NO | - |
| ANTIS_Code | varchar |  |  | NO | Code |
| ANTIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANTIS_CreatedDate | date |  |  | SI | Created Date |
| ANTIS_CreatedTime | time |  |  | SI | Created Time |
| ANTIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANTIS_DateFrom | date |  |  | SI | Date From |
| ANTIS_DateTo | date |  |  | SI | Date To |
| ANTIS_Desc | varchar |  |  | NO | Description |
| ANTIS_Owner | varchar |  |  | SI | Owner |
| ANTIS_UpdatedDate | date |  |  | SI | Updated Date |
| ANTIS_UpdatedTime | time |  |  | SI | Updated Time |
| ANTIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Source of Referral |
| Q02 | - |  |  | SI | Source of Referral Comment |
| Q03 | - |  |  | SI | Medical History |
| Q04 | - |  |  | SI | Medical History |
| Q05 | - |  |  | SI | Medications |
| Q06 | - |  |  | SI | Vision |
| Q07 | - |  |  | SI | Vision Comment |
| Q08 | - |  |  | SI | Hearing History |
| Q09 | - |  |  | SI | Results |
| Q10 | - |  |  | SI | Hearing Aids |
| Q11 | - |  |  | SI | Hearing History Comment |
| Q12 | - |  |  | SI | Parent Relation |
| Q13 | - |  |  | SI | Family History of Communication |
| Q14 | - |  |  | SI | Family History Comment |
| Q15 | - |  |  | SI | Prior Feeding or Swallowing Assessment |
| Q16 | - |  |  | SI | Previous MBS Study |
| Q17 | - |  |  | SI | Previous Feeding Evaluation |
| Q18 | - |  |  | SI | Previous Upper GI Study |
| Q19 | - |  |  | SI | Comment |
| Q20 | - |  |  | SI | Feeding & Nutrition History |
| Q21 | - |  |  | SI | Initial Feeding |
| Q22 | - |  |  | SI | Problems with Feeding during Infancy |
| Q23 | - |  |  | SI | Alternative Feeding During Early Infancy / Childho... |
| Q24 | - |  |  | SI | Current Milk Formula |
| Q25 | - |  |  | SI | Milk Formula Comment |
| Q26 | - |  |  | SI | Total Amount of Bottle Feeds per Day (cc) |
| Q27 | - |  |  | SI | Total Amount of Bottle Feeds per Day (times per da... |
| Q28 | - |  |  | SI | Tolerated Consistencies |
| Q29 | - |  |  | SI | Typical Meals |
| Q30 | - |  |  | SI | Typical Meal Comment |
| Q31 | - |  |  | SI | Patient Demonstrated the Following |
| Q32 | - |  |  | SI | Comment |
| Q33 | - |  |  | SI | Self Feeds - Able With |
| Q34 | - |  |  | SI | Self-Feeds - Not Able With |
| Q35 | - |  |  | SI | Current Feeding Status |
| Q36 | - |  |  | SI | Meal Duration |
| Q37 | - |  |  | SI | Comment |
| Q38 | - |  |  | SI | Swallowing Assessment |
| Q39 | - |  |  | SI | Oral Motor Examination |
| Q40 | - |  |  | SI | Oral Motor Examination Structure Comment |
| Q41 | - |  |  | SI | Oral Motor Examination Function Comment |
| Q42 | - |  |  | SI | Food Utensils |
| Q43 | - |  |  | SI | Positioning |
| Q44 | - |  |  | SI | Self Feeding |
| Q45 | - |  |  | SI | Bedside Swallowing Evaluation |
| Q46 | - |  |  | SI | Patient Demonstrated the Following |
| Q47 | - |  |  | SI | Oral Sensory Development |
| Q48 | - |  |  | SI | Sucking |
| Q49 | - |  |  | SI | Suckling |
| Q50 | - |  |  | SI | Bite Reflex |
| Q51 | - |  |  | SI | Suck-Swallow-Breathe Coordination |
| Q52 | - |  |  | SI | Swallow Trigger |
| Q53 | - |  |  | SI | Laryngeal Elevation |
| Q54 | - |  |  | SI | Pharyngeal Residues |
| Q55 | - |  |  | SI | Comment |
| Q56 | - |  |  | SI | Diagnosis |
| Q57 | - |  |  | SI | WNL Swallowing Mechanism |
| Q58 | - |  |  | SI | Oral Dysphagia |
| Q59 | - |  |  | SI | Oropharyngeal Dysphagia |
| Q60 | - |  |  | SI | Comment |
| Q61 | - |  |  | SI | Plan |
| Q62 | - |  |  | SI | Plan |
| Q63 | - |  |  | SI | Feeding Method |
| Q64 | - |  |  | SI | Feeding Technique |
| Q65 | - |  |  | SI | Feeding Position |
| Q66 | - |  |  | SI | Swallowing Stimulation Exercises |
| Q67 | - |  |  | SI | Oral Motor Exercises |
| Q68 | - |  |  | SI | Oral Hygiene Advice |
| Q69 | - |  |  | SI | Home-Based Swallowing Stimulation Program |
| Q70 | - |  |  | SI | Comment |
| Q71 | - |  |  | SI | Case History |
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