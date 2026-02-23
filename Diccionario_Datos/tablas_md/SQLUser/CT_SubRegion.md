# SQLUser.CT_SubRegion

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBREG_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Living Situation/ Social Support |
| Q03 | - |  |  | SI | Number of Previous Admissions / Emergency Room Vis... |
| Q04 | - |  |  | SI | Number of Active Medical Problems |
| Q05 | - |  |  | SI | Cognition |
| Q06 | - |  |  | SI | Functional Status |
| Q07 | - |  |  | SI | Behaviour Pattern |
| Q08 | - |  |  | SI | Mobility |
| Q09 | - |  |  | SI | Sensory Deficits |
| Q10 | - |  |  | SI | 0 - 10: At risk for home care services |
| Q11 | - |  |  | SI | 11 - 19: At risk for discharge planning |
| Q12 | - |  |  | SI | 20+: At risk for placement other than home |
| Q13 | - |  |  | SI | The Blaylock Risk Assessment Screening Score (BRAS... |
| Q14 | - |  |  | SI | Number of Drugs |
| Q15 | - |  |  | SI | No valid score |
| Q16 | - |  |  | SI | Refer the patient for discharge coordination |
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
| SUBREG_Code | varchar |  |  | NO | Code |
| SUBREG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBREG_CreatedDate | date |  |  | SI | Created Date |
| SUBREG_CreatedTime | time |  |  | SI | Created Time |
| SUBREG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBREG_DateFrom | date |  |  | SI | Date From |
| SUBREG_DateTo | date |  |  | SI | Date To |
| SUBREG_Desc | varchar |  |  | NO | Description |
| SUBREG_OnlineDocRegionCode | varchar |  |  | SI | Online Documentation Region Code |
| SUBREG_Owner | varchar |  |  | SI | Owner |
| SUBREG_UpdatedDate | date |  |  | SI | Updated Date |
| SUBREG_UpdatedTime | time |  |  | SI | Updated Time |
| SUBREG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*