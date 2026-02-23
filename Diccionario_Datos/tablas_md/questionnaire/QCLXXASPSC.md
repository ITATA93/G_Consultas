# questionnaire.QCLXXASPSC

> Aspectos Socio-Culturales

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Aspectos Socio-Culturales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q27 | varchar |  |  | SI | Consumo Alcohol |
| Q28 | varchar |  |  | SI | Tiempo Consumo Alcohol |
| Q29 | varchar |  |  | SI | Tabaquismo |
| Q30 | numeric |  |  | SI | N° Cigarrillos por día |
| Q31 | numeric |  |  | SI | N° Años de Consumo |
| Q32 | varchar |  |  | SI | Paquete Cigarrillos |
| Q33 | varchar |  |  | SI | Consumo de Drogas |
| Q34 | varchar |  |  | SI | Otra Droga |
| Q35 | varchar |  |  | SI | Tiempo Consumo Drogas |
| Q36 | varchar |  |  | SI | Nivel Educacional  |
| Q37 | varchar |  |  | SI | Discapacidad Física / Cognitiva (Vulnerabilidad) |
| Q38 | varchar |  |  | SI | Otra Vulnerabilidad |
| Q39 | varchar |  |  | SI | Nivel de Dependencia |
| Q40 | varchar |  |  | SI | Forma de Comunicación |
| Q41 | varchar |  |  | SI | Otra Forma de comunicación |
| Q42 | varchar |  |  | SI | Necesita Intérprete |
| Q43 | varchar |  |  | SI | Comentarios |
| Q44 | varchar |  |  | SI | Religión |
| Q45 | varchar |  |  | SI | Otra Religión |
| Q46 | varchar |  |  | SI | Aspectos Socio-Culturales relevantes Progenitor Ma... |
| Q47 | varchar |  |  | SI | Profesional de Salud |
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