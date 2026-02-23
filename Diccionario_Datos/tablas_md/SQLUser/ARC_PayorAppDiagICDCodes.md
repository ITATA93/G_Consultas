# SQLUser.ARC_PayorAppDiagICDCodes

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICD_ParRef | bigint | PK |  | NO | ARC_PayorApprovalDiag Parent Reference |
| ICD_Childsub | double |  |  | NO | Childsub |
| ICD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICD_Code_DR | bigint |  | FK | SI | Des Ref MRC_ICDDx |
| ICD_CreatedDate | date |  |  | SI | Created Date |
| ICD_CreatedTime | time |  |  | SI | Created Time |
| ICD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICD_DateFrom | date |  |  | NO | Date From |
| ICD_DateTo | date |  |  | SI | Date To |
| ICD_EpisodeType | varchar |  |  | SI | Episode Type |
| ICD_RowId | varchar |  |  | NO | - |
| ICD_UpdatedDate | date |  |  | SI | Updated Date |
| ICD_UpdatedTime | time |  |  | SI | Updated Time |
| ICD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nada de Dolor |
| Q02 | - |  |  | SI | Nada Agotado (Cansancio, Debelidad) |
| Q03 | - |  |  | SI | Nada Somnoliento (Adormilado) |
| Q04 | - |  |  | SI | Sin Náuseas |
| Q05 | - |  |  | SI | Ninguna Pérdida de Apetito |
| Q06 | - |  |  | SI | Ninguna dificultad para Respirar |
| Q07 | - |  |  | SI | Nada Desanimado |
| Q08 | - |  |  | SI | Nada Nervioso (Intranquilidad, Ansiedad) |
| Q09 | - |  |  | SI | Duermo Perfectamente |
| Q10 | - |  |  | SI | Sentirse Perfectamente (Sensación de Bienestar) |
| Q11 | - |  |  | SI | Descripción del problema |
| Q12 | - |  |  | SI | Otro Problema |
| Q14 | - |  |  | SI | El peor dolor que se pueda imaginar |
| Q16 | - |  |  | SI | Lo más agotado que se puede imaginar |
| Q18 | - |  |  | SI | Lo más somnoliento que se pueda imaginar |
| Q20 | - |  |  | SI | Las peores náuseas que se pueda imaginar |
| Q22 | - |  |  | SI | La peor apetito que se pueda imaginar |
| Q24 | - |  |  | SI | La mayor dificultad para respirar que se pueda ima... |
| Q26 | - |  |  | SI | El más desanimado que se pueda imaginar |
| Q28 | - |  |  | SI | Lo más nervioso que se pueda imaginar |
| Q30 | - |  |  | SI | La mayor dificulta para dormir que se pueda imagin... |
| Q31 | - |  |  | SI | Sentirse lo peor que se pueda imaginar |
| Q32 | - |  |  | SI | Lo peor posible |
| Q33 | - |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q34 | - |  |  | SI | Cada puntuación representa la gravedad del síntoma... |
| Q35 | - |  |  | SI | El Sistema de Evaluación de Síntomas de Edmonton (... |
| Q36 | - |  |  | SI | Un número más alto se asocia con una mayor graveda... |
| Q47 | - |  |  | SI | Clasificación |
| Q49 | - |  |  | SI | Gravedad del problema |
| Q59 | - |  |  | SI | Fecha Evaluación |
| Q60 | - |  |  | SI | Hora Evaluación |
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