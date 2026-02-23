# questionnaire.QCLXXETUCI

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date | PK |  | SI | Fecha de Entrega |
| Q02 | time | PK |  | SI | Hora de Entrega |
| Q03 | varchar | PK |  | SI | Nombre del Profesional que entrega |
| Q04 | varchar | PK |  | SI | Nombre del Profesional que recibe |
| Q05 | numeric | PK |  | SI | Número de días hospitalizado |
| Q06 | numeric | PK |  | SI | Número de días en la unidad |
| Q07 | varchar | PK |  | SI | Médico Tratante |
| Q08 | varchar | PK |  | SI | Alta Programada |
| Q09 | date | PK |  | SI | Fecha probable de Alta |
| Q10 | varchar | PK |  | SI | Condición del Paciente |
| Q11 | varchar | PK |  | SI | Estado de Salud  |
| Q12 | varchar | PK |  | SI | Aislamiento |
| Q13 | varchar | PK |  | SI | Alimentación |
| Q14 | varchar | PK |  | SI | Ventilación |
| Q15 | varchar | PK |  | SI | Actividad/Mobilidad |
| Q16 | varchar | PK |  | SI | Evolución General |
| Q17 | varchar | PK |  | SI | Neurológica |
| Q18 | varchar | PK |  | SI | Respiratoria |
| Q19 | varchar | PK |  | SI | Cardiovascular |
| Q20 | varchar | PK |  | SI | Infeccioso |
| Q21 | varchar | PK |  | SI | Gastrointestinal / Metabólico |
| Q22 | varchar | PK |  | SI | Renal / Genito-urinario |
| Q23 | varchar | PK |  | SI | Hematológico |
| Q24 | varchar | PK |  | SI | Músculo-esquelético |
| Q25 | varchar | PK |  | SI | Piel / Tegumentos |
| Q26 | varchar | PK |  | SI | Otros |
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