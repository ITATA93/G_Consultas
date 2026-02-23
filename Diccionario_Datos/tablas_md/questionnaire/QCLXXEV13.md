# questionnaire.QCLXXEV13

> Encuesta VES 13

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta VES 13

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Edad |
| Q02 | varchar |  |  | SI | Autopercepción del estado de salud |
| Q03 | varchar |  |  | SI | Actividades básicas e instrumentales de la vida di... |
| Q04 | varchar |  |  | SI | ¿Necesita ayuda para? |
| Q05 | varchar |  |  | SI | Ir de compras |
| Q06 | varchar |  |  | SI | Utilizar dinero |
| Q07 | varchar |  |  | SI | Realizar trabajos ligeros en casa |
| Q08 | varchar |  |  | SI | Trasportarse |
| Q09 | varchar |  |  | SI | Bañarse |
| Q10 | varchar |  |  | SI | Actividades Adicionales |
| Q11 | varchar |  |  | SI | ¿Necesita ayuda para? |
| Q12 | varchar |  |  | SI | Agacharse, ponerse en cuclillas o de rodillas |
| Q13 | varchar |  |  | SI | Levantar o cargar un objeto de 10 libras |
| Q14 | varchar |  |  | SI | Escribir o manipular objetos pequeños |
| Q15 | varchar |  |  | SI | Extender los brazos encima del hombro |
| Q16 | varchar |  |  | SI | Caminar 500 metros |
| Q17 | varchar |  |  | SI | Realizar trabajos pesados en casa |
| Q18 | varchar |  |  | SI | Riesgo de deterioro funcional o muerte (a 2 años d... |
| Q19 | varchar |  |  | SI | 0-2 |
| Q20 | varchar |  |  | SI | 3+ |
| Q21 | varchar |  |  | SI | Puntaje de Vulnerabilidad |
| Q22 | varchar |  |  | SI | 11,8 - 14,8% |
| Q23 | varchar |  |  | SI | 49,8 - 54,9% |
| Q24 | varchar |  |  | SI | Paciente No Vulnerable |
| Q25 | varchar |  |  | SI | Paciente Vulnerable |
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