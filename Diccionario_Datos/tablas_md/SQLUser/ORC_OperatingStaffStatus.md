# SQLUser.ORC_OperatingStaffStatus

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPSTFS_RowId | bigint | PK |  | NO | - |
| OPSTFS_Code | varchar |  |  | NO | Code |
| OPSTFS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPSTFS_CreatedDate | date |  |  | SI | Created Date |
| OPSTFS_CreatedTime | time |  |  | SI | Created Time |
| OPSTFS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPSTFS_DateFrom | date |  |  | SI | Date From |
| OPSTFS_DateTo | date |  |  | SI | Date To |
| OPSTFS_Desc | varchar |  |  | NO | Description |
| OPSTFS_Owner | varchar |  |  | SI | Owner |
| OPSTFS_UpdatedDate | date |  |  | SI | Updated Date |
| OPSTFS_UpdatedTime | time |  |  | SI | Updated Time |
| OPSTFS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of dialysis |
| Q02 | - |  |  | SI | Haemodiafiltration type |
| Q03 | - |  |  | SI | Session No |
| Q04 | - |  |  | SI | Machine |
| Q05 | - |  |  | SI | Machine No. |
| Q06 | - |  |  | SI | Treatment duration (hours) |
| Q07 | - |  |  | SI | Dialyzer |
| Q08 | - |  |  | SI | Dialysate bath |
| Q09 | - |  |  | SI | Dialysate concentrate - Sodium (NA) (mmol/L) |
| Q10 | - |  |  | SI | Dialysate concentrate - Potassium (K) (mmol/L) |
| Q11 | - |  |  | SI | Dialysate concentrate - Calcium (CA) (mmol/L) |
| Q12 | - |  |  | SI | Dialysate concentrate - Bicarbonate (HCO3) (mmol/L... |
| Q13 | - |  |  | SI | Dialysate fluid temperature (C) |
| Q14 | - |  |  | SI | Ultra filtration profile |
| Q15 | - |  |  | SI | Mode |
| Q16 | - |  |  | SI | Sodium (Na) profile |
| Q17 | - |  |  | SI | Start value (mmol/L) |
| Q18 | - |  |  | SI | End value (mmol/L) |
| Q19 | - |  |  | SI | Duration (hours) |
| Q20 | - |  |  | SI | Bicarbonate (HCO3) profile |
| Q21 | - |  |  | SI | Start value (mmol/L) |
| Q22 | - |  |  | SI | End value (mmol/L) |
| Q23 | - |  |  | SI | Duration (hours) |
| Q24 | - |  |  | SI | Isolated ultrafiltration |
| Q25 | - |  |  | SI | Isolated ultrafiltration volume (L) |
| Q26 | - |  |  | SI | Duration (hours) |
| Q28 | - |  |  | SI | Vascular access |
| Q28ObsDR | - |  |  | SI | Vascular access DR |
| Q29 | - |  |  | SI | Access site location |
| Q30 | - |  |  | SI | Catheter locking solution (if permanent / temporar... |
| Q31 | - |  |  | SI | Dialysis needle size |
| Q31ObsDR | - |  |  | SI | Dialysis needle size DR |
| Q32 | - |  |  | SI | Arterial volume (ml) |
| Q33 | - |  |  | SI | Venous volume (ml) |
| Q34 | - |  |  | SI | Dialysis treatment comments |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
| Q37 | - |  |  | SI | Access site location |
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