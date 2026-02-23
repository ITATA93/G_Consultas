# SQLUser.ORC_AnonymousDelivery

**Schema:** SQLUser
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANODEL_RowId | bigint | PK |  | NO | - |
| ANODEL_Code | varchar |  |  | NO | Code |
| ANODEL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANODEL_CreatedDate | date |  |  | SI | Created Date |
| ANODEL_CreatedTime | time |  |  | SI | Created Time |
| ANODEL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANODEL_DateFrom | date |  |  | SI | Date From |
| ANODEL_DateTo | date |  |  | SI | Date To |
| ANODEL_Desc | varchar |  |  | NO | Description |
| ANODEL_Owner | varchar |  |  | SI | Owner |
| ANODEL_UpdatedDate | date |  |  | SI | Updated Date |
| ANODEL_UpdatedTime | time |  |  | SI | Updated Time |
| ANODEL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of Assessment |
| Q02 | - |  |  | SI | Speech Pathologist |
| Q03 | - |  |  | SI | Pre-morbid |
| Q04 | - |  |  | SI | Swallow |
| Q05 | - |  |  | SI | Speech |
| Q06 | - |  |  | SI | Language |
| Q07 | - |  |  | SI | Voice |
| Q08 | - |  |  | SI | Cognitive Communication |
| Q09 | - |  |  | SI | Augmentative and Alternative Communication (AAC) |
| Q10 | - |  |  | SI | Social Supports |
| Q11 | - |  |  | SI | Social Services |
| Q12 | - |  |  | SI | Occupation / Leisure |
| Q13 | - |  |  | SI | Cognitive Function |
| Q14 | - |  |  | SI | Orientation |
| Q15 | - |  |  | SI | Co-operative? |
| Q16 | - |  |  | SI | Other |
| Q17 | - |  |  | SI | Vision |
| Q18 | - |  |  | SI | Hearing |
| Q19 | - |  |  | SI | Patient’s perceived Problems |
| Q20 | - |  |  | SI | Patient’s Goals |
| Q21 | - |  |  | SI | Dysphagia Assessment |
| Q22 | - |  |  | SI | Dysphagia Assessment |
| Q23 | - |  |  | SI | Current Diet |
| Q24 | - |  |  | SI | Alternative Feeding |
| Q25 | - |  |  | SI | Alternative Feeding Note |
| Q26 | - |  |  | SI | Alertness |
| Q27 | - |  |  | SI | Positioning |
| Q28 | - |  |  | SI | Respiration |
| Q29 | - |  |  | SI | Oral Health / Dentition |
| Q30 | - |  |  | SI | Saliva Management |
| Q31 | - |  |  | SI | Other Observations |
| Q32 | - |  |  | SI | Risk Factors for Developing Aspiration Pneumonia |
| Q33 | - |  |  | SI | Oral Feeding Note |
| Q34 | - |  |  | SI | Bulbar Assessment |
| Q35 | - |  |  | SI | Cranial Nerve V |
| Q36 | - |  |  | SI | Cranial Nerve VII |
| Q37 | - |  |  | SI | Cranial Nerve IX-X |
| Q38 | - |  |  | SI | Cranial Nerve XII |
| Q39 | - |  |  | SI | Observed with |
| Q40 | - |  |  | SI | Manoeuvres / Strategies Trialled |
| Q41 | - |  |  | SI | Pre Oral Stage |
| Q42 | - |  |  | SI | Oral Stage |
| Q43 | - |  |  | SI | Pharyngeal Stage |
| Q44 | - |  |  | SI | Oesophageal Stage |
| Q45 | - |  |  | SI | Impression |
| Q46 | - |  |  | SI | Recommendations |
| Q47 | - |  |  | SI | Precautions |
| Q48 | - |  |  | SI | Plan |
| Q49 | - |  |  | SI | Communication |
| Q50 | - |  |  | SI | Motor Speech |
| Q51 | - |  |  | SI | Dysarthria |
| Q52 | - |  |  | SI | Dyspraxia |
| Q53 | - |  |  | SI | Intelligibility |
| Q54 | - |  |  | SI | Impression (Communication) |
| Q55 | - |  |  | SI | Language |
| Q56 | - |  |  | SI | Comprehension |
| Q57 | - |  |  | SI | Basic Information |
| Q58 | - |  |  | SI | Following Commands |
| Q59 | - |  |  | SI | Comments (Following Commands) |
| Q60 | - |  |  | SI | Abstract / Complex Information |
| Q61 | - |  |  | SI | Expression |
| Q62 | - |  |  | SI | Conversation |
| Q63 | - |  |  | SI | Able to Express Needs / Wants |
| Q64 | - |  |  | SI | Naming |
| Q65 | - |  |  | SI | Yes/No Response |
| Q66 | - |  |  | SI | Cognitive Communication |
| Q67 | - |  |  | SI | Impression (Language) |
| Q68 | - |  |  | SI | Voice |
| Q69 | - |  |  | SI | Quality |
| Q70 | - |  |  | SI | Volume |
| Q71 | - |  |  | SI | Respiration |
| Q72 | - |  |  | SI | Impression (Voice) |
| Q73 | - |  |  | SI | Main Problems Identified |
| Q74 | - |  |  | SI | Recommended Communication Strategies |
| Q75 | - |  |  | SI | Treatment Plan |
| Q76 | - |  |  | SI | Reason |
| Q77 | - |  |  | SI | Co-operative |
| Q78 | - |  |  | SI | Oral Trials |
| Q79 | - |  |  | SI | Social |
| Q80 | - |  |  | SI | Date |
| Q81 | - |  |  | SI | Time |
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