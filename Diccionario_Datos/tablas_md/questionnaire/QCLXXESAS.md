# questionnaire.QCLXXESAS

> Evaluación de Síntomas de Edmonton (ESAS-M)

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Síntomas de Edmonton (ESAS-M)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nada de Dolor |
| Q02 | varchar |  |  | SI | Nada Agotado (Cansancio, Debelidad) |
| Q03 | varchar |  |  | SI | Nada Somnoliento (Adormilado) |
| Q04 | varchar |  |  | SI | Sin Náuseas |
| Q05 | varchar |  |  | SI | Ninguna Pérdida de Apetito |
| Q06 | varchar |  |  | SI | Ninguna dificultad para Respirar |
| Q07 | varchar |  |  | SI | Nada Desanimado |
| Q08 | varchar |  |  | SI | Nada Nervioso (Intranquilidad, Ansiedad) |
| Q09 | varchar |  |  | SI | Duermo Perfectamente |
| Q10 | varchar |  |  | SI | Sentirse Perfectamente (Sensación de Bienestar) |
| Q11 | varchar |  |  | SI | Descripción del problema |
| Q12 | varchar |  |  | SI | Otro Problema |
| Q14 | varchar |  |  | SI | El peor dolor que se pueda imaginar |
| Q16 | varchar |  |  | SI | Lo más agotado que se puede imaginar |
| Q18 | varchar |  |  | SI | Lo más somnoliento que se pueda imaginar |
| Q20 | varchar |  |  | SI | Las peores náuseas que se pueda imaginar |
| Q22 | varchar |  |  | SI | La peor apetito que se pueda imaginar |
| Q24 | varchar |  |  | SI | La mayor dificultad para respirar que se pueda ima... |
| Q26 | varchar |  |  | SI | El más desanimado que se pueda imaginar |
| Q28 | varchar |  |  | SI | Lo más nervioso que se pueda imaginar |
| Q30 | varchar |  |  | SI | La mayor dificulta para dormir que se pueda imagin... |
| Q31 | varchar |  |  | SI | Sentirse lo peor que se pueda imaginar |
| Q32 | varchar |  |  | SI | Lo peor posible |
| Q33 | varchar |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q34 | varchar |  |  | SI | Cada puntuación representa la gravedad del síntoma... |
| Q35 | varchar |  |  | SI | El Sistema de Evaluación de Síntomas de Edmonton (... |
| Q36 | varchar |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q47 | varchar |  |  | SI | Clasificación |
| Q49 | varchar |  |  | SI | Gravedad del problema |
| Q59 | date |  |  | SI | Fecha Evaluación |
| Q60 | time |  |  | SI | Hora Evaluación |
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