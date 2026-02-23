# SQLUser.LBDR_Batch

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRB_RowID | bigint | PK |  | NO | - |
| LBDRB_AntibioticSensitivities | varchar |  |  | SI | Text for Antibiotic Sensitivities
Translated |
| LBDRB_AttachmentMaxCol | numeric |  |  | SI | Number of column for attachment |
| LBDRB_BatchDate | date |  |  | SI | Batch Date
The date when the Batch was created |
| LBDRB_BatchFooterClass | varchar |  |  | SI | Batch Footer Zen Report - a copy of LBCDRBatchFoot... |
| LBDRB_BatchHeaderClass | varchar |  |  | SI | Batch Header Zen Report - a copy of LBCDRBatchHead... |
| LBDRB_BatchSortKey | varchar |  |  | SI | Batch Sort Key
The value used to determine the or... |
| LBDRB_BatchTime | time |  |  | SI | Batch Time
The time when the Batch was created |
| LBDRB_BatchType | varchar |  |  | SI | Batch Type From LBCDRBBatchType, with addition of ... |
| LBDRB_ConfLocationCode | varchar |  |  | SI | Courier Confidential LabSite Code (for report) |
| LBDRB_ConfLocationDesc | varchar |  |  | SI | Courier Confidential LabSite Desc (for report) |
| LBDRB_Confidential | varchar |  |  | SI | Courier is Confidential - Translated text for repo... |
| LBDRB_CourierCode | varchar |  |  | SI | Courier Code (for report) |
| LBDRB_CourierDesc | varchar |  |  | SI | Courier Desc (for report) |
| LBDRB_Courier_DR | bigint |  | FK | SI | Courier |
| LBDRB_DFTIDs | varchar |  |  | SI | Comma-List of LBDRDFTIDs in the Batch
Use to gene... |
| LBDRB_EpisodeReportClass | varchar |  |  | SI | Episode ZENReport Class
No longer used |
| LBDRB_IncludePreliminary | integer |  |  | SI | Preliminary Results Included
1=yes |
| LBDRB_LBCDRBatch_DR | bigint |  | FK | SI | The Batch definition used for this Batch |
| LBDRB_LanguageID | varchar |  |  | SI | Batch Language
The ID of the language (User.SSLan... |
| LBDRB_MICReportingFormat | varchar |  |  | SI | MIC Reporting Format
When the field is blank, usi... |
| LBDRB_OrganismBoldFont | varchar |  |  | SI | Show Organism Line in Bold. |
| LBDRB_OrganismNoItalics | varchar |  |  | SI | Show Organism Line without italics. |
| LBDRB_PreliminaryText | varchar |  |  | SI | Preliminary Report Text
The text to appear on the... |
| LBDRB_PrintDate | date |  |  | SI | Batch Print Date
The date when the Batch was (las... |
| LBDRB_PrintTime | time |  |  | SI | Batch Print Time
The time when the Batch was (las... |
| LBDRB_ReportFont | varchar |  |  | SI | Doctors Reports Font
Specifies the font family to... |
| LBDRB_ReportRequestCheckPoint | integer |  |  | SI | ReportRequest Checkpoint
When an InstantPrint bat... |
| LBDRB_ReprintOfBatch | varchar |  |  | SI | Reprint of Batch
The ID of the Batch for which th... |
| LBDRB_ReprintText | varchar |  |  | SI | Reprint Text for Reports
'Printed' or 'Reprint' t... |
| LBDRB_ShowMedicalStaffAsgn | varchar |  |  | SI | Display Medical Staff Assignment in Doctor Report ... |
| Q01 | - |  |  | SI | pa / FiO2 |
| Q02 | - |  |  | SI | Recuento Plaquetas (x mil) |
| Q03 | - |  |  | SI | Bilirrubina (md/dl) |
| Q04 | - |  |  | SI | Hipotensión |
| Q05 | - |  |  | SI | Puntaje Glasgow |
| Q06 | - |  |  | SI | Creatinina mg/dl |
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