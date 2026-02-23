# SQLUser.CF_OEObservationRule

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEOBS_RowId | bigint | PK |  | NO | - |
| OEOBS_AgeFrom | double |  |  | SI | AgeFrom  |
| OEOBS_AgeTo | double |  |  | SI | AgeTo  |
| OEOBS_AgeType | varchar |  |  | SI | AgeType |
| OEOBS_DateFrom | date |  |  | SI | DateFrom |
| OEOBS_DateTo | date |  |  | SI | DateTo |
| OEOBS_DaysOffset | double |  |  | SI | DaysOffset  |
| OEOBS_ObservationItem_DR | bigint |  | FK | SI | ObsItemDR |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hola Evaluación |
| Q03 | - |  |  | SI | Registro |
| Q04 | - |  |  | SI | Longitud (cm) |
| Q05 | - |  |  | SI | Ancho (cm) |
| Q06 | - |  |  | SI | Profundidad (cm) |
| Q07 | - |  |  | SI | Tipo de Herida |
| Q08 | - |  |  | SI | Otra Herida |
| Q09 | - |  |  | SI | Aspecto de la Herida |
| Q10 | - |  |  | SI | Mayor Extensión/Diámetro |
| Q11 | - |  |  | SI | Profundidad |
| Q12 | - |  |  | SI | Exudado Cantidad |
| Q13 | - |  |  | SI | Exudado Calidad |
| Q14 | - |  |  | SI | Tejido Esfacelado o Necrótico |
| Q15 | - |  |  | SI | Tejido Granulatorio |
| Q16 | - |  |  | SI | Edema |
| Q17 | - |  |  | SI | Escala del Dolor |
| Q18 | - |  |  | SI | Piel Circundante |
| Q19 | - |  |  | SI | Limpieza con Agua Destilada Estéril |
| Q20 | - |  |  | SI | Cantidad Utilizada de Agua destilada estéril |
| Q21 | - |  |  | SI | Limpieza con suero fisiológico 0,9% |
| Q22 | - |  |  | SI | Cantidad Utilizada de Suero fisiológico 0,9% |
| Q23 | - |  |  | SI | Limpieza con Prontosan |
| Q24 | - |  |  | SI | Cantidad Utilizada de Prontosan |
| Q25 | - |  |  | SI | Limpieza con Vashe |
| Q26 | - |  |  | SI | Cantidad Utilizada de Vashe |
| Q27 | - |  |  | SI | Otra Agua Destilada Estéril |
| Q28 | - |  |  | SI | Otro Suero Fisiológico |
| Q29 | - |  |  | SI | Otra Prontosan |
| Q30 | - |  |  | SI | Otro&nbsp |
| Q31 | - |  |  | SI | Cobertura Utilizada |
| Q32 | - |  |  | SI | Otra Cobertura Utilizada |
| Q33 | - |  |  | SI | Apósito Interactivo |
| Q34 | - |  |  | SI | Otra Apósito Interactivo |
| Q35 | - |  |  | SI | Apósito Bioactivo |
| Q36 | - |  |  | SI | Otra Apósito Bioactivo |
| Q37 | - |  |  | SI | Apósito Mixto |
| Q38 | - |  |  | SI | Otro Apósito Mixto |
| Q39 | - |  |  | SI | Protector Cutáneo |
| Q40 | - |  |  | SI | Otra Protector Cutáneo |
| Q41 | - |  |  | SI | Vendaje de Fijación |
| Q42 | - |  |  | SI | Otra Vendaje de Fijacion |
| Q43 | - |  |  | SI | TPN/VAC |
| Q44 | - |  |  | SI | Categoria de Lesión por Presión |
| Q45 | - |  |  | SI | Descripción de Contenido Drenado |
| Q46 | - |  |  | SI | Otra Descripción de Contenido Drenado |
| Q47 | - |  |  | SI | Presencia de Sutura Quirúrgica |
| Q48 | - |  |  | SI | Se Retiran |
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