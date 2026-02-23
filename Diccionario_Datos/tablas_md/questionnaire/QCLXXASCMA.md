# questionnaire.QCLXXASCMA

> Aspectos Socio-Culturales de la Madre

**Schema:** questionnaire
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Aspectos Socio-Culturales de la Madre

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q103 | varchar |  |  | SI | Otra Religión |
| Q220 | varchar |  |  | SI | Profesional de Salud |
| Q25 | varchar |  |  | SI | Religión |
| Q26 | varchar |  |  | SI | Consumo de Alcohol |
| Q27 | varchar |  |  | SI | Tiempo Consumo Alcohol |
| Q28 | varchar |  |  | SI | Tabaquismo |
| Q29 | numeric |  |  | SI | N° Cigarrillos por Día |
| Q30 | numeric |  |  | SI | N° de años de Consumo |
| Q31 | varchar |  |  | SI | Paquete Cigarrillos/Año |
| Q32 | varchar |  |  | SI | Consumo de Droga |
| Q33 | varchar |  |  | SI | Otra Droga |
| Q34 | varchar |  |  | SI | Tiempo de Consumo Drogas |
| Q35 | varchar |  |  | SI | Discapacidad Física/Cognitiva (Vulnerabilidad) |
| Q36 | varchar |  |  | SI | Nivel de Dependencia |
| Q37 | varchar |  |  | SI | Nivel Educacional |
| Q38 | varchar |  |  | SI | Forma  de Comunicación |
| Q39 | varchar |  |  | SI | Otra Forma de Comunicación |
| Q40 | varchar |  |  | SI | Necesita Intérprete |
| Q41 | varchar |  |  | SI | Comentario Necesita Intérprete |
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