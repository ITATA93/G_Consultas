# questionnaire.QCLXXRVHD

> Registro Visita Hospitalización Domiciliaria

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Visita Hospitalización Domiciliaria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. ANTECEDENTES DEL PACIENTE |
| Q02 | varchar |  |  | SI | Nombre del Paciente |
| Q03 | varchar |  |  | SI | Edad del Paciente |
| Q04 | varchar |  |  | SI | N° Ficha Clínica |
| Q05 | varchar |  |  | SI | Domicilio del Paciente |
| Q06 | varchar |  |  | SI | Número Domicilio |
| Q07 | varchar |  |  | SI | RUN |
| Q08 | varchar |  |  | SI | Diagnóstico |
| Q09 | varchar |  |  | SI | Servicio de Origen del Paciente |
| Q10 | date |  |  | SI | Fecha Ingreso Programa H.D. |
| Q11 | varchar |  |  | SI | Evaluación Paciente o Cuidador al Egreso Hospitala... |
| Q12 | varchar |  |  | SI | Funcionarios Requeridos en la Visita al Paciente |
| Q13 | varchar |  |  | SI | 2. ANTECEDENTES CUIDADOR Y FAMILIARES |
| Q14 | varchar |  |  | SI | Nombre Cuidador |
| Q15 | varchar |  |  | SI | Parentesco Cuidador |
| Q16 | varchar |  |  | SI | Teléfono Cuidador |
| Q17 | numeric |  |  | SI | N° Integrante |
| Q18 | varchar |  |  | SI | Detalle |
| Q19 | varchar |  |  | SI | Otros Funcionarios |
| Q20 | varchar |  |  | SI | 3. FECHA DE TERMINO HOSPITALIZACIÓN DOMICILIARIA |
| Q21 | numeric |  |  | SI | Días de Estada en Programa H.D. |
| Q22 | varchar |  |  | SI | Contrareferencia con la Red de salud |
| Q23 | varchar |  |  | SI | Evaluación Paciente o Cuidador al Egreso H.D. |
| Q24 | varchar |  |  | SI | Apellido Paterno |
| Q25 | varchar |  |  | SI | Apellido Materno |
| Q26 | varchar |  |  | SI | Satifacción Usuario con Programa H.D. |
| Q27 | varchar |  |  | SI | Nombre de los Profesionales |
| Q28 | varchar |  |  | SI | Indicación de Nutrición Enteral Domiciliaria (NED) |
| Q29 | varchar |  |  | SI | 4. REM P3 Sección A |
| Q31 | varchar |  |  | SI | Tipo de Cupos Asignado |
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