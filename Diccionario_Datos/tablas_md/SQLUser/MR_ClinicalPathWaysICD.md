# SQLUser.MR_ClinicalPathWaysICD

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICD_ParRef | varchar | PK |  | NO | MR_ClinicalPathWays Parent Reference |
| CQQ01 | - |  |  | SI | (null) |
| CQQ02 | - |  |  | SI | (null) |
| CQQ03 | - |  |  | SI | (null) |
| CQQ04 | - |  |  | SI | (null) |
| CQQ05 | - |  |  | SI | (null) |
| CQQ06 | - |  |  | SI | (null) |
| CQQ07 | - |  |  | SI | (null) |
| CQQ08 | - |  |  | SI | (null) |
| CQQ09 | - |  |  | SI | (null) |
| CQQ10 | - |  |  | SI | (null) |
| CQQ11 | - |  |  | SI | (null) |
| CQQ12 | - |  |  | SI | (null) |
| CQQ13 | - |  |  | SI | (null) |
| CQQ14 | - |  |  | SI | (null) |
| CQQ15 | - |  |  | SI | (null) |
| CQQ16 | - |  |  | SI | (null) |
| CQQ17 | - |  |  | SI | (null) |
| ICD_Childsub | double |  |  | NO | Childsub |
| ICD_ICD_DR | bigint |  | FK | SI | Des Ref ICD |
| ICD_RowId | varchar |  |  | NO | - |
| QQ01 | - |  |  | SI | Humor depresivo (tristeza, desesperanza, desamparo... |
| QQ02 | - |  |  | SI | Sentimientos de culpa |
| QQ03 | - |  |  | SI | Suicidio |
| QQ04 | - |  |  | SI | Insomnio precoz |
| QQ05 | - |  |  | SI | Insomnio intermedio |
| QQ06 | - |  |  | SI | Insomnio tardío |
| QQ07 | - |  |  | SI | Trabajo y actividades |
| QQ08 | - |  |  | SI | Inhibición psicomotora (lentitud de pensamiento y ... |
| QQ09 | - |  |  | SI | Agitación psicomotora |
| QQ10 | - |  |  | SI | Ansiedad Psíquica |
| QQ11 | - |  |  | SI | Ansiedad somática (signos físicos de ansiedad) |
| QQ12 | - |  |  | SI | Síntomas Somáticos Gastrointestinales |
| QQ13 | - |  |  | SI | Síntomas Somáticos Generales |
| QQ14 | - |  |  | SI | Síntomas genitales (tales como: disminución de la ... |
| QQ15 | - |  |  | SI | Hipocondria |
| QQ16 | - |  |  | SI | Introspección (insight) |
| QQ17 | - |  |  | SI | Pérdida de Peso |
| QQ22 | - |  |  | SI | Resultado Escala Hamilton |
| QQ22ObsDR | - |  |  | SI | Resultado Escala Hamilton DR |
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