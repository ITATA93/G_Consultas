# SQLUser.CT_ExChgRate

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTEXC_CTCUR_ParRef | bigint | PK |  | NO | Des Ref to CTCUR |
| CTEXC_CTFP_DR | varchar |  | FK | SI | Not Used Des Ref to CTFP |
| CTEXC_ChildSub | double |  |  | NO | CTEXC ChildSub (New Key) |
| CTEXC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTEXC_CreatedDate | date |  |  | SI | Created Date |
| CTEXC_CreatedTime | time |  |  | SI | Created Time |
| CTEXC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTEXC_Date | date |  |  | NO | Effective Date |
| CTEXC_Rate | double |  |  | NO | Exchange Rate |
| CTEXC_RowId | varchar |  |  | NO | - |
| CTEXC_UpdatedDate | date |  |  | SI | Updated Date |
| CTEXC_UpdatedTime | time |  |  | SI | Updated Time |
| CTEXC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1. Do you think you have been eating enough food l... |
| Q04 | - |  |  | SI | 2. Do you think you have lost weight recently with... |
| Q05 | - |  |  | SI | Prompt: Ask the patient if they have been feeling ... |
| Q06 | - |  |  | SI | If Yes, how much weight do you think you have lost... |
| Q07 | - |  |  | SI | 3. Does the patient look frail or undernourished |
| Q08 | - |  |  | SI | Assess patient for signs of muscle wasting, poor s... |
| Q09 | - |  |  | SI | Reason for referral to dietitian |
| Q10 | - |  |  | SI | • Malnutrition (ANT score > 4) |
| Q11 | - |  |  | SI | • Enteral nutrition |
| Q12 | - |  |  | SI | • Parenteral nutrition |
| Q13 | - |  |  | SI | • Refeeding syndrome |
| Q14 | - |  |  | SI | • Burns > 10% |
| Q15 | - |  |  | SI | • Postoperative upper gastrointestinal (GI) surger... |
| Q16 | - |  |  | SI | • Severe life threatening food allergy |
| Q17 | - |  |  | SI | • Acute management of GI conditions e.g. Crohn’s, ... |
| Q18 | - |  |  | SI | • Pressure injuries |
| Q19 | - |  |  | SI | • Chronic disease requiring education e.g. new dia... |
| Q20 | - |  |  | SI | The Adult Nutrition Tool (ANT) is a validated tool... |
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