# questionnaire.QCLXXHABDEP

> Hábitos y Dependencias

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hábitos y Dependencias

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q107 | varchar |  |  | SI | Nombre Madre |
| Q108 | varchar |  |  | SI | Nombre Padre |
| Q109 | varchar |  |  | SI | Uso de  Tuto |
| Q110 | varchar |  |  | SI | Comentario uso de Tuto |
| Q111 | varchar |  |  | SI | Uso de Chupete |
| Q112 | varchar |  |  | SI | Comentario uso de Chupete |
| Q113 | varchar |  |  | SI | Uso de Mamaderas |
| Q114 | varchar |  |  | SI | Comentario uso de Mamaderas |
| Q115 | varchar |  |  | SI | Uso de Pañal |
| Q116 | varchar |  |  | SI | Comentario uso de Pañal |
| Q117 | varchar |  |  | SI | Alimentación |
| Q118 | varchar |  |  | SI | Higiene |
| Q119 | varchar |  |  | SI | Vestuario |
| Q120 | varchar |  |  | SI | Deambulación |
| Q121 | varchar |  |  | SI | Movilización |
| Q122 | varchar |  |  | SI | Comunicación |
| Q1221 | varchar |  |  | SI | Eliminación |
| Q123 | varchar |  |  | SI | Comentario Alimentación |
| Q124 | varchar |  |  | SI | Comentario Higiene |
| Q125 | varchar |  |  | SI | Comentario Vestuario |
| Q126 | varchar |  |  | SI | Comentario Deambulación |
| Q127 | varchar |  |  | SI | Comentario Movilización |
| Q128 | varchar |  |  | SI | Comentario Comunicación |
| Q1281 | varchar |  |  | SI | Comentario Eliminación |
| Q170 | varchar |  |  | SI | Profesional de Salud |
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