# SQLUser.CT_LocStorageBin

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STORBIN_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | Do you have a husband, wife or partner |
| Q01A | - |  |  | SI | Surname |
| Q01B | - |  |  | SI | Forename |
| Q01C | - |  |  | SI | Home phone |
| Q01D | - |  |  | SI | Mobile phone |
| Q01E | - |  |  | SI | Date of birth |
| Q01F | - |  |  | SI | Previous name |
| Q01G | - |  |  | SI | Occupation |
| Q01H | - |  |  | SI | Employment status |
| Q01I | - |  |  | SI | Place of birth |
| Q02 | - |  |  | SI | Is the person above the baby's father |
| Q02A | - |  |  | SI | Surname |
| Q02B | - |  |  | SI | Forename |
| Q02C | - |  |  | SI | Home phone |
| Q02D | - |  |  | SI | Mobile phone |
| Q02E | - |  |  | SI | Address |
| Q02H | - |  |  | SI | Father's occupation |
| Q02I | - |  |  | SI | Father's employment status |
| Q03 | - |  |  | SI | Father's ethnic category |
| Q04 | - |  |  | SI | Father's family origins are Mediterranean, African... |
| Q05 | - |  |  | SI | Details |
| Q22 | - |  |  | SI | Father's date of birth a |
| Q23 | - |  |  | SI | Father's place of birth a |
| Q24 | - |  |  | SI | Is address same as woman's a |
| Q24A | - |  |  | SI | Address a |
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
| STORBIN_Childsub | double |  |  | NO | Childsub |
| STORBIN_Code | varchar |  |  | NO | Code |
| STORBIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STORBIN_CreatedDate | date |  |  | SI | Created Date |
| STORBIN_CreatedTime | time |  |  | SI | Created Time |
| STORBIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STORBIN_DateFrom | date |  |  | SI | Date From |
| STORBIN_DateTo | date |  |  | SI | Date To |
| STORBIN_Desc | varchar |  |  | NO | Description |
| STORBIN_RowId | varchar |  |  | NO | - |
| STORBIN_StorBinGroup_DR | bigint |  | FK | SI | Des Ref to INCStorageBinGroup |
| STORBIN_StorBinType_DR | bigint |  | FK | SI | Des Ref to INCStorageBinType |
| STORBIN_UpdatedDate | date |  |  | SI | Updated Date |
| STORBIN_UpdatedTime | time |  |  | SI | Updated Time |
| STORBIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*