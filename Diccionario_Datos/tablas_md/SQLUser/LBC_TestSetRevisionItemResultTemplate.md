# SQLUser.LBC_TestSetRevisionItemResultTemplate

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRIRT_ParRef | varchar | PK |  | NO | - |
| LBCTSRIRT_AllowMultiple | varchar |  |  | SI | Allow Multiple |
| LBCTSRIRT_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRIRT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LBCTSRIRT_DateFrom | date |  |  | NO | Date From
Effective date for the record |
| LBCTSRIRT_DateTo | date |  |  | SI | Date To
Last day the record is active
Optional. ... |
| LBCTSRIRT_IncludeSpecimenDetails | varchar |  |  | SI | Include Specimen Details |
| LBCTSRIRT_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRIRT_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRIRT_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRIRT_RowID | varchar |  |  | NO | - |
| LBCTSRIRT_Sequence | numeric |  |  | SI | Rule Sequence |
| LBCTSRIRT_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRIRT_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRIRT_Template_DR | bigint |  | FK | SI | Letter Template |
| Q01 | - |  |  | SI | Oxigenación |
| Q02 | - |  |  | SI | Ventilación |
| Q03 | - |  |  | SI | Observaciones |
| Q04 | - |  |  | SI | ANANO |
| Q05 | - |  |  | SI | FiO2 (%) |
| Q06 | - |  |  | SI | Oxigeno (lts./min) |
| Q07 | - |  |  | SI | Aire (lts./min) |
| Q08 | - |  |  | SI | Protóxido (NO2) (lts./min) |
| Q09 | - |  |  | SI | Circuito |
| Q10 | - |  |  | SI | Aire (lts./min) |
| Q11 | - |  |  | SI | Protóxido (NO2) (lts./min) |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*