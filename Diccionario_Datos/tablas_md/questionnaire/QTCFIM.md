# questionnaire.QTCFIM

> FIM (TM)

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(FIM (TM))*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Assessment phase |
| Q04 | varchar |  |  | SI | Self-Care |
| Q05 | varchar |  |  | SI | Eating |
| Q06 | varchar |  |  | SI | Grooming |
| Q07 | varchar |  |  | SI | Bathing |
| Q08 | varchar |  |  | SI | Dressing upper body |
| Q09 | varchar |  |  | SI | Dressing lower body |
| Q10 | varchar |  |  | SI | Toileting |
| Q11 | varchar |  |  | SI | Bladder management |
| Q12 | varchar |  |  | SI | Bowel management |
| Q13 | varchar |  |  | SI | Transfers |
| Q14 | varchar |  |  | SI | Sphincter Control |
| Q15 | varchar |  |  | SI | Transfers - bed, chair, wheelchair |
| Q16 | varchar |  |  | SI | Transfers - toilet |
| Q17 | varchar |  |  | SI | Transfers - tub, shower |
| Q18 | varchar |  |  | SI | Locomotion |
| Q19 | varchar |  |  | SI | Walking / Wheelchair |
| Q20 | varchar |  |  | SI | Method |
| Q21 | varchar |  |  | SI | Stairs |
| Q22 | varchar |  |  | SI | Motor subscale score |
| Q23 | varchar |  |  | SI | Communication |
| Q24 | varchar |  |  | SI | Comprehension |
| Q25 | varchar |  |  | SI | Method |
| Q26 | varchar |  |  | SI | Expression |
| Q27 | varchar |  |  | SI | Method |
| Q28 | varchar |  |  | SI | Social Cognition |
| Q29 | varchar |  |  | SI | Social interaction |
| Q30 | varchar |  |  | SI | Problem solving |
| Q31 | varchar |  |  | SI | Memory |
| Q32 | varchar |  |  | SI | Cognitive subscale score |
| Q33 | varchar |  |  | SI | Total FIM TM score |
| Q34 | varchar |  |  | SI | Leave no blanks. Enter 1 if patient is not testabl... |
| Q35 | varchar |  |  | SI | Guidelines for scoring |
| Q36 | varchar |  |  | SI | No Helper |
| Q37 | varchar |  |  | SI | Level 7 |
| Q38 | varchar |  |  | SI | Complete independence: Performs independently and ... |
| Q39 | varchar |  |  | SI | Level 6 |
| Q40 | varchar |  |  | SI | Modified independence: Uses an assistive device, o... |
| Q41 | varchar |  |  | SI | Helper - Modified Dependence |
| Q42 | varchar |  |  | SI | Level 5 |
| Q43 | varchar |  |  | SI | Supervision or set-up: Receives only cueing or coa... |
| Q44 | varchar |  |  | SI | Level 4 |
| Q45 | varchar |  |  | SI | Minimal assistance: Receives incidental help but p... |
| Q46 | varchar |  |  | SI | Level 3 |
| Q47 | varchar |  |  | SI | Receives moderate assistance: Performs more than h... |
| Q48 | varchar |  |  | SI | Helper - Complete Dependence |
| Q49 | varchar |  |  | SI | Level 2 |
| Q50 | varchar |  |  | SI | Maximal assistance: Provides less than half of the... |
| Q51 | varchar |  |  | SI | Level 1 |
| Q52 | varchar |  |  | SI | Receives total assistance Contributes less than 25... |
| Q53 | varchar |  |  | SI | Score |
| Q54 | varchar |  |  | SI | Classification |
| Q55 | varchar |  |  | SI | 18 - 126 |
| Q56 | varchar |  |  | SI | The higher the score, the higher the level of inde... |
| Q57 | varchar |  |  | SI | 18 - 126: The higher the score, the higher the lev... |
| Q58 | varchar |  |  | SI | Motor subscale score |
| Q59 | varchar |  |  | SI | Cognitive subscale score |
| Q60 | varchar |  |  | SI | Total FIM TM score |
| Q61 | varchar |  |  | SI | The FIM TM is an 18-item measurement tool that exp... |
| Q62 | varchar |  |  | SI | The higher the score, the higher the level of inde... |
| Q63 | varchar |  |  | SI | Total FIM TM score |
| Q64 | varchar |  |  | SI | Eating comment |
| Q65 | varchar |  |  | SI | Grooming comment |
| Q66 | varchar |  |  | SI | Bathing comment |
| Q67 | varchar |  |  | SI | Dressing upper body comment |
| Q68 | varchar |  |  | SI | Dressing lower body comment |
| Q69 | varchar |  |  | SI | Toileting comment |
| Q70 | varchar |  |  | SI | Bladder management comment |
| Q71 | varchar |  |  | SI | Bowel management comment |
| Q72 | varchar |  |  | SI | Transfers - bed, chair, wheelchair comment |
| Q73 | varchar |  |  | SI | Transfers - toilet comment |
| Q74 | varchar |  |  | SI | Transfers - tub, shower comment |
| Q75 | varchar |  |  | SI | Walking / Wheelchair comment |
| Q76 | varchar |  |  | SI | Stairs comment |
| Q77 | varchar |  |  | SI | Comprehension comment |
| Q78 | varchar |  |  | SI | Expression comment |
| Q79 | varchar |  |  | SI | Social interaction comment |
| Q80 | varchar |  |  | SI | Problem solving comment |
| Q81 | varchar |  |  | SI | Memory comment |
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