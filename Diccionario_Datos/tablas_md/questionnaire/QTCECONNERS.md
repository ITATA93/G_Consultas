# questionnaire.QTCECONNERS

> Test de Conners para Profesores

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Conners para Profesores

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Inquieto, demasiado activo |
| Q02 | varchar |  |  | SI | Excitable, Impulsivo |
| Q03 | varchar |  |  | SI | Molesta a otros niños |
| Q04 | varchar |  |  | SI | No termina lo que comienza |
| Q05 | varchar |  |  | SI | Se mueve constantemente |
| Q06 | varchar |  |  | SI | Se distrae con facilidad |
| Q07 | varchar |  |  | SI | Hay que satisfacerle de inmediato; no tolera la fr... |
| Q08 | varchar |  |  | SI | Llora con facilidad |
| Q09 | varchar |  |  | SI | Cambia de humor bruscamente |
| Q10 | varchar |  |  | SI | Pataletas; conducta explosiva |
| Q11 | varchar |  |  | SI | RESPECTO A SU APRENDIZAJE |
| Q12 | varchar |  |  | SI | ¿Su lectura es poco fluida o silabeante? |
| Q13 | varchar |  |  | SI | ¿Le cuesta comprender lo que ha leído? |
| Q14 | varchar |  |  | SI | ¿Le cuesta escribir al dictado? |
| Q15 | varchar |  |  | SI | ¿Tiene dificultades para copiar a tiempo lo leído ... |
| Q16 | varchar |  |  | SI | ¿Comete muchas faltas de ortografía? |
| Q17 | varchar |  |  | SI | ¿Le cuesta demasiado el cálculo matemático? |
| Q18 | varchar |  |  | SI | POR FAVOR INDÍQUENOS |
| Q19 | varchar |  |  | SI | ¿Recibe medicación en la escuela? |
| Q20 | varchar |  |  | SI | ¿Ha notado mejoría en conducta? |
| Q21 | varchar |  |  | SI | PONGA NOTA DE 1 A 7 |
| Q22 | varchar |  |  | SI | A su conducta |
| Q23 | varchar |  |  | SI | A su rendimiento |
| Q24 | varchar |  |  | SI | A la relación con sus profesores |
| Q25 | varchar |  |  | SI | A la relación con sus compañeros |
| Q26 | varchar |  |  | SI | Resultado Test de Conners |
| Q26ObsDR | varchar |  | FK | SI | Resultado Test de Conners DR |
| Q27 | varchar |  |  | SI | Nivel Educacional |
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