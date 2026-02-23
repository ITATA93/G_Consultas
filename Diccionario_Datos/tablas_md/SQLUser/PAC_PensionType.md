# SQLUser.PAC_PensionType

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PENSTYPE_RowId | bigint | PK |  | NO | - |
| PENSTYPE_Code | varchar |  |  | NO | Code |
| PENSTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PENSTYPE_CreatedDate | date |  |  | SI | Created Date |
| PENSTYPE_CreatedTime | time |  |  | SI | Created Time |
| PENSTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PENSTYPE_DateFrom | date |  |  | SI | Date From |
| PENSTYPE_DateTo | date |  |  | SI | Date To |
| PENSTYPE_Desc | varchar |  |  | NO | Description |
| PENSTYPE_Owner | varchar |  |  | SI | Owner |
| PENSTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| PENSTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| PENSTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type |
| Q04 | - |  |  | SI | Ovarian cancer |
| Q05 | - |  |  | SI | Cervical cancer |
| Q06 | - |  |  | SI | Endometriosis |
| Q07 | - |  |  | SI | Symptoms |
| Q08 | - |  |  | SI | Personal documentation |
| Q09 | - |  |  | SI | Oncological gynecology examination |
| Q10 | - |  |  | SI | Cancer recurrence |
| Q11 | - |  |  | SI | Next appointment |
| Q12 | - |  |  | SI | Other |
| Q13 | - |  |  | SI | Therapeutic indications |
| Q14 | - |  |  | SI | Lab tests to be carried out |
| Q15 | - |  |  | SI | Radiology tests to be carried out |
| Q16 | - |  |  | SI | Other tests to be carried out |
| Q17 | - |  |  | SI | Colposcopy |
| Q18 | - |  |  | SI | Papanicolaou test |
| Q19 | - |  |  | SI | Colposcopy date |
| Q20 | - |  |  | SI | Papanicolaou test date |
| Q21 | - |  |  | SI | Other |
| Q22 | - |  |  | SI | Summary of recent clinical events |
| Q23 | - |  |  | SI | Notes |
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