# questionnaire.QCLXXT5PAL

> Test de 5 Palabras

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de 5 Palabras

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Responsable |
| Q04 | varchar |  |  | SI | Consigna: Lea estas palabras en voz alta e intente... |
| Q05 | varchar |  |  | SI | Lectura 5 palabras |
| Q06 | varchar |  |  | SI | Total lectura 5 palabras |
| Q07 | varchar |  |  | SI | Consigna: Puede ahora, mirándo la hoja, decirme ¿c... |
| Q08 | varchar |  |  | SI | Identificación 5 palabras |
| Q09 | varchar |  |  | SI | Total identificación 5 palabras |
| Q10 | varchar |  |  | SI | Recuerdo libre inmediato 5 palabras |
| Q11 | varchar |  |  | SI | Total Recuerdo libre inmediato 5 palabras |
| Q12 | varchar |  |  | SI | Intrusiones recuerdo libre inmedito |
| Q13 | numeric |  |  | SI | Total Intrusiones recuerdo libre  inmedito |
| Q14 | varchar |  |  | SI | Consigna: ¿Cuál era la flor?; ¿Cuál era la fruta?;... |
| Q15 | varchar |  |  | SI | Recuerdo con Clave Inmediato |
| Q16 | varchar |  |  | SI | Intrusiones recuerdo con Clave Inmedito |
| Q17 | numeric |  |  | SI | Intrusiones Recuerdo con Clave  Inmedito |
| Q18 | varchar |  |  | SI | Total Recuerdo inmediato con clave |
| Q19 | varchar |  |  | SI | Total Intrusiones Recuerdo Inmediato |
| Q20 | varchar |  |  | SI | Número de ensayos necesarios para aprender las 5 p... |
| Q21 | varchar |  |  | SI | Consigna: Dígame todas las palabras que recuerde |
| Q22 | varchar |  |  | SI | Recuerdo diferido libre 5 palabras |
| Q23 | varchar |  |  | SI | Recuerdo diferido libre 5 palabras |
| Q24 | varchar |  |  | SI | Intrusiones recuerdo diferido libre |
| Q25 | numeric |  |  | SI | Intrusiones recuerdo diferido libre |
| Q26 | varchar |  |  | SI | Consigna: ¿Cuál era la flor?; ¿Cuál era la fruta?;... |
| Q27 | varchar |  |  | SI | Recuerdo diferido con clave 5 palabras |
| Q28 | varchar |  |  | SI | Intrusiones recuerdo diferido con clave |
| Q29 | numeric |  |  | SI | Intrusiones recuerdo diferido con clave |
| Q30 | varchar |  |  | SI | Total intrusiones recuerdo diferido |
| Q31 | varchar |  |  | SI | Total recuerdo diferido con clave 5 palabras |
| Q32 | varchar |  |  | SI | Puntaje total recuerdo inmediato |
| Q33 | varchar |  |  | SI | Puntaje total recuerdo diferido |
| Q34 | varchar |  |  | SI | Puntaje total 5 palabras |
| Q35 | varchar |  |  | SI | Puntaje total Intrusiones |
| Q36 | varchar |  |  | SI | Observaciones |
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