# questionnaire.QTCEENINF

> Estado Nutricional Infantil 0 - 4 años

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estado Nutricional Infantil 0 - 4 años

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q19 | varchar |  |  | SI | Kg. |
| Q20 | varchar |  |  | SI | cm |
| Q21 | varchar |  |  | SI | Kg/m² |
| QENI | varchar |  |  | SI | Estado Nutricional Infantil |
| QENIObsDR | varchar |  | FK | SI | Estado Nutricional Infantil DR |
| QIIM | bit |  |  | SI | Ingresar Información Manualmente |
| QNN019 | varchar |  |  | SI | Índice de masa corporal (IMC) |
| QNN022 | varchar |  |  | SI | Peso |
| QNN022ObsDR | varchar |  | FK | SI | Peso DR |
| QNN023 | varchar |  |  | SI | Talla |
| QNN023ObsDR | varchar |  | FK | SI | Talla DR |
| QNN029 | varchar |  |  | SI | Peso/Edad |
| QNN029ObsDR | varchar |  | FK | SI | Peso/Edad DR |
| QNN030 | varchar |  |  | SI | Peso/Talla |
| QNN030ObsDR | varchar |  | FK | SI | Peso/Talla DR |
| QNN031 | varchar |  |  | SI | Talla/Edad |
| QNN031ObsDR | varchar |  | FK | SI | Talla/Edad DR |
| QNN033 | varchar |  |  | SI | Calificación estado nutricional según IMC |
| QNN034 | varchar |  |  | SI | Diagnóstico nutricional integrado |
| QNN038 | varchar |  |  | SI | Tipo de alimentación (Antíguo) |
| QNN039 | varchar |  |  | SI | Detalle de alimentación (otras comidas) |
| QNN040 | varchar |  |  | SI | Tiempo de lactancia materna exclusiva |
| QNN041 | varchar |  |  | SI | Estado Nutricional PNAC |
| QNN041ObsDR | varchar |  | FK | SI | Estado Nutricional PNAC DR |
| QNN090 | varchar |  |  | SI | Tipo de Lactancia |
| QNN090ObsDR | varchar |  | FK | SI | Tipo de Lactancia DR |
| QPNN | varchar |  |  | SI | Paciente NANEAS |
| QSEN | varchar |  |  | SI | Usuario bajo algún programa del SENAME [REM]  |
| QTAI | varchar |  |  | SI | Tipo de Alimentación Infantil |
| QTAIObsDR | varchar |  | FK | SI | Tipo de Alimentación Infantil DR |
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