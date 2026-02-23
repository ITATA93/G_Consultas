# SQLUser.LBC_ReportPageAllocation

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRPA_RowID | bigint | PK |  | NO | - |
| LBCRPA_AllocationType | varchar |  |  | SI | Allocation Type |
| LBCRPA_CareProv_DR | varchar |  | FK | SI | Care Provider Recipient |
| LBCRPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRPA_DateFrom | date |  |  | SI | Effective Start Date |
| LBCRPA_DateTo | date |  |  | SI | Effective End Date |
| LBCRPA_LabSiteOrigin_DR | bigint |  | FK | SI | Lab Site Origin |
| LBCRPA_Location_DR | bigint |  | FK | SI | Location As Recipient |
| LBCRPA_Owner | varchar |  |  | SI | Owner |
| LBCRPA_RecipientType | varchar |  |  | SI | Recipient Type |
| LBCRPA_RefDoc_DR | bigint |  | FK | SI | Referral Doctor Recipient |
| LBCRPA_ReportPage_DR | bigint |  | FK | SI | Report Page |
| LBCRPA_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCRPA_TestSetRevision_DR | bigint |  | FK | SI | Test Set Revision |
| LBCRPA_TestSetWorkGroup_DR | bigint |  | FK | SI | Cumulative Report Group
Mutually Exclusive to LBC... |
| LBCRPA_ThirdParty_DR | bigint |  | FK | SI | Third Party Recipient |
| Q01 | - |  |  | SI | Escala Numérica del Dolor |
| Q01ObsDR | - |  |  | SI | Escala Numérica del Dolor DR |
| Q02 | - |  |  | SI | Tipo de Dolor |
| Q03 | - |  |  | SI | Ubicación del Dolor |
| Q04 | - |  |  | SI | Irradia Dolor |
| Q05 | - |  |  | SI | Exacerba Dolor |
| Q06 | - |  |  | SI | Disminuye Dolor |
| Q07 | - |  |  | SI | Ubicación del dolor |
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