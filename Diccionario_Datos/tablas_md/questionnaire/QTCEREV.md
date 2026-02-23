# questionnaire.QTCEREV

> Raquídea Epidural Combinada

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Raquídea Epidural Combinada

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Técnica |
| Q02 | varchar |  |  | SI | Trocar |
| Q03 | varchar |  |  | SI | Nivel Metámera |
| Q04 | varchar |  |  | SI | Abordaje |
| Q05 | varchar |  |  | SI | Infiltración Local |
| Q06 | varchar |  |  | SI | Descripción |
| Q07 | varchar |  |  | SI | Observaciones |
| Q08 | varchar |  |  | SI | Número |
| Q09 | varchar |  |  | SI | ANANO |
| Q10 | varchar |  |  | SI | Posición Anestésica |
| Q11 | varchar |  |  | SI | Parestesis |
| Q12 | varchar |  |  | SI | Descripción |
| Q13 | varchar |  |  | SI | Posición Pcte. Inicio Anestesia |
| Q14 | varchar |  |  | SI | Descripción del Procedimiento  |
| Q15 | varchar |  |  | SI | Técnica |
| Q16 | bit |  |  | SI | Espinal punta lápiz  |
| Q17 | numeric |  |  | SI | N° Espinal Punta lápiz   |
| Q18 | bit |  |  | SI | Tuohy   |
| Q19 | numeric |  |  | SI | N° Tuohy  |
| Q20 | bit |  |  | SI | Otro |
| Q21 | varchar |  |  | SI | Texto libre Otro   |
| Q22 | numeric |  |  | SI | Número Catéter  |
| Q23 | varchar |  |  | SI | Direccción  |
| Q24 | numeric |  |  | SI | Introducción |
| Q25 | varchar |  |  | SI | Sitio Punción   |
| Q26 | varchar |  |  | SI | Registro Aspiración Líquido Céfalo Raquídeo |
| Q27 | varchar |  |  | SI | Registro Aspiración de sangre  |
| Q28 | varchar |  |  | SI | Drogas se administran por: |
| Q29 | varchar |  |  | SI | Abordaje |
| Q30 | varchar |  |  | SI | Infiltración Local |
| Q31 | date |  |  | SI | Fecha Adm Analgesia |
| Q32 | time |  |  | SI | Hora Adm Analgesia |
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