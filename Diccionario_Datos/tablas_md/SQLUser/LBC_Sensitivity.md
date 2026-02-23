# SQLUser.LBC_Sensitivity

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSENS_RowID | bigint | PK |  | NO | - |
| LBCSENS_Code | varchar |  |  | SI | Code |
| LBCSENS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSENS_CreatedDate | date |  |  | SI | Created Date |
| LBCSENS_CreatedTime | time |  |  | SI | Created Time |
| LBCSENS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSENS_DateFrom | date |  |  | SI | From Date |
| LBCSENS_DateTo | date |  |  | SI | To Date |
| LBCSENS_Desc | varchar |  |  | SI | Description |
| LBCSENS_Owner | varchar |  |  | SI | Owner |
| LBCSENS_Type | varchar |  |  | SI | Sensitivity Type
Standard Type: LabSensitivityTyp... |
| LBCSENS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSENS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSENS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Ha perdido peso este último tiempo? |
| Q02 | - |  |  | SI | Si ha perdido peso ¿Cuánto ha perdido? |
| Q03 | - |  |  | SI | ¿Se alimenta deficientemente por falta de apetito? |
| Q04 | - |  |  | SI | Riesgo Bajo (Se alimenta bien y no ha perdido peso... |
| Q05 | - |  |  | SI | Riesgo Medio (No se alimenta y ha perdido peso) |
| Q06 | - |  |  | SI | Riesgo Alto (No se alimenta bien y ha perdido mas ... |
| Q07 | - |  |  | SI | Sin riesgo de desnutrición |
| Q08 | - |  |  | SI | En riesgo de desnutrición |
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