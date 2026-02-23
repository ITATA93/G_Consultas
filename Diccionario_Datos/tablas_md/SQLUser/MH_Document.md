# SQLUser.MH_Document

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Salud Mental**. Módulo de psiquiatría.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_RowId | bigint | PK |  | NO | - |
| DOC_CreatedDate | date |  |  | SI | CreatedDate |
| DOC_CreatedTime | time |  |  | SI | CreatedTime |
| DOC_Deleted | varchar |  |  | SI | Deleted |
| DOC_DetSuspension_DR | varchar |  | FK | SI | Des Ref MHDetSuspension |
| DOC_Detention_DR | bigint |  | FK | SI | Des Ref MHDetention |
| DOC_DocumentType_DR | bigint |  | FK | SI | Des Ref MHCDocumentType |
| DOC_EditableLetter_DR | bigint |  | FK | SI | Des Ref PALetter |
| DOC_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| DOC_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| DOC_Questionnaire | varchar |  |  | SI | Questionnaire |
| DOC_ScannedDocument | varchar |  |  | SI | ScannedDocument |
| DOC_ScannedDocument_DR | varchar |  | FK | SI | Des Ref PAPersonPictures |
| DOC_SignedAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| DOC_SignedDetAgent_DR | varchar |  | FK | SI | Des Ref MHDetAgent |
| DOC_Task_DR | bigint |  | FK | SI | Des Ref epr.TaskList |
| Q1DSinf | - |  |  | SI | Cota Inferior -1DS |
| Q1DSsup | - |  |  | SI | Cota Superior 1DS |
| Q2DSinf | - |  |  | SI | Cota Inferior -2DS |
| Q2DSsup | - |  |  | SI | Cota Superior 2DS |
| Q3DSinf | - |  |  | SI | Cota Inferior -3DS |
| Q3DSsup | - |  |  | SI | Cota Superior 3DS |
| QMEDIA | - |  |  | SI | Mediana |
| QTalla | - |  |  | SI | Talla |
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