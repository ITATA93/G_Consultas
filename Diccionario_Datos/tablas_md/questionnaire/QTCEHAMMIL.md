# questionnaire.QTCEHAMMIL

> Escala de Hamilton para valoración de la Depresión (1960)

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Hamilton para valoración de la Depresión (1960)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQQ01 | varchar |  |  | SI | - |
| CQQ02 | varchar |  |  | SI | - |
| CQQ03 | varchar |  |  | SI | - |
| CQQ04 | varchar |  |  | SI | - |
| CQQ05 | varchar |  |  | SI | - |
| CQQ06 | varchar |  |  | SI | - |
| CQQ07 | varchar |  |  | SI | - |
| CQQ08 | varchar |  |  | SI | - |
| CQQ09 | varchar |  |  | SI | - |
| CQQ10 | varchar |  |  | SI | - |
| CQQ11 | varchar |  |  | SI | - |
| CQQ12 | varchar |  |  | SI | - |
| CQQ13 | varchar |  |  | SI | - |
| CQQ14 | varchar |  |  | SI | - |
| CQQ15 | varchar |  |  | SI | - |
| CQQ16 | varchar |  |  | SI | - |
| CQQ17 | varchar |  |  | SI | - |
| QQ01 | varchar |  |  | SI | Humor depresivo (tristeza, desesperanza, desamparo... |
| QQ02 | varchar |  |  | SI | Sentimientos de culpa |
| QQ03 | varchar |  |  | SI | Suicidio |
| QQ04 | varchar |  |  | SI | Insomnio precoz |
| QQ05 | varchar |  |  | SI | Insomnio intermedio |
| QQ06 | varchar |  |  | SI | Insomnio tardío |
| QQ07 | varchar |  |  | SI | Trabajo y actividades |
| QQ08 | varchar |  |  | SI | Inhibición psicomotora (lentitud de pensamiento y ... |
| QQ09 | varchar |  |  | SI | Agitación psicomotora |
| QQ10 | varchar |  |  | SI | Ansiedad Psíquica |
| QQ11 | varchar |  |  | SI | Ansiedad somática (signos físicos de ansiedad) |
| QQ12 | varchar |  |  | SI | Síntomas Somáticos Gastrointestinales |
| QQ13 | varchar |  |  | SI | Síntomas Somáticos Generales |
| QQ14 | varchar |  |  | SI | Síntomas genitales (tales como: disminución de la ... |
| QQ15 | varchar |  |  | SI | Hipocondria |
| QQ16 | varchar |  |  | SI | Introspección (insight) |
| QQ17 | varchar |  |  | SI | Pérdida de Peso |
| QQ22 | varchar |  |  | SI | Resultado Escala Hamilton |
| QQ22ObsDR | varchar |  | FK | SI | Resultado Escala Hamilton DR |
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