# questionnaire.QTCEINVTBC

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Identificación |
| Q02 | varchar | PK |  | SI | Nombre |
| Q03 | varchar | PK |  | SI | Apellido Paterno |
| Q04 | varchar | PK |  | SI | Apellido Materno |
| Q05 | varchar | PK |  | SI | Edad |
| Q06 | varchar | PK |  | SI | Procedencia |
| Q07 | varchar | PK |  | SI | Domicilio |
| Q08 | numeric | PK |  | SI | N° de Ficha |
| Q09 | varchar | PK |  | SI | Muestra |
| Q10 | varchar | PK |  | SI | Especificar |
| Q11 | varchar | PK |  | SI | Antecedentes de Tratamiento |
| Q12 | varchar | PK |  | SI | Examen Diagnóstico |
| Q13 | varchar | PK |  | SI | Examen para Control de Tratamiento Actual |
| Q14 | varchar | PK |  | SI | Con: (Drogas del Tratamiento Actual) |
| Q15 | numeric | PK |  | SI | N° de meses de Tratamiento Actual |
| Q16 | date | PK |  | SI | Fecha Solicitud |
| Q17 | varchar | PK |  | SI | Nombre  |
| Q18 | numeric | PK |  | SI | Cantidad de Solicitudes  |
| Q20 | varchar | PK |  | SI | Abandono |
| Q21 | varchar | PK |  | SI | Mes/Año de Abandono |
| Q22 | varchar | PK |  | SI | ¿Con que Drogas? |
| Q24 | varchar | PK |  | SI | Año de Contacto |
| Q25 | varchar | PK |  | SI | Personal de Salud |
| Q26 | varchar | PK |  | SI | Extranjero |
| Q27 | varchar | PK |  | SI | País |
| Q28 | varchar | PK |  | SI | Coinfeccion Retroviral |
| Q29 | varchar | PK |  | SI | Situación de Calle |
| Q30 | varchar | PK |  | SI | ¿En qué calle y comuna duerme? |
| Q31 | varchar | PK |  | SI | Pertenece a una Población Cerrada |
| Q32 | varchar | PK |  | SI | ¿Cual? |
| Q33 | varchar | PK |  | SI | En control de tratamiento actualmente (CT) |
| Q34 | numeric | PK |  | SI | Numero de meses con tratamiento a la fecha |
| Q35 | varchar | PK |  | SI | ¿Que droga esta usando? |
| Q36 | varchar | PK |  | SI | Resultado de Baciloscopía o Frotis |
| Q37 | varchar | PK |  | SI | Estado Paciente |
| Q38 | varchar | PK |  | SI | Contacto TBC |
| Q39 | varchar | PK |  | SI | Antes Tratado |
| Q40 | varchar | PK |  | SI | Año de Tratamiento |
| Q41 | varchar | PK |  | SI | ¿Con que  Drogas? |
| Q42 | numeric | PK |  | SI | Cultivo Número |
| Q43 | varchar | PK |  | SI | Especificar Drogas tratamiento actual |
| Q44 | varchar | PK |  | SI | Nombre de Usuario |
| Q45 | date | PK |  | SI | Fecha Resultado de laboratorio |
| Q46 | varchar | PK |  | SI | Otros |
| Q47 | varchar | PK |  | SI | Virgen al Tratamiento (VT) |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*