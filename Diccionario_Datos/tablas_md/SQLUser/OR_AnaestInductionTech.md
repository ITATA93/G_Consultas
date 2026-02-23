# SQLUser.OR_AnaestInductionTech

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAIND_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAIND_Childsub | double |  |  | NO | Childsub |
| ANAIND_RowId | varchar |  |  | NO | - |
| ANAIND_Type_DR | bigint |  | FK | SI | Des Ref MRCCareEventType |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Assessment phase |
| Q04 | - |  |  | SI | Self-Care |
| Q05 | - |  |  | SI | Eating |
| Q06 | - |  |  | SI | Grooming |
| Q07 | - |  |  | SI | Bathing |
| Q08 | - |  |  | SI | Dressing upper body |
| Q09 | - |  |  | SI | Dressing lower body |
| Q10 | - |  |  | SI | Toileting |
| Q11 | - |  |  | SI | Bladder management |
| Q12 | - |  |  | SI | Bowel management |
| Q13 | - |  |  | SI | Transfers |
| Q14 | - |  |  | SI | Sphincter Control |
| Q15 | - |  |  | SI | Transfers - bed, chair, wheelchair |
| Q16 | - |  |  | SI | Transfers - toilet |
| Q17 | - |  |  | SI | Transfers - tub, shower |
| Q18 | - |  |  | SI | Locomotion |
| Q19 | - |  |  | SI | Walking / Wheelchair |
| Q20 | - |  |  | SI | Method |
| Q21 | - |  |  | SI | Stairs |
| Q22 | - |  |  | SI | Motor subscale score |
| Q23 | - |  |  | SI | Communication |
| Q24 | - |  |  | SI | Comprehension |
| Q25 | - |  |  | SI | Method |
| Q26 | - |  |  | SI | Expression |
| Q27 | - |  |  | SI | Method |
| Q28 | - |  |  | SI | Social Cognition |
| Q29 | - |  |  | SI | Social interaction |
| Q30 | - |  |  | SI | Problem solving |
| Q31 | - |  |  | SI | Memory |
| Q32 | - |  |  | SI | Cognitive subscale score |
| Q33 | - |  |  | SI | Total FIM TM score |
| Q34 | - |  |  | SI | Leave no blanks. Enter 1 if patient is not testabl... |
| Q35 | - |  |  | SI | Guidelines for scoring |
| Q36 | - |  |  | SI | No Helper |
| Q37 | - |  |  | SI | Level 7 |
| Q38 | - |  |  | SI | Complete independence: Performs independently and ... |
| Q39 | - |  |  | SI | Level 6 |
| Q40 | - |  |  | SI | Modified independence: Uses an assistive device, o... |
| Q41 | - |  |  | SI | Helper - Modified Dependence |
| Q42 | - |  |  | SI | Level 5 |
| Q43 | - |  |  | SI | Supervision or set-up: Receives only cueing or coa... |
| Q44 | - |  |  | SI | Level 4 |
| Q45 | - |  |  | SI | Minimal assistance: Receives incidental help but p... |
| Q46 | - |  |  | SI | Level 3 |
| Q47 | - |  |  | SI | Receives moderate assistance: Performs more than h... |
| Q48 | - |  |  | SI | Helper - Complete Dependence |
| Q49 | - |  |  | SI | Level 2 |
| Q50 | - |  |  | SI | Maximal assistance: Provides less than half of the... |
| Q51 | - |  |  | SI | Level 1 |
| Q52 | - |  |  | SI | Receives total assistance Contributes less than 25... |
| Q53 | - |  |  | SI | Score |
| Q54 | - |  |  | SI | Classification |
| Q55 | - |  |  | SI | 18 - 126 |
| Q56 | - |  |  | SI | The higher the score, the higher the level of inde... |
| Q57 | - |  |  | SI | 18 - 126: The higher the score, the higher the lev... |
| Q58 | - |  |  | SI | Motor subscale score |
| Q59 | - |  |  | SI | Cognitive subscale score |
| Q60 | - |  |  | SI | Total FIM TM score |
| Q61 | - |  |  | SI | The FIM TM is an 18-item measurement tool that exp... |
| Q62 | - |  |  | SI | The higher the score, the higher the level of inde... |
| Q63 | - |  |  | SI | Total FIM TM score |
| Q64 | - |  |  | SI | Eating comment |
| Q65 | - |  |  | SI | Grooming comment |
| Q66 | - |  |  | SI | Bathing comment |
| Q67 | - |  |  | SI | Dressing upper body comment |
| Q68 | - |  |  | SI | Dressing lower body comment |
| Q69 | - |  |  | SI | Toileting comment |
| Q70 | - |  |  | SI | Bladder management comment |
| Q71 | - |  |  | SI | Bowel management comment |
| Q72 | - |  |  | SI | Transfers - bed, chair, wheelchair comment |
| Q73 | - |  |  | SI | Transfers - toilet comment |
| Q74 | - |  |  | SI | Transfers - tub, shower comment |
| Q75 | - |  |  | SI | Walking / Wheelchair comment |
| Q76 | - |  |  | SI | Stairs comment |
| Q77 | - |  |  | SI | Comprehension comment |
| Q78 | - |  |  | SI | Expression comment |
| Q79 | - |  |  | SI | Social interaction comment |
| Q80 | - |  |  | SI | Problem solving comment |
| Q81 | - |  |  | SI | Memory comment |
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