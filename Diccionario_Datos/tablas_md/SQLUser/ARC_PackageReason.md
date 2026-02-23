# SQLUser.ARC_PackageReason

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACKREA_RowId | bigint | PK |  | NO | - |
| PACKREA_Code | varchar |  |  | NO | Code |
| PACKREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACKREA_CreatedDate | date |  |  | SI | Created Date |
| PACKREA_CreatedTime | time |  |  | SI | Created Time |
| PACKREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACKREA_DateFrom | date |  |  | SI | Date From |
| PACKREA_DateTo | date |  |  | SI | Date To |
| PACKREA_Desc | varchar |  |  | NO | Description |
| PACKREA_Owner | varchar |  |  | SI | Owner |
| PACKREA_UpdatedDate | date |  |  | SI | Updated Date |
| PACKREA_UpdatedTime | time |  |  | SI | Updated Time |
| PACKREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad |
| Q02 | - |  |  | SI | Autopercepción del estado de salud |
| Q03 | - |  |  | SI | Actividades básicas e instrumentales de la vida di... |
| Q04 | - |  |  | SI | ¿Necesita ayuda para? |
| Q05 | - |  |  | SI | Ir de compras |
| Q06 | - |  |  | SI | Utilizar dinero |
| Q07 | - |  |  | SI | Realizar trabajos ligeros en casa |
| Q08 | - |  |  | SI | Trasportarse |
| Q09 | - |  |  | SI | Bañarse |
| Q10 | - |  |  | SI | Actividades Adicionales |
| Q11 | - |  |  | SI | ¿Necesita ayuda para? |
| Q12 | - |  |  | SI | Agacharse, ponerse en cuclillas o de rodillas |
| Q13 | - |  |  | SI | Levantar o cargar un objeto de 10 libras |
| Q14 | - |  |  | SI | Escribir o manipular objetos pequeños |
| Q15 | - |  |  | SI | Extender los brazos encima del hombro |
| Q16 | - |  |  | SI | Caminar 500 metros |
| Q17 | - |  |  | SI | Realizar trabajos pesados en casa |
| Q18 | - |  |  | SI | Riesgo de deterioro funcional o muerte (a 2 años d... |
| Q19 | - |  |  | SI | 0-2 |
| Q20 | - |  |  | SI | 3+ |
| Q21 | - |  |  | SI | Puntaje de Vulnerabilidad |
| Q22 | - |  |  | SI | 11,8 - 14,8% |
| Q23 | - |  |  | SI | 49,8 - 54,9% |
| Q24 | - |  |  | SI | Paciente No Vulnerable |
| Q25 | - |  |  | SI | Paciente Vulnerable |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*