# SQLUser.MRC_ClinNotesType

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNT_RowId | bigint | PK |  | NO | - |
| CNT_Code | varchar |  |  | NO | Code |
| CNT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CNT_CreatedDate | date |  |  | SI | Created Date |
| CNT_CreatedTime | time |  |  | SI | Created Time |
| CNT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNT_DateFrom | date |  |  | SI | DateFrom |
| CNT_DateTo | date |  |  | SI | DateTo |
| CNT_Desc | varchar |  |  | NO | Description |
| CNT_EncSOAPICategory | varchar |  |  | SI | Encounter Record SOAPI Category |
| CNT_HTMLTemplate_DR | bigint |  | FK | SI | HTMLTemplate |
| CNT_Owner | varchar |  |  | SI | Owner |
| CNT_Template | varchar |  |  | SI | Template |
| CNT_UpdatedDate | date |  |  | SI | Updated Date |
| CNT_UpdatedTime | time |  |  | SI | Updated Time |
| CNT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ1 | - |  |  | SI | (null) |
| CQ2 | - |  |  | SI | (null) |
| CQ3 | - |  |  | SI | (null) |
| CQ4 | - |  |  | SI | (null) |
| CQ5 | - |  |  | SI | (null) |
| CQ6 | - |  |  | SI | (null) |
| Q09 | - |  |  | SI | Presión Arterial Sistólica |
| Q09ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q1 | - |  |  | SI | Presión arterial |
| Q10 | - |  |  | SI | Presión Arterial Diastólica |
| Q10ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q12 | - |  |  | SI | Medición de Presión Arterial |
| Q13 | - |  |  | SI | Presión Arterial |
| Q14 | - |  |  | SI | Diabetes |
| Q16 | - |  |  | SI | MMSE |
| Q17 | - |  |  | SI | En el último mes se ha sentido deprimido |
| Q18 | - |  |  | SI | En el último mes se ha sentido nervioso o angustia... |
| Q19 | - |  |  | SI | Recuerde Ingresar Resultado en forma Manual en Cue... |
| Q2 | - |  |  | SI | ¿Tiene Ud. diagnóstico de diabetes? |
| Q20 | - |  |  | SI | Lee diario, revista o libro |
| Q3 | - |  |  | SI | ¿Lee ud. diario, revista o libro? |
| Q4 | - |  |  | SI | MMSE (Minimental abreviado) |
| Q5 | - |  |  | SI | ¿En el último mes se ha sentido deprimido o bajone... |
| Q6 | - |  |  | SI | ¿En el último mes se ha sentido Ud. muy nervioso, ... |
| Q7 | - |  |  | SI | Resultado EFAM B |
| Q7ObsDR | - |  |  | SI | Resultado EFAM B DR |
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