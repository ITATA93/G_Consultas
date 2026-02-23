# SQLUser.MR_ObjFind

**Schema:** SQLUser
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MROBJ_MRADM_ParRef | bigint | PK |  | NO | Des Ref to MRADM |
| MROBJ_Childsub | numeric |  |  | NO | MROBJ Childsub (NewKey) |
| MROBJ_Date | date |  |  | SI | Date |
| MROBJ_Desc | varchar |  |  | SI | Description of Objective Finding |
| MROBJ_DocCode_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| MROBJ_EditCP_DR | varchar |  | FK | SI | Des Ref EditCP_DR |
| MROBJ_HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| MROBJ_HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| MROBJ_RTFNotes | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| MROBJ_RowId | varchar |  |  | NO | - |
| MROBJ_Status | varchar |  |  | SI | Objective Status |
| MROBJ_Time | time |  |  | SI | Time |
| MROBJ_UpdateDate | date |  |  | SI | Update Date |
| MROBJ_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| MROBJ_UpdateTime | time |  |  | SI | Update Time |
| MROBJ_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Text |
| Q01TxtOnly | - |  |  | SI | Text Plain Text Only |
| Q02 | - |  |  | SI | Title |
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