# SQLUser.ARC_PayAgreemReferral

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REF_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| Q01 | - |  |  | SI | Clasificación de Meggit-Wagner |
| Q02 | - |  |  | SI | Grado |
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
| REF_CTLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| REF_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| REF_Childsub | double |  |  | NO | Childsub |
| REF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REF_CreatedDate | date |  |  | SI | Created Date |
| REF_CreatedTime | time |  |  | SI | Created Time |
| REF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REF_DateFrom | date |  |  | SI | DateFrom |
| REF_DateTo | date |  |  | SI | DateTo |
| REF_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| REF_Message | varchar |  |  | SI | Message |
| REF_Overide | varchar |  |  | SI | REFOveride |
| REF_PayorCPID | varchar |  |  | SI | Payor Care Provider ID |
| REF_RowId | varchar |  |  | NO | - |
| REF_Speciality_DR | bigint |  | FK | SI | Des Ref Speciality |
| REF_UpdatedDate | date |  |  | SI | Updated Date |
| REF_UpdatedTime | time |  |  | SI | Updated Time |
| REF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*