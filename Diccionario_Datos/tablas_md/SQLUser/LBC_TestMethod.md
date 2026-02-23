# SQLUser.LBC_TestMethod

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTM_RowID | bigint | PK |  | NO | - |
| LBCTM_Code | varchar |  |  | SI | Code |
| LBCTM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTM_CreatedDate | date |  |  | SI | Created Date |
| LBCTM_CreatedTime | time |  |  | SI | Created Time |
| LBCTM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTM_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTM_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTM_Desc | varchar |  |  | SI | Description |
| LBCTM_Owner | varchar |  |  | SI | Owner |
| LBCTM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q19 | - |  |  | SI | Kg. |
| Q20 | - |  |  | SI | cm |
| Q21 | - |  |  | SI | Kg/m² |
| QENI | - |  |  | SI | Estado Nutricional Infantil |
| QENIObsDR | - |  |  | SI | Estado Nutricional Infantil DR |
| QIIM | - |  |  | SI | Ingresar Información Manualmente |
| QNN019 | - |  |  | SI | Índice de masa corporal (IMC) |
| QNN022 | - |  |  | SI | Peso |
| QNN022ObsDR | - |  |  | SI | Peso DR |
| QNN023 | - |  |  | SI | Talla |
| QNN023ObsDR | - |  |  | SI | Talla DR |
| QNN029 | - |  |  | SI | Peso/Edad |
| QNN029ObsDR | - |  |  | SI | Peso/Edad DR |
| QNN030 | - |  |  | SI | Peso/Talla |
| QNN030ObsDR | - |  |  | SI | Peso/Talla DR |
| QNN031 | - |  |  | SI | Talla/Edad |
| QNN031ObsDR | - |  |  | SI | Talla/Edad DR |
| QNN033 | - |  |  | SI | Calificación estado nutricional según IMC |
| QNN034 | - |  |  | SI | Diagnóstico nutricional integrado |
| QNN038 | - |  |  | SI | Tipo de alimentación (Antíguo) |
| QNN039 | - |  |  | SI | Detalle de alimentación (otras comidas) |
| QNN040 | - |  |  | SI | Tiempo de lactancia materna exclusiva |
| QNN041 | - |  |  | SI | Estado Nutricional PNAC |
| QNN041ObsDR | - |  |  | SI | Estado Nutricional PNAC DR |
| QNN090 | - |  |  | SI | Tipo de Lactancia |
| QNN090ObsDR | - |  |  | SI | Tipo de Lactancia DR |
| QPNN | - |  |  | SI | Paciente NANEAS |
| QSEN | - |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
| QTAI | - |  |  | SI | Tipo de Alimentación Infantil |
| QTAIObsDR | - |  |  | SI | Tipo de Alimentación Infantil DR |
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