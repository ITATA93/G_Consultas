# SQLUser.LBC_WorksheetTestSet

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCWSTS_ParRef | bigint | PK |  | NO | Parent Worsheet Definition DR |
| LBCWSTS_AllItems | varchar |  |  | SI | Include all test items on worksheet |
| LBCWSTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCWSTS_ColumnOffset | integer |  |  | SI | Column offset within the worksheet for this test s... |
| LBCWSTS_RowID | varchar |  |  | NO | - |
| LBCWSTS_Sequence | double |  |  | SI | Sequence which test set is displayed on worksheet |
| LBCWSTS_TestSet_DR | bigint |  | FK | SI | TestSet Reference |
| LBCWSTS_TotalColumns | integer |  |  | SI | Number of test set item columns for this test set,... |
| Q01 | - |  |  | SI | Nombre del Paciente |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | Grupo y RH de la Madre |
| Q05 | - |  |  | SI | Apgar 1 Minuto |
| Q06 | - |  |  | SI | Apgar 5 Minutos |
| Q07 | - |  |  | SI | Grupo y Rh del Recien Nacido |
| Q08 | - |  |  | SI | Antecedentes Morbidos de la Madre |
| Q09 | - |  |  | SI | Antecedentes Quirurgicos de la Madre |
| Q10 | - |  |  | SI | Antecedentes Sociales/Habitos de la Madre |
| Q11 | - |  |  | SI | Fecha de Ingreso |
| Q12 | - |  |  | SI | N° Ficha Clinica |
| Q13 | - |  |  | SI | Anamnesis |
| Q14 | - |  |  | SI | Peso Ingreso |
| Q14ObsDR | - |  |  | SI | Peso Ingreso DR |
| Q15 | - |  |  | SI | Peso al Nacer |
| Q15ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q16 | - |  |  | SI | Talla al Nacer |
| Q16ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q17 | - |  |  | SI | Circunferencia Craneana (cm) |
| Q17ObsDR | - |  |  | SI | Circunferencia Craneana (cm) DR |
| Q18 | - |  |  | SI | Antecedentes Morbidos del Hijo |
| Q19 | - |  |  | SI | Ingresa con Billirubinemia de: |
| Q19ObsDR | - |  |  | SI | Ingresa con Billirubinemia de: DR |
| Q20 | - |  |  | SI | Nivel de Foto es: |
| Q20ObsDR | - |  |  | SI | Nivel de Foto es: DR |
| Q21 | - |  |  | SI | Presenta Ictericia desde las: |
| Q22 | - |  |  | SI | Examen Fisico |
| Q23 | - |  |  | SI | Diagnósticos de Ingreso |
| Q24 | - |  |  | SI | Plan |
| Q25 | - |  |  | SI | Profesional de salud |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*