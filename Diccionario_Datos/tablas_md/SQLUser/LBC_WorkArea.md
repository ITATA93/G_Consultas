# SQLUser.LBC_WorkArea

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCWA_RowID | bigint | PK |  | NO | - |
| LBCQCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCWA_Code | varchar |  |  | NO | Code |
| LBCWA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCWA_CreatedDate | date |  |  | SI | Created Date |
| LBCWA_CreatedTime | time |  |  | SI | Created Time |
| LBCWA_DateFrom | date |  |  | SI | Date from |
| LBCWA_DateTo | date |  |  | SI | Date to |
| LBCWA_Department_DR | bigint |  | FK | SI | Department |
| LBCWA_Desc | varchar |  |  | NO | Description |
| LBCWA_EnableSpecimenReceive | varchar |  |  | SI | Enable to appear in Work Area Specimen Receive |
| LBCWA_LabSite_DR | bigint |  | FK | NO | Lab Site  |
| LBCWA_Owner | varchar |  |  | SI | Owner |
| LBCWA_Procedures | varchar |  |  | SI | Procedures |
| LBCWA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCWA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCWA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Valoración del Dolor |
| Q02 | - |  |  | SI | Escala de Dolor |
| Q02ObsDR | - |  |  | SI | Escala de Dolor DR |
| Q03 | - |  |  | SI | Razones para No Evaluar Dolor |
| Q04 | - |  |  | SI | Especifique |
| Q05 | - |  |  | SI | Imagen |
| Q06 | - |  |  | SI | Ubicación del Dolor |
| Q06ObsDR | - |  |  | SI | Ubicación del Dolor DR |
| Q07 | - |  |  | SI | Razones para no Evaluar Dolor |
| Q07ObsDR | - |  |  | SI | Razones para no Evaluar Dolor DR |
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