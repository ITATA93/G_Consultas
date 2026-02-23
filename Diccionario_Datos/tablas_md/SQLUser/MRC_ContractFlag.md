# SQLUser.MRC_ContractFlag

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTFL_RowId | bigint | PK |  | NO | - |
| CONTFL_Code | varchar |  |  | NO | Code |
| CONTFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTFL_CreatedDate | date |  |  | SI | Created Date |
| CONTFL_CreatedTime | time |  |  | SI | Created Time |
| CONTFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTFL_DateFrom | date |  |  | SI | Date From |
| CONTFL_DateTo | date |  |  | SI | Date To |
| CONTFL_Desc | varchar |  |  | NO | Description |
| CONTFL_Owner | varchar |  |  | SI | Owner |
| CONTFL_UpdatedDate | date |  |  | SI | Updated Date |
| CONTFL_UpdatedTime | time |  |  | SI | Updated Time |
| CONTFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QL | - |  |  | SI | L |
| QM | - |  |  | SI | M |
| QMeses | - |  |  | SI | Edad Corregida en Meses |
| QS | - |  |  | SI | S |
| QSD0 | - |  |  | SI | SD0 |
| QSD1 | - |  |  | SI | SD1 |
| QSD1neg | - |  |  | SI | SD1neg |
| QSD2 | - |  |  | SI | SD2 |
| QSD2neg | - |  |  | SI | SD2neg |
| QSD3 | - |  |  | SI | SD3 |
| QSD3neg | - |  |  | SI | SD3neg |
| QStDev | - |  |  | SI | StDev |
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