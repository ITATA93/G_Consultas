# SQLUser.MRC_BodyPartsSymptoms

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SYM_ParRef | bigint | PK |  | NO | MRC_BodyParts Parent Reference |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Servicio Clínico |
| Q04 | - |  |  | SI | Motivo de Ingreso |
| Q05 | - |  |  | SI | Anamnesis Próxima |
| Q06 | - |  |  | SI | Examen General |
| Q07 | - |  |  | SI | Descripción Ex. General |
| Q08 | - |  |  | SI | Ex. Cabeza y Cuello |
| Q09 | - |  |  | SI | Descripción Ex. Cabeza y Cuello |
| Q10 | - |  |  | SI | Ex. Cardiopulmonar |
| Q11 | - |  |  | SI | Examen Cardíaco |
| Q12 | - |  |  | SI | Descripción Ex. Cardíaco |
| Q13 | - |  |  | SI | Examen Pulmonar |
| Q14 | - |  |  | SI | Descripción Ex. Pulmonar |
| Q15 | - |  |  | SI | Ex. Abdominal |
| Q16 | - |  |  | SI | Ex. Región Genital / Anal |
| Q17 | - |  |  | SI | Descripción: Ex. Región Genital / Anal |
| Q18 | - |  |  | SI | Ex. Extremidades |
| Q19 | - |  |  | SI | Descripción: Ex. Extremidades |
| Q20 | - |  |  | SI | Otros comentarios del Ex. Físico |
| Q21 | - |  |  | SI | Plan de Manejo al Ingreso |
| Q22 | - |  |  | SI | Descripción Ex. Abdominal |
| Q23 | - |  |  | SI | Ex. Neurológico |
| Q24 | - |  |  | SI | Descripción Ex. Neurológico |
| Q25 | - |  |  | SI | Conclusión |
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
| SYM_Childsub | double |  |  | NO | Childsub |
| SYM_Code | varchar |  |  | NO | Code |
| SYM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SYM_CreatedDate | date |  |  | SI | Created Date |
| SYM_CreatedTime | time |  |  | SI | Created Time |
| SYM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SYM_Desc | varchar |  |  | NO | Description |
| SYM_RowId | varchar |  |  | NO | - |
| SYM_UpdatedDate | date |  |  | SI | Updated Date |
| SYM_UpdatedTime | time |  |  | SI | Updated Time |
| SYM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*