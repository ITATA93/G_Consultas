# questionnaire.QCLXXRCURAV

> Registro de Curaciones avanzadas

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro de Curaciones avanzadas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hola Evaluación |
| Q03 | varchar |  |  | SI | Registro |
| Q04 | numeric |  |  | SI | Longitud (cm) |
| Q05 | numeric |  |  | SI | Ancho (cm) |
| Q06 | numeric |  |  | SI | Profundidad (cm) |
| Q07 | varchar |  |  | SI | Tipo de Herida |
| Q08 | varchar |  |  | SI | Otra Herida |
| Q09 | varchar |  |  | SI | Aspecto de la Herida |
| Q10 | varchar |  |  | SI | Mayor Extensión/Diámetro |
| Q11 | varchar |  |  | SI | Profundidad |
| Q12 | varchar |  |  | SI | Exudado Cantidad |
| Q13 | varchar |  |  | SI | Exudado Calidad |
| Q14 | varchar |  |  | SI | Tejido Esfacelado o Necrótico |
| Q15 | varchar |  |  | SI | Tejido Granulatorio |
| Q16 | varchar |  |  | SI | Edema |
| Q17 | varchar |  |  | SI | Escala del Dolor |
| Q18 | varchar |  |  | SI | Piel Circundante |
| Q19 | bit |  |  | SI | Limpieza con Agua Destilada Estéril |
| Q20 | varchar |  |  | SI | Cantidad Utilizada de Agua destilada estéril |
| Q21 | bit |  |  | SI | Limpieza con suero fisiológico 0,9% |
| Q22 | varchar |  |  | SI | Cantidad Utilizada de Suero fisiológico 0,9% |
| Q23 | bit |  |  | SI | Limpieza con Prontosan |
| Q24 | varchar |  |  | SI | Cantidad Utilizada de Prontosan |
| Q25 | bit |  |  | SI | Limpieza con Vashe |
| Q26 | varchar |  |  | SI | Cantidad Utilizada de Vashe |
| Q27 | varchar |  |  | SI | Otra Agua Destilada Estéril |
| Q28 | varchar |  |  | SI | Otro Suero Fisiológico |
| Q29 | varchar |  |  | SI | Otra Prontosan |
| Q30 | varchar |  |  | SI | Otro&nbsp;Vashe |
| Q31 | varchar |  |  | SI | Cobertura Utilizada |
| Q32 | varchar |  |  | SI | Otra Cobertura Utilizada |
| Q33 | varchar |  |  | SI | Apósito Interactivo |
| Q34 | varchar |  |  | SI | Otra Apósito Interactivo |
| Q35 | varchar |  |  | SI | Apósito Bioactivo |
| Q36 | varchar |  |  | SI | Otra Apósito Bioactivo |
| Q37 | varchar |  |  | SI | Apósito Mixto |
| Q38 | varchar |  |  | SI | Otro Apósito Mixto |
| Q39 | varchar |  |  | SI | Protector Cutáneo |
| Q40 | varchar |  |  | SI | Otra Protector Cutáneo |
| Q41 | varchar |  |  | SI | Vendaje de Fijación |
| Q42 | varchar |  |  | SI | Otra Vendaje de Fijacion |
| Q43 | varchar |  |  | SI | TPN/VAC |
| Q44 | varchar |  |  | SI | Categoria de Lesión por Presión |
| Q45 | varchar |  |  | SI | Descripción de Contenido Drenado |
| Q46 | varchar |  |  | SI | Otra Descripción de Contenido Drenado |
| Q47 | varchar |  |  | SI | Presencia de Sutura Quirúrgica |
| Q48 | varchar |  |  | SI | Se Retiran |
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