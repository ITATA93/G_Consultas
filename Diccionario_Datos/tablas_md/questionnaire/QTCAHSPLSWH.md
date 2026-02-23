# questionnaire.QTCAHSPLSWH

> Swallowing Case History (Paeds)

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Swallowing Case History (Paeds)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Source of Referral |
| Q02 | varchar |  |  | SI | Source of Referral Comment |
| Q03 | varchar |  |  | SI | Medical History |
| Q04 | varchar |  |  | SI | Medical History |
| Q05 | varchar |  |  | SI | Medications |
| Q06 | varchar |  |  | SI | Vision |
| Q07 | varchar |  |  | SI | Vision Comment |
| Q08 | varchar |  |  | SI | Hearing History |
| Q09 | varchar |  |  | SI | Results |
| Q10 | varchar |  |  | SI | Hearing Aids |
| Q11 | varchar |  |  | SI | Hearing History Comment |
| Q12 | varchar |  |  | SI | Parent Relation |
| Q13 | varchar |  |  | SI | Family History of Communication |
| Q14 | varchar |  |  | SI | Family History Comment |
| Q15 | varchar |  |  | SI | Prior Feeding or Swallowing Assessment |
| Q16 | varchar |  |  | SI | Previous MBS Study |
| Q17 | varchar |  |  | SI | Previous Feeding Evaluation |
| Q18 | varchar |  |  | SI | Previous Upper GI Study |
| Q19 | varchar |  |  | SI | Comment |
| Q20 | varchar |  |  | SI | Feeding & Nutrition History |
| Q21 | varchar |  |  | SI | Initial Feeding |
| Q22 | varchar |  |  | SI | Problems with Feeding during Infancy |
| Q23 | varchar |  |  | SI | Alternative Feeding During Early Infancy / Childho... |
| Q24 | varchar |  |  | SI | Current Milk Formula |
| Q25 | varchar |  |  | SI | Milk Formula Comment |
| Q26 | numeric |  |  | SI | Total Amount of Bottle Feeds per Day (cc) |
| Q27 | numeric |  |  | SI | Total Amount of Bottle Feeds per Day (times per da... |
| Q28 | varchar |  |  | SI | Tolerated Consistencies |
| Q29 | varchar |  |  | SI | Typical Meals |
| Q30 | varchar |  |  | SI | Typical Meal Comment |
| Q31 | varchar |  |  | SI | Patient Demonstrated the Following |
| Q32 | varchar |  |  | SI | Comment |
| Q33 | varchar |  |  | SI | Self Feeds - Able With |
| Q34 | varchar |  |  | SI | Self-Feeds - Not Able With |
| Q35 | varchar |  |  | SI | Current Feeding Status |
| Q36 | varchar |  |  | SI | Meal Duration |
| Q37 | varchar |  |  | SI | Comment |
| Q38 | varchar |  |  | SI | Swallowing Assessment |
| Q39 | varchar |  |  | SI | Oral Motor Examination |
| Q40 | varchar |  |  | SI | Oral Motor Examination Structure Comment |
| Q41 | varchar |  |  | SI | Oral Motor Examination Function Comment |
| Q42 | varchar |  |  | SI | Food Utensils |
| Q43 | varchar |  |  | SI | Positioning |
| Q44 | varchar |  |  | SI | Self Feeding |
| Q45 | varchar |  |  | SI | Bedside Swallowing Evaluation |
| Q46 | varchar |  |  | SI | Patient Demonstrated the Following |
| Q47 | varchar |  |  | SI | Oral Sensory Development |
| Q48 | varchar |  |  | SI | Sucking |
| Q49 | varchar |  |  | SI | Suckling |
| Q50 | varchar |  |  | SI | Bite Reflex |
| Q51 | varchar |  |  | SI | Suck-Swallow-Breathe Coordination |
| Q52 | varchar |  |  | SI | Swallow Trigger |
| Q53 | varchar |  |  | SI | Laryngeal Elevation |
| Q54 | varchar |  |  | SI | Pharyngeal Residues |
| Q55 | varchar |  |  | SI | Comment |
| Q56 | varchar |  |  | SI | Diagnosis |
| Q57 | varchar |  |  | SI | WNL Swallowing Mechanism |
| Q58 | varchar |  |  | SI | Oral Dysphagia |
| Q59 | varchar |  |  | SI | Oropharyngeal Dysphagia |
| Q60 | varchar |  |  | SI | Comment |
| Q61 | varchar |  |  | SI | Plan |
| Q62 | varchar |  |  | SI | Plan |
| Q63 | varchar |  |  | SI | Feeding Method |
| Q64 | varchar |  |  | SI | Feeding Technique |
| Q65 | varchar |  |  | SI | Feeding Position |
| Q66 | varchar |  |  | SI | Swallowing Stimulation Exercises |
| Q67 | varchar |  |  | SI | Oral Motor Exercises |
| Q68 | varchar |  |  | SI | Oral Hygiene Advice |
| Q69 | varchar |  |  | SI | Home-Based Swallowing Stimulation Program |
| Q70 | varchar |  |  | SI | Comment |
| Q71 | varchar |  |  | SI | Case History |
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