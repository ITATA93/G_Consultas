# questionnaire.QTCEEVKINR

> Evaluación Kinésica RBC

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Kinésica RBC

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Postura |
| Q02 | varchar |  |  | SI | Alineación |
| Q03 | varchar |  |  | SI | Plano Sagital |
| Q04 | varchar |  |  | SI | Plano Frontal |
| Q05 | varchar |  |  | SI | Plano Transversal |
| Q06 | varchar |  |  | SI | Base de Apoyo  |
| Q07 | varchar |  |  | SI | Reacciones de Equilibrio |
| Q08 | varchar |  |  | SI | Reacciones de Enderezamiento |
| Q09 | varchar |  |  | SI | Transferencias |
| Q10 | varchar |  |  | SI | Giros Decúbitos |
| Q11 | varchar |  |  | SI | Sedestación |
| Q12 | varchar |  |  | SI | Cuatro Apoyos |
| Q13 | varchar |  |  | SI | Bipedestación |
| Q14 | varchar |  |  | SI | Marcha |
| Q15 | varchar |  |  | SI | Pruebas Especiales |
| Q16 | varchar |  |  | SI | Apreciación Diagnósticas Kinésicas |
| Q17 | varchar |  |  | SI | postura obs |
| Q18 | varchar |  |  | SI | Alineación obs |
| Q19 | varchar |  |  | SI | Plano Sagital obs |
| Q20 | varchar |  |  | SI | Plano Frontal obs |
| Q21 | varchar |  |  | SI | Plano Transversal obs |
| Q22 | varchar |  |  | SI | Base de Apoyo obs |
| Q23 | varchar |  |  | SI | Reacciones de Equilibrio obs |
| Q24 | varchar |  |  | SI | Reacciones de Enderezamiento obs |
| Q25 | varchar |  |  | SI | Transferencias obs |
| Q26 | varchar |  |  | SI | Giros Decúbitos obs |
| Q27 | varchar |  |  | SI | Sedentación obs |
| Q28 | varchar |  |  | SI | Cuatro Apoyos obs |
| Q29 | varchar |  |  | SI | Bipedestación obs |
| Q30 | varchar |  |  | SI | Marcha obs |
| Q31 | bit |  |  | SI | Evaluación Intermedia |
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