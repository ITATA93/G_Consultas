# SQLUser.LBC_ReasonForTesting

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRFT_RowID | bigint | PK |  | NO | - |
| ChildQ16DR | - |  |  | SI | Child Reference: Área a Preparar |
| LBCRFT_Code | varchar |  |  | NO | Code |
| LBCRFT_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCRFT_CreatedDate | date |  |  | SI | Created Date |
| LBCRFT_CreatedTime | time |  |  | SI | Created Time |
| LBCRFT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRFT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRFT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRFT_Desc | varchar |  |  | NO | Description |
| LBCRFT_Owner | varchar |  |  | SI | Owner |
| LBCRFT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRFT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRFT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Estado de la piel |
| Q02 | - |  |  | SI | Localización y Tipo de Lesión |
| Q03 | - |  |  | SI | Tricotomía |
| Q04 | - |  |  | SI | Localización tricotomía |
| Q05 | - |  |  | SI | Lateralidad tricotomia |
| Q06 | - |  |  | SI | Área a preparar |
| Q07 | - |  |  | SI | Aseo de piel |
| Q08 | - |  |  | SI | Responsable Aseo |
| Q09 | - |  |  | SI | Antisepsia Piel |
| Q10 | - |  |  | SI | Responsable Antisepsia |
| Q11 | - |  |  | SI | Otra (estado de la piel) |
| Q12 | - |  |  | SI | comentario tricotomía |
| Q13 | - |  |  | SI | Otra Estado de la piel |
| Q14 | - |  |  | SI | Otro Antisepsia Piel |
| Q15 | - |  |  | SI | Otro tipo de aseo |
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