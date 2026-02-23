# SQLUser.LBC_CancerCode

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCC_RowID | bigint | PK |  | NO | - |
| LBCCC_Code | varchar |  |  | NO | Code  |
| LBCCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCC_CreatedDate | date |  |  | SI | Created Date |
| LBCCC_CreatedTime | time |  |  | SI | Created Time |
| LBCCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCC_DateFrom | date |  |  | SI | From Date |
| LBCCC_DateTo | date |  |  | SI | To Date |
| LBCCC_Department_DR | bigint |  | FK | SI | Des Ref Department |
| LBCCC_Desc | varchar |  |  | NO | Description |
| LBCCC_Owner | varchar |  |  | SI | Owner |
| LBCCC_Sequence | double |  |  | SI | Sequence |
| LBCCC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Historia de asma en la infancia |
| Q02 | - |  |  | SI | Historia de sibilancias recurrentes (más de 6 mese... |
| Q03 | - |  |  | SI | Historia de disnea o sensación de “pecho apretado”... |
| Q04 | - |  |  | SI | Historia de tos o disnea inducidas por: risa, ejer... |
| Q05 | - |  |  | SI | Alivio inmediato (± 15 minutos) con el uso de BD |
| Q06 | - |  |  | SI | Alivio espontáneo en corto tiempo (horas) de sínto... |
| Q07 | - |  |  | SI | Antecedentes familiares de asma bronquial |
| Q08 | - |  |  | SI | Antecedentes de enfermedades atópicas |
| QRCDA | - |  |  | SI | Resultado Puntaje Criterios Diagnósticos Asma |
| QRCDAObsDR | - |  |  | SI | Resultado Puntaje Criterios Diagnósticos Asma DR |
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