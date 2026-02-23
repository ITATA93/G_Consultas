# questionnaire.QTCEMCAV

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | RUT |
| Q02 | varchar | PK |  | SI | Nombre |
| Q03 | varchar | PK |  | SI | Apellido Paterno |
| Q04 | varchar | PK |  | SI | Apellido Materno |
| Q05 | varchar | PK |  | SI | Sexo |
| Q06 | varchar | PK |  | SI | Fecha Nacimiento |
| Q07 | varchar | PK |  | SI | Edad |
| Q08 | varchar | PK |  | SI | Dirección |
| Q09 | varchar | PK |  | SI | Región |
| Q10 | varchar | PK |  | SI | Ciudad / Localidad |
| Q11 | varchar | PK |  | SI | Comuna |
| Q12 | varchar | PK |  | SI | Teléfono |
| Q13 | varchar | PK |  | SI | Previsión |
| Q14 | varchar | PK |  | SI | Profesional Responsable |
| Q15 | varchar | PK |  | SI | Región |
| Q16 | varchar | PK |  | SI | Provincia |
| Q17 | varchar | PK |  | SI | Comuna |
| Q18 | varchar | PK |  | SI | Dirección |
| Q19 | varchar | PK |  | SI | Laboratorio / Hospital |
| Q20 | varchar | PK |  | SI | Unidad |
| Q21 | varchar | PK |  | SI | Correo Electrónico |
| Q22 | varchar | PK |  | SI | Teléfono |
| Q23 | varchar | PK |  | SI | Fax |
| Q24 | date | PK |  | SI | Fecha Obtención de la Muestra |
| Q25 | time | PK |  | SI | Hora de Obtención |
| Q26 | varchar | PK |  | SI | Exámen |
| Q27 | varchar | PK |  | SI | Otro (Especificar) |
| Q28 | varchar | PK |  | SI | Antecedentes Clínicos / Epidemiologicos del Pacien... |
| Q29 | varchar | PK |  | SI | Otro(especificar) |
| Q30 | varchar | PK |  | SI | Presentación |
| Q31 | varchar | PK |  | SI | Enfermedad Asociada |
| Q32 | varchar | PK |  | SI | Diagnóstico |
| Q33 | varchar | PK |  | SI | Sintomatologia |
| Q34 | varchar | PK |  | SI | Tiempo de Evolución |
| Q35 | date | PK |  | SI | Fecha de Contacto |
| Q36 | varchar | PK |  | SI | Embarazo |
| Q37 | date | PK |  | SI | Fecha de Inicio de Sintomas |
| Q38 | varchar | PK |  | SI | N° Semanas (Embarazo) |
| Q39 | varchar | PK |  | SI | Muestra |
| Q40 | varchar | PK |  | SI | Otro |
| Q41 | varchar | PK |  | SI | N° de Muestra:  |
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