# questionnaire.QTCAHSPLSP

> Speech Pathology Assessment

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Speech Pathology Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Assessment |
| Q02 | varchar |  |  | SI | Speech Pathologist |
| Q03 | varchar |  |  | SI | Pre-morbid |
| Q04 | varchar |  |  | SI | Swallow |
| Q05 | varchar |  |  | SI | Speech |
| Q06 | varchar |  |  | SI | Language |
| Q07 | varchar |  |  | SI | Voice |
| Q08 | varchar |  |  | SI | Cognitive Communication |
| Q09 | varchar |  |  | SI | Augmentative and Alternative Communication (AAC) |
| Q10 | varchar |  |  | SI | Social Supports |
| Q11 | varchar |  |  | SI | Social Services |
| Q12 | varchar |  |  | SI | Occupation / Leisure |
| Q13 | varchar |  |  | SI | Cognitive Function |
| Q14 | varchar |  |  | SI | Orientation |
| Q15 | varchar |  |  | SI | Co-operative? |
| Q16 | varchar |  |  | SI | Other |
| Q17 | varchar |  |  | SI | Vision |
| Q18 | varchar |  |  | SI | Hearing |
| Q19 | varchar |  |  | SI | Patient’s perceived Problems |
| Q20 | varchar |  |  | SI | Patient’s Goals |
| Q21 | varchar |  |  | SI | Dysphagia Assessment |
| Q22 | varchar |  |  | SI | Dysphagia Assessment |
| Q23 | varchar |  |  | SI | Current Diet |
| Q24 | varchar |  |  | SI | Alternative Feeding |
| Q25 | varchar |  |  | SI | Alternative Feeding Note |
| Q26 | varchar |  |  | SI | Alertness |
| Q27 | varchar |  |  | SI | Positioning |
| Q28 | varchar |  |  | SI | Respiration |
| Q29 | varchar |  |  | SI | Oral Health / Dentition |
| Q30 | varchar |  |  | SI | Saliva Management |
| Q31 | varchar |  |  | SI | Other Observations |
| Q32 | varchar |  |  | SI | Risk Factors for Developing Aspiration Pneumonia |
| Q33 | varchar |  |  | SI | Oral Feeding Note |
| Q34 | varchar |  |  | SI | Bulbar Assessment |
| Q35 | varchar |  |  | SI | Cranial Nerve V |
| Q36 | varchar |  |  | SI | Cranial Nerve VII |
| Q37 | varchar |  |  | SI | Cranial Nerve IX-X |
| Q38 | varchar |  |  | SI | Cranial Nerve XII |
| Q39 | varchar |  |  | SI | Observed with |
| Q40 | varchar |  |  | SI | Manoeuvres / Strategies Trialled |
| Q41 | varchar |  |  | SI | Pre Oral Stage |
| Q42 | varchar |  |  | SI | Oral Stage |
| Q43 | varchar |  |  | SI | Pharyngeal Stage |
| Q44 | varchar |  |  | SI | Oesophageal Stage |
| Q45 | varchar |  |  | SI | Impression |
| Q46 | varchar |  |  | SI | Recommendations |
| Q47 | varchar |  |  | SI | Precautions |
| Q48 | varchar |  |  | SI | Plan |
| Q49 | varchar |  |  | SI | Communication |
| Q50 | varchar |  |  | SI | Motor Speech |
| Q51 | varchar |  |  | SI | Dysarthria |
| Q52 | varchar |  |  | SI | Dyspraxia |
| Q53 | varchar |  |  | SI | Intelligibility |
| Q54 | varchar |  |  | SI | Impression (Communication) |
| Q55 | varchar |  |  | SI | Language |
| Q56 | varchar |  |  | SI | Comprehension |
| Q57 | varchar |  |  | SI | Basic Information |
| Q58 | varchar |  |  | SI | Following Commands |
| Q59 | varchar |  |  | SI | Comments (Following Commands) |
| Q60 | varchar |  |  | SI | Abstract / Complex Information |
| Q61 | varchar |  |  | SI | Expression |
| Q62 | varchar |  |  | SI | Conversation |
| Q63 | varchar |  |  | SI | Able to Express Needs / Wants |
| Q64 | varchar |  |  | SI | Naming |
| Q65 | varchar |  |  | SI | Yes/No Response |
| Q66 | varchar |  |  | SI | Cognitive Communication |
| Q67 | varchar |  |  | SI | Impression (Language) |
| Q68 | varchar |  |  | SI | Voice |
| Q69 | varchar |  |  | SI | Quality |
| Q70 | varchar |  |  | SI | Volume |
| Q71 | varchar |  |  | SI | Respiration |
| Q72 | varchar |  |  | SI | Impression (Voice) |
| Q73 | varchar |  |  | SI | Main Problems Identified |
| Q74 | varchar |  |  | SI | Recommended Communication Strategies |
| Q75 | varchar |  |  | SI | Treatment Plan |
| Q76 | varchar |  |  | SI | Reason |
| Q77 | varchar |  |  | SI | Co-operative |
| Q78 | varchar |  |  | SI | Oral Trials |
| Q79 | varchar |  |  | SI | Social |
| Q80 | date |  |  | SI | Date |
| Q81 | time |  |  | SI | Time |
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