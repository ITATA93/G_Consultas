# SQLUser.LB_TestSetSpecialHandling

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSSH_ParRef | bigint | PK |  | NO | - |
| LBTSSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBTSSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBTSSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBTSSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBTSSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBTSSH_RowID | varchar |  |  | NO | - |
| LBTSSH_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| Q01 | - |  |  | SI | Establecimiento de Salud (código y descripción) El... |
| Q02 | - |  |  | SI | Código establecimiento de salud |
| Q03 | - |  |  | SI | Mes de Atención |
| Q04 | - |  |  | SI | Año de Atención |
| Q05 | - |  |  | SI | Horas Odontológicas Mensuales Contratadas Eliminad... |
| Q05B | - |  |  | SI | Horas Odontológicas Mensuales Contratadas |
| Q06 | - |  |  | SI | Horas disponibles Atención Clínica (horas) |
| Q07 | - |  |  | SI | n° citas agendadas atencion morbilidad |
| Q08 | - |  |  | SI | n° citas agendadas atencion tratamiento |
| Q09 | - |  |  | SI | n° citas agendadas atencion urgencia |
| Q10 | - |  |  | SI | n° citas efectivas atencion morbilidad |
| Q11 | - |  |  | SI | n° citas efectivas atencion tratamiento |
| Q12 | - |  |  | SI | n° citas efectivas atencion  urgencia |
| QHR | - |  |  | SI | Establecimiento de Salud |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*