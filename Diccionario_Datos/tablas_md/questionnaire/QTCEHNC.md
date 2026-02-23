# questionnaire.QTCEHNC

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Conciente |
| Q02 | varchar | PK |  | SI | Orientado |
| Q03 | varchar | PK |  | SI | Físico |
| Q04 | varchar | PK |  | SI | Psíquico |
| Q05 | bit | PK |  | SI | Glasgow |
| Q06 | varchar | PK |  | SI | Sin déficit |
| Q07 | varchar | PK |  | SI | Déficit ligero |
| Q08 | varchar | PK |  | SI | Déficit importante |
| Q09 | bit | PK |  | SI | Ninguno |
| Q10 | varchar | PK |  | SI | Fármacos (todos) y horario últimas dosis |
| Q11 | varchar | PK |  | SI | Lugar de caida |
| Q11a | varchar | PK |  | SI | Dónde |
| Q12 | bit | PK |  | SI | Paso a sillón |
| Q12a | varchar | PK |  | SI | Paso a sillón |
| Q13 | bit | PK |  | SI | Intento de o caminando |
| Q13a | varchar | PK |  | SI | Intento de o caminando |
| Q14 | varchar | PK |  | SI | Otros |
| Q15 | varchar | PK |  | SI | Protección previo al accidente |
| Q16 | varchar | PK |  | SI | Persona que encuentra al paciente |
| Q16a | varchar | PK |  | SI | Quien |
| Q17 | varchar | PK |  | SI | Breve descripción de lo que pasó y/ocómo lo encont... |
| Q18 | varchar | PK |  | SI | Según condición del paciente, ¿Qué pasó? (con sus ... |
| Q19 | varchar | PK |  | SI | Se avisa a Dr. |
| Q19a | varchar | PK |  | SI | A las |
| Q19b | varchar | PK |  | SI | Responde a las |
| Q20 | varchar | PK |  | SI | Se avisa a Enfermera |
| Q20a | varchar | PK |  | SI | A las |
| Q20b | varchar | PK |  | SI | Responde a las |
| Q21 | varchar | PK |  | SI | Se solicitan RX |
| Q21a | varchar | PK |  | SI | Cuáles |
| Q22 | varchar | PK |  | SI | Observaciones |
| Q23 | varchar | PK |  | SI | Se notifica |
| Q24 | varchar | PK |  | SI | Enfermera/o que notifica |
| Q34 | varchar | PK |  | SI | Motivo de Ingreso y DG. |
| Q35 | bit | PK |  | SI | Agitado |
| Q36 | bit | PK |  | SI | Tranquilo |
| Q37 | bit | PK |  | SI | Independiente |
| Q38 | bit | PK |  | SI | Precisa ayuda para movilizarse |
| Q39 | bit | PK |  | SI | Postrado |
| Q40 | varchar | PK |  | SI | Actividad que realizaba |
| Q41 | varchar | PK |  | SI | Visual |
| Q42 | varchar | PK |  | SI | Auditivo |
| Q43 | varchar | PK |  | SI | Luga de Caída |
| Q44 | varchar | PK |  | SI | Auditivo |
| Q45 | varchar | PK |  | SI | Visual |
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