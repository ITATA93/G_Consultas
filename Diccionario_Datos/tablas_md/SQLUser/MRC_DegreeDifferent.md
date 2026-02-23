# SQLUser.MRC_DegreeDifferent

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEGDIF_RowId | bigint | PK |  | NO | - |
| DEGDIF_Code | varchar |  |  | NO | Code |
| DEGDIF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEGDIF_CreatedDate | date |  |  | SI | Created Date |
| DEGDIF_CreatedTime | time |  |  | SI | Created Time |
| DEGDIF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEGDIF_DateFrom | date |  |  | SI | Date From |
| DEGDIF_DateTo | date |  |  | SI | Date To |
| DEGDIF_Desc | varchar |  |  | NO | Description |
| DEGDIF_Owner | varchar |  |  | SI | Owner |
| DEGDIF_UpdatedDate | date |  |  | SI | Updated Date |
| DEGDIF_UpdatedTime | time |  |  | SI | Updated Time |
| DEGDIF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Mamografía |
| Q01ObsDR | - |  |  | SI | Mamografía DR |
| Q02 | - |  |  | SI | Comentario |
| Q03 | - |  |  | SI | Conducta a Seguir |
| Q04 | - |  |  | SI | Fecha de Realización del Examen |
| Q05 | - |  |  | SI | Fecha Próximo Examen |
| Q06 | - |  |  | SI | Fecha de Registro Mamografia |
| Q06ObsDR | - |  |  | SI | Fecha de Registro Mamografia DR |
| Q07 | - |  |  | SI | Conducta a Seguir |
| Q07ObsDR | - |  |  | SI | Conducta a Seguir DR |
| Q08 | - |  |  | SI | Fecha Próxima Mamografía |
| Q08ObsDR | - |  |  | SI | Fecha Próxima Mamografía DR |
| Q09 | - |  |  | SI | Institución |
| Q10 | - |  |  | SI | Dirección |
| Q11 | - |  |  | SI | Ciudad |
| Q12 | - |  |  | SI | RUT |
| Q13 | - |  |  | SI | Mecanismo&nbsp |
| Q14 | - |  |  | SI | Mamografia realizada en el Examen de Medicina Prev... |
| Q15 | - |  |  | SI | Si&nbsp |
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