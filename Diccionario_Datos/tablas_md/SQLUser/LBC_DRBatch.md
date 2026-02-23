# SQLUser.LBC_DRBatch

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDRB_RowID | bigint | PK |  | NO | - |
| LBCDRB_BatchFooterClass | varchar |  |  | SI | Batch Footer Class
The Zen Report which creates t... |
| LBCDRB_BatchHeaderClass | varchar |  |  | SI | Batch Header Class
The Zen Report which creates t... |
| LBCDRB_BatchType | varchar |  |  | SI | Batch Type
	C = CourierRun batch -  used by regul... |
| LBCDRB_Code | varchar |  |  | NO | Code |
| LBCDRB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDRB_CreatedDate | date |  |  | SI | Created Date |
| LBCDRB_CreatedTime | time |  |  | SI | Created Time |
| LBCDRB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDRB_DateFrom | date |  |  | SI | Date From
Effective date for the record |
| LBCDRB_DateTo | date |  |  | SI | Date To
Last day the record is active  |
| LBCDRB_Desc | varchar |  |  | NO | Description |
| LBCDRB_EpisodeReportClass | varchar |  |  | SI | Episode ZENReport Class
No longer used |
| LBCDRB_LBEPSortOption | varchar |  |  | SI | LabEpisode Sort Option
The value of this property... |
| LBCDRB_Language_DR | bigint |  | FK | SI | Doctors Reports Batch default Language
The langua... |
| LBCDRB_Owner | varchar |  |  | SI | Owner |
| LBCDRB_RecipientFooterClass | varchar |  |  | SI | Recipient Footer Class
The Zen Report which creat... |
| LBCDRB_RecipientHeaderClass | varchar |  |  | SI | Recipient Header Class
The Zen Report which creat... |
| LBCDRB_RecipientSortOption | varchar |  |  | SI | Recipient Sort Option
The value of this property ... |
| LBCDRB_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDRB_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDRB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | CT Safety |
| Q02 | - |  |  | SI | Has the patient ever had a contrast reaction? |
| Q02a | - |  |  | SI | Please state which contrast |
| Q03 | - |  |  | SI | Does the patient have any allergies? |
| Q03a | - |  |  | SI | Please, make sure the Patient's allergies are prop... |
| Q04 | - |  |  | SI | Does the patient have any of the following thyroid... |
| Q05 | - |  |  | SI | Does the patient have asthma? |
| Q05a | - |  |  | SI | Is it currently controlled? |
| Q06 | - |  |  | SI | Renal Function |
| Q07 | - |  |  | SI | Is the patient aged over 65? |
| Q08 | - |  |  | SI | Is the patient diabetic? |
| Q08a | - |  |  | SI | Is the patient taking Metformin for their diabetes... |
| Q09 | - |  |  | SI | Does the patient suffer from heart failure? |
| Q10 | - |  |  | SI | Does the patient have any known chronic kidney dis... |
| Q11 | - |  |  | SI | Did you answer 'Yes' to a Renal Function question? |
| Q11a | - |  |  | SI | Estimated Glomerular Filtration Rate (eGFR) level |
| Q11b | - |  |  | SI | Date of last eGFR test |
| Q11c | - |  |  | SI | Creatinine level |
| Q11d | - |  |  | SI | Date of last Creatinine test |
| Q11e | - |  |  | SI | If this test is older than 6 weeks then please ens... |
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