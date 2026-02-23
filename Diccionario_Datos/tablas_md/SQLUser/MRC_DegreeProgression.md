# SQLUser.MRC_DegreeProgression

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEGPRO_RowId | bigint | PK |  | NO | - |
| DEGPRO_Code | varchar |  |  | NO | Code |
| DEGPRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEGPRO_CreatedDate | date |  |  | SI | Created Date |
| DEGPRO_CreatedTime | time |  |  | SI | Created Time |
| DEGPRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEGPRO_DateFrom | date |  |  | SI | Date From |
| DEGPRO_DateTo | date |  |  | SI | Date To |
| DEGPRO_Desc | varchar |  |  | NO | Description |
| DEGPRO_Owner | varchar |  |  | SI | Owner |
| DEGPRO_UpdatedDate | date |  |  | SI | Updated Date |
| DEGPRO_UpdatedTime | time |  |  | SI | Updated Time |
| DEGPRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | T.Dolor |
| Q02 | - |  |  | SI | Dolor |
| Q09 | - |  |  | SI | T.Habilidad para caminar |
| Q10 | - |  |  | SI | Habilidad para caminar |
| Q17 | - |  |  | SI | T.Movilidad |
| Q18 | - |  |  | SI | Movilidad |
| Q24 | - |  |  | SI | Resultado Evaluación Funcional Cadera |
| Q24ObsDR | - |  |  | SI | Resultado Evaluación Funcional Cadera DR |
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