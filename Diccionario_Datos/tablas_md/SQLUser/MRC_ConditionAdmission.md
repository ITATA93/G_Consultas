# SQLUser.MRC_ConditionAdmission

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CADM_RowID | bigint | PK |  | NO | - |
| CADM_Code | varchar |  |  | SI | Code |
| CADM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CADM_CreatedDate | date |  |  | SI | Created Date |
| CADM_CreatedTime | time |  |  | SI | Created Time |
| CADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CADM_DateFrom | date |  |  | SI | Date From |
| CADM_DateTo | date |  |  | SI | Date To |
| CADM_Desc | varchar |  |  | SI | Description |
| CADM_Owner | varchar |  |  | SI | Owner |
| CADM_UpdatedDate | date |  |  | SI | Updated Date |
| CADM_UpdatedTime | time |  |  | SI | Updated Time |
| CADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) |
| Q02 | - |  |  | SI | codigo establecimiento de salud |
| Q03 | - |  |  | SI | Fecha Ejecución |
| Q04 | - |  |  | SI | Hora Inicio |
| Q05 | - |  |  | SI | Hora Término |
| Q06 | - |  |  | SI | Ejecutada por |
| Q07 | - |  |  | SI | N° Sesiones Pacientes, Padre y/o Cuidadores (E) |
| Q08 | - |  |  | SI | Tema |
| Q09 | - |  |  | SI | Tipo de asistentes (02-Tema) |
| Q10 | - |  |  | SI | Tipo de Asistentes (01 y 03-Tema) |
| Q11 | - |  |  | SI | Observaciones de la atención grupal |
| Q13 | - |  |  | SI | Mes |
| Q14 | - |  |  | SI | Año |
| Q15 | - |  |  | SI | N° Participantes Pacientes, Padres y/o Cuidadores ... |
| Q16 | - |  |  | SI | Un Profesional (E) |
| Q17 | - |  |  | SI | N° Sesiones Salas Cunas y Jardines Infantiles (E) |
| Q18 | - |  |  | SI | N° Participantes Salas Cunas y Jardines Infantiles... |
| Q19 | - |  |  | SI | Un Profesional (E) |
| Q20 | - |  |  | SI | N° Sesiones Establecimientos Educacionales (E) |
| Q21 | - |  |  | SI | N° Participantes Establecimientos Educacionales (E... |
| Q22 | - |  |  | SI | N° Sesiones Intersector (E) |
| Q23 | - |  |  | SI | N° Participantes Intersector (E) |
| Q24 | - |  |  | SI | Un Profesional (E) |
| Q25 | - |  |  | SI | N° Sesiones Pacientes y/o Cuidadores (R) |
| Q26 | - |  |  | SI | N° Participantes Pacientes y/o Cuidadores (R) |
| Q27 | - |  |  | SI | Un Profesional (R) |
| Q28 | - |  |  | SI | N° Sesiones Pacientes, Padres y/o Cuidadores (A) |
| Q29 | - |  |  | SI | N° Participantes Pacientes, Pades y/o Cuidadores (... |
| Q30 | - |  |  | SI | Un Profesional (A) |
| Q31 | - |  |  | SI | N° Sesiones Salas Cunas y Jardines Infantiles (A) |
| Q32 | - |  |  | SI | N° Participantes Salas Cunas y Jardines Infantiles... |
| Q33 | - |  |  | SI | Un Profesional (A) |
| Q34 | - |  |  | SI | N° Sesiones Establecimientos Educacionales (A) |
| Q35 | - |  |  | SI | N° Participantes Establecimientos Educacionales (A... |
| Q36 | - |  |  | SI | Un Profesional (A) |
| Q37 | - |  |  | SI | N° Sesiones Intersector (A) |
| Q38 | - |  |  | SI | N° Participantes Intersector (A) |
| Q39 | - |  |  | SI | Un Profesional (A) |
| Q40 | - |  |  | SI | Un Profesional (E) |
| Q41 | - |  |  | SI | Dos o Más Profesionales (E) |
| Q42 | - |  |  | SI | Dos o Más Profesionales (E) |
| Q43 | - |  |  | SI | Dos o Más Profesionales (E) |
| Q44 | - |  |  | SI | Dos o Más Profesionales (R) |
| Q45 | - |  |  | SI | Dos o Más Profesionales (A) |
| Q46 | - |  |  | SI | Dos o Más Profesionales (A) |
| Q47 | - |  |  | SI | Dos o Más Profesionales (A) |
| Q48 | - |  |  | SI | Dos o Más Profesionales (A) |
| Q49 | - |  |  | SI | Dos o Más Profesionales (E) |
| QHR | - |  |  | SI | Establecimiento |
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