# SQLUser.MRC_ClinPathwayStatus

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLPS_RowId | bigint | PK |  | NO | - |
| CLPS_Code | varchar |  |  | NO | Code |
| CLPS_CreatedDate | date |  |  | SI | Created Date |
| CLPS_CreatedTime | time |  |  | SI | Created Time |
| CLPS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLPS_Desc | varchar |  |  | NO | Description |
| CLPS_UpdatedDate | date |  |  | SI | Updated Date |
| CLPS_UpdatedTime | time |  |  | SI | Updated Time |
| CLPS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQRMB1 | - |  |  | SI | (null) |
| CQRMB10 | - |  |  | SI | (null) |
| CQRMB2 | - |  |  | SI | (null) |
| CQRMB3 | - |  |  | SI | (null) |
| CQRMB4 | - |  |  | SI | (null) |
| CQRMB5 | - |  |  | SI | (null) |
| CQRMB6 | - |  |  | SI | (null) |
| CQRMB7 | - |  |  | SI | (null) |
| CQRMB8 | - |  |  | SI | (null) |
| QRBron | - |  |  | SI | Resultado de la Evaluación |
| QRBronObsDR | - |  |  | SI | Resultado de la Evaluación DR |
| QRMB1 | - |  |  | SI | Malformaciones congénitas |
| QRMB10 | - |  |  | SI | Síndrome bronquial obstructivo recurrente (SBOR) |
| QRMB2 | - |  |  | SI | Tabaquismo materno |
| QRMB3 | - |  |  | SI | Hospitalización anterior |
| QRMB4 | - |  |  | SI | Desnutrición |
| QRMB5 | - |  |  | SI | Baja escolaridad materna |
| QRMB6 | - |  |  | SI | Bajo peso de nacimiento, < 2500 grs. |
| QRMB7 | - |  |  | SI | Lactancia materna insuficiente, < 4 meses |
| QRMB8 | - |  |  | SI | Madre adolescente (10 - 19 años) |
| QRRbron | - |  |  | SI | Resultado Evaluación |
| QRRbronObsDR | - |  |  | SI | Resultado Evaluación DR |
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
| Qres | - |  |  | SI | Resultado Score Riesgo Morir Bronconeumonia |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*