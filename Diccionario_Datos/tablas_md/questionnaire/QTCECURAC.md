# questionnaire.QTCECURAC

> Curación Avanzada de Heridas

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Curación Avanzada de Heridas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de herida |
| Q02 | varchar |  |  | SI | Otro tipo de herida |
| Q03 | varchar |  |  | SI | Ubicación de la herida |
| Q04 | varchar |  |  | SI | Infección de la Herida |
| Q05 | varchar |  |  | SI | Tratamiento Antibiótico Actual |
| Q06 | varchar |  |  | SI | Descripción de la herida |
| Q07 | varchar |  |  | SI | Otra descripción de herida |
| Q08 | numeric |  |  | SI | Longitud (cm) |
| Q09 | numeric |  |  | SI | Ancho (cm) |
| Q10 | numeric |  |  | SI | Profundidad (cm) |
| Q11 | varchar |  |  | SI | Descripción del exudado |
| Q12 | varchar |  |  | SI | Otro descripción de contenido drenado |
| Q13 | varchar |  |  | SI | Acciones Realizadas en la Herida |
| Q14 | varchar |  |  | SI | Otra Acciones Realizadas en la Herida |
| Q15 | varchar |  |  | SI | Apósito Primario Utilizado |
| Q16 | varchar |  |  | SI | Otro apósito primario |
| Q17 | varchar |  |  | SI | Apósito secundario |
| Q18 | varchar |  |  | SI | Otro apósito secundario |
| Q19 | varchar |  |  | SI | Observaciones de la Herida |
| Q20 | bigint |  |  | SI | Imagen de la herida |
| Q20TxtOnly | bigint |  |  | SI | Imagen de la herida Plain Text Only |
| Q21 | varchar |  |  | SI | Actividad Vendaje |
| Q22 | varchar |  |  | SI | Dimensiones de la herida |
| Q23 | varchar |  |  | SI | cm |
| Q24 | varchar |  |  | SI | cm |
| Q25 | varchar |  |  | SI | cm |
| Q26 | varchar |  |  | SI | Mecanismo causante de la herida |
| Q27 | varchar |  |  | SI | Otra descripción del exudado |
| Q28 | varchar |  |  | SI | Cantidad de exudado |
| Q29 | varchar |  |  | SI | Presencia de sutura |
| Q30 | varchar |  |  | SI | Cuál |
| Q31 | varchar |  |  | SI | Tejido de la herida |
| Q32 | numeric |  |  | SI | Granulación (%) |
| Q33 | numeric |  |  | SI | Esfacelo (%) |
| Q34 | numeric |  |  | SI | Necrótico (%) |
| Q35 | varchar |  |  | SI | Piel circundante |
| Q36 | varchar |  |  | SI | Presencia de drenaje |
| Q37 | varchar |  |  | SI | Cuál |
| Q38 | varchar |  |  | SI | Tratamiento farmacológico relevante |
| Q39 | varchar |  |  | SI | Otro fármaco relevante |
| Q40 | varchar |  |  | SI | Limpieza de la piel |
| Q41 | varchar |  |  | SI | Limpieza de la herida |
| Q42 | varchar |  |  | SI | Arrastre mecánico |
| Q43 | varchar |  |  | SI | Cuál |
| Q44 | varchar |  |  | SI | Desbridamiento |
| Q45 | varchar |  |  | SI | Toma de cultivo |
| Q46 | varchar |  |  | SI | Apósito primario |
| Q47 | varchar |  |  | SI | Protección de la piel |
| Q48 | varchar |  |  | SI | Otra protección de la piel |
| Q49 | varchar |  |  | SI | Fijación |
| Q50 | varchar |  |  | SI | Otra fijación |
| Q51 | varchar |  |  | SI | Terapia coadyuvante |
| Q52 | varchar |  |  | SI | Otra terapia coadyuvante |
| Q53 | varchar |  |  | SI | Plan de Tratamiento / Comentarios |
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