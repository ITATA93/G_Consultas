# questionnaire.QREMA27J

> Servicios de la Red del Programa Más Adultos Mayores Autovalentes

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Servicios de la Red del Programa Más Adultos Mayores Autovalentes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Mes |
| Q02 | numeric |  |  | SI | Año |
| Q03 | numeric |  |  | SI | N° Total de Servicios |
| Q04 | numeric |  |  | SI | Unidad Municipal de Personas Mayores |
| Q05 | numeric |  |  | SI | Unidad Municipal de Atención Social |
| Q06 | numeric |  |  | SI | Unidad Municipal de Deportes |
| Q07 | numeric |  |  | SI | Unidad Municipal Turismo |
| Q08 | numeric |  |  | SI | Unidad Municipal Educación |
| Q09 | numeric |  |  | SI | Biblioteca Municipal |
| Q10 | numeric |  |  | SI | Unidad Cultura Municipal |
| Q11 | numeric |  |  | SI | Otras Unidades Municipales |
| Q12 | numeric |  |  | SI | Escuelas o Colegios |
| Q13 | numeric |  |  | SI | Universidades |
| Q14 | numeric |  |  | SI | Otras Unidades Externas al Municipio |
| Q15 | numeric |  |  | SI | N° Total de Servicios |
| Q16 | numeric |  |  | SI | Unidad Municipal de Personas Mayores |
| Q17 | numeric |  |  | SI | Unidad Municipal de Atención Social |
| Q18 | numeric |  |  | SI | Unidad Municipal de Deportes |
| Q19 | numeric |  |  | SI | Unidad Municipal Turismo |
| Q20 | numeric |  |  | SI | Unidad Municipal Educación |
| Q21 | numeric |  |  | SI | Biblioteca Municipal |
| Q22 | numeric |  |  | SI | Unidad Cultura Municipal |
| Q23 | numeric |  |  | SI | Otras Unidades Municipales |
| Q24 | numeric |  |  | SI | Escuelas o Colegios |
| Q25 | numeric |  |  | SI | Universidades |
| Q26 | numeric |  |  | SI | Otras Unidades Externas al Municipio |
| QHR | varchar |  |  | SI | Establecimiento |
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