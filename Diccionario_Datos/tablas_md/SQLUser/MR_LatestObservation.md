# SQLUser.MR_LatestObservation

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOBS_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| LOBS_Childsub | double |  |  | NO | Childsub |
| LOBS_MRObsItem_DR | varchar |  | FK | SI | Des Ref MRObsItem_ |
| LOBS_ObsItem_DR | bigint |  | FK | SI | Des Ref ObsItem |
| LOBS_RowId | varchar |  |  | NO | - |
| LOBS_Value | varchar |  |  | SI | Value |
| Q01 | - |  |  | SI | Epidural Date and time of Insertion |
| Q02 | - |  |  | SI | Epidural Level of Insertion |
| Q03 | - |  |  | SI | Epidural Checks |
| Q04 | - |  |  | SI | Dermatome Level |
| Q06 | - |  |  | SI | Sedation Score |
| Q07 | - |  |  | SI | Pain Score |
| Q08 | - |  |  | SI | Sedation Score |
| Q08ObsDR | - |  |  | SI | Sedation Score DR |
| Q09 | - |  |  | SI | Motor block checked and recovered 2hrs post remova... |
| Q09ObsDR | - |  |  | SI | Motor block checked and recovered 2hrs post remova... |
| Q10 | - |  |  | SI | Date of Removal |
| Q11 | - |  |  | SI | Time of Removal |
| Q12 | - |  |  | SI | Removed by |
| Q13 | - |  |  | SI | Inserted by |
| Q14 | - |  |  | SI | Time of insertion |
| Q16 | - |  |  | SI | Date |
| Q17 | - |  |  | SI | Time |
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