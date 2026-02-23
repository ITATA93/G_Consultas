# SQLUser.ARC_OrdSetsHosp

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | varchar | PK |  | NO | ARC_OrdSets Parent Reference |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_DateFrom | date |  |  | SI | Date From |
| HOSP_DateTo | date |  |  | SI | Date To |
| HOSP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HOSP_RowId | varchar |  |  | NO | - |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | a) Epicrisis Médica |
| Q02 | - |  |  | SI | b) Interconsultas |
| Q03 | - |  |  | SI | c) Horas de Control |
| Q04 | - |  |  | SI | d) Exámenes |
| Q05 | - |  |  | SI | e) Material Educativo |
| Q06 | - |  |  | SI | f) Pertenencias Personales |
| Q07 | - |  |  | SI | g) Otros |
| Q08 | - |  |  | SI | h) Acompañante durante el Traslado |
| Q09 | - |  |  | SI | Comentarios Epicrisis Médica |
| Q10 | - |  |  | SI | Comentarios Interconsultas |
| Q11 | - |  |  | SI | Comentarios Horas de Control |
| Q12 | - |  |  | SI | Comentarios Exámenes |
| Q13 | - |  |  | SI | Comentarios Material Educativo |
| Q14 | - |  |  | SI | Comentarios Pertenencias Personales |
| Q15 | - |  |  | SI | Comentarios Otros |
| Q16 | - |  |  | SI | Comentarios Acompañante durante el Traslado |
| Q17 | - |  |  | SI | Nombre de quien recibe los documentos |
| Q18 | - |  |  | SI | Nombre a quien se le notifica el traslado |
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