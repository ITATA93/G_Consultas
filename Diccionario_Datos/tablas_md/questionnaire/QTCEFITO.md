# questionnaire.QTCEFITO

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Escolaridad |
| Q02 | varchar | PK |  | SI | Situacion laboral |
| Q03 | varchar | PK |  | SI | Fecha de evaluacion |
| Q04 | varchar | PK |  | SI | Diagnóstico |
| Q05 | varchar | PK |  | SI | Diagnóstico secundario |
| Q06 | varchar | PK |  | SI | Resumen historia de vida |
| Q07 | varchar | PK |  | SI | ¿Para qué cosas soy bueno? |
| Q08 | varchar | PK |  | SI | ¿Qué cosas son importantes para mi? |
| Q09 | varchar | PK |  | SI | ¿Que cosas disfruto hacer? |
| Q19 | varchar | PK |  | SI | Esta rutina,¿es satisfactoria para mi? |
| Q1a | varchar | PK |  | SI | Hora |
| Q1b | varchar | PK |  | SI | Actividad |
| Q1c | varchar | PK |  | SI | Actividad |
| Q20 | varchar | PK |  | SI | Hábitos dominantes |
| Q21 | varchar | PK |  | SI | Hábitos útiles |
| Q22 | varchar | PK |  | SI | Hábitos empobrecidos |
| Q23 | varchar | PK |  | SI | ¿Con qué papeles desempeño en la vida? |
| Q24 | varchar | PK |  | SI | ¿Mis habilidades motoras facilitan mi desempeño? |
| Q25 | varchar | PK |  | SI | ¿Mis habilidades de Procesamiento facilitan mi des... |
| Q26 | varchar | PK |  | SI | ¿Mis habilidades de comunicacion e intreracción fa... |
| Q27 | varchar | PK |  | SI | ¿Como es el hambiente donde me desempeño? |
| Q28 | varchar | PK |  | SI | ¿Como son las personas con las que me relaciono? |
| Q29 | varchar | PK |  | SI | Nivel de función |
| Q2a | varchar | PK |  | SI | hora |
| Q2b | varchar | PK |  | SI | Actividad |
| Q2c | varchar | PK |  | SI | Actividad |
| Q30 | varchar | PK |  | SI | Objetivo General |
| Q31 | varchar | PK |  | SI | Objetivos especificos |
| Q32 | varchar | PK |  | SI | Actividades |
| Q33 | varchar | PK |  | SI | Nombre evaluador |
| Q3a | varchar | PK |  | SI | Hora |
| Q3b | varchar | PK |  | SI | Actividad |
| Q3c | varchar | PK |  | SI | Actividad |
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