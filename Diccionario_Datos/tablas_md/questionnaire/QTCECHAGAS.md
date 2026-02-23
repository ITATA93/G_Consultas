# questionnaire.QTCECHAGAS

> Formulario para confirmación serológica Enfermedad de Chagas (Trypanosoma cruzi) Laboratorios Clínicos y Bancos de Sangre

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario para confirmación serológica Enfermedad de Chagas (Trypanosoma cruzi) Laboratorios Clínicos y Bancos de Sangre

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Muestra de  |
| Q02 | date |  |  | SI | Fecha Envío |
| Q03 | numeric |  |  | SI | N° de Ficha |
| Q04 | numeric |  |  | SI | N° de Bolsa |
| Q05 | varchar |  |  | SI | Apellido Paterno |
| Q06 | varchar |  |  | SI | Apellido Materno |
| Q07 | varchar |  |  | SI | Nombre del Paciente |
| Q08 | varchar |  |  | SI | RUT |
| Q09 | varchar |  |  | SI | Fecha de Nacimiento |
| Q10 | varchar |  |  | SI | Sexo |
| Q11 | varchar |  |  | SI | Teléfono |
| Q12 | varchar |  |  | SI | Dirección |
| Q13 | varchar |  |  | SI | Profesional Responsable |
| Q14 | varchar |  |  | SI | Establecimiento |
| Q15 | varchar |  |  | SI | Dirección |
| Q16 | varchar |  |  | SI | Ciudad |
| Q17 | numeric |  |  | SI | Fax |
| Q18 | numeric |  |  | SI | Teléfono |
| Q19 | varchar |  |  | SI | Servicio |
| Q20 | varchar |  |  | SI | Mail |
| Q21 | varchar |  |  | SI | Tipo de Muestra |
| Q22 | date |  |  | SI | Fecha Obtención  |
| Q23 | time |  |  | SI | Hora Obtención |
| Q24 | varchar |  |  | SI | Previsión |
| Q25 | varchar |  |  | SI | Técnica Realizada |
| Q27 | varchar |  |  | SI | Otra (indique) |
| Q28 | varchar |  |  | SI | Lectura |
| Q29 | varchar |  |  | SI | Punto Corte |
| Q31 | varchar |  |  | SI | Lote |
| Q32 | varchar |  |  | SI | Antecedentes Clínicos/Epidemiológicos |
| Q33 | date |  |  | SI | Fecha Envío |
| Q34 | varchar |  |  | SI | Resultado |
| Q35 | varchar |  |  | SI | Marca Comercial |
| Q36 | varchar |  |  | SI | Edad |
| Q37 | varchar |  |  | SI | Tipo de Muestra |
| Q38 | varchar |  |  | SI | Técnica Realizada |
| Q39 | varchar |  |  | SI | Resultado |
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