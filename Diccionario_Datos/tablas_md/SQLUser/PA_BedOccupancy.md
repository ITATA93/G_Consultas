# SQLUser.PA_BedOccupancy

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Gestión de Camas**. Control de ocupación y asignación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BD_RowId | bigint | PK |  | NO | - |
| BD_BedType_DR | bigint |  | FK | SI | Des Ref BedType |
| BD_Date | date |  |  | SI | Date |
| BD_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| BD_NumberOfBeds | double |  |  | SI | Number Of Beds |
| BD_NumberOfEmptyBeds | double |  |  | SI | Number Of Empty Beds |
| BD_Ward_DR | bigint |  | FK | SI | Des Ref Ward |
| ChildQ28DR | - |  |  | SI | Child Reference: Assessment |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient identified |
| Q04 | - |  |  | SI | Informed consent obtained from patient? |
| Q05 | - |  |  | SI | Pre-procedure checklist |
| Q06 | - |  |  | SI | Pre-procedure notes |
| Q07 | - |  |  | SI | Insertion status |
| Q08 | - |  |  | SI | Insertion date |
| Q09 | - |  |  | SI | Insertion time |
| Q10 | - |  |  | SI | Catheter type |
| Q10ObsDR | - |  |  | SI | Catheter type DR |
| Q11 | - |  |  | SI | Insertion reason |
| Q12 | - |  |  | SI | Other insertion reason |
| Q13 | - |  |  | SI | Catheter material |
| Q13ObsDR | - |  |  | SI | Catheter material DR |
| Q14 | - |  |  | SI | Urinary catheter size (Fr) |
| Q14ObsDR | - |  |  | SI | Urinary catheter size (Fr) DR |
| Q15 | - |  |  | SI | Patient location at time of insertion |
| Q16 | - |  |  | SI | Number of attempts |
| Q17 | - |  |  | SI | Total catheter balloon capacity (mL) |
| Q18 | - |  |  | SI | Fluid used to inflate balloon and inflation volume |
| Q19 | - |  |  | SI | Procedure outcome |
| Q20 | - |  |  | SI | Post-insertion checklist |
| Q21 | - |  |  | SI | Urine collection device used |
| Q22 | - |  |  | SI | Insertion notes |
| Q23 | - |  |  | SI | Inserted by |
| Q24 | - |  |  | SI | Assistant |
| Q25 | - |  |  | SI | Duration in situ |
| Q26 | - |  |  | SI | Due date for catheter change |
| Q27 | - |  |  | SI | Due date for catheter bag change |
| Q29 | - |  |  | SI | Removal date |
| Q30 | - |  |  | SI | Removal time |
| Q31 | - |  |  | SI | Removal reason |
| Q32 | - |  |  | SI | Removal outcome |
| Q33 | - |  |  | SI | Suprapubic catheter suture removed |
| Q34 | - |  |  | SI | Catheter tip sent for microbiology culture and sen... |
| Q35 | - |  |  | SI | Catheter removal notes |
| Q36 | - |  |  | SI | Removed by |
| Q37 | - |  |  | SI | Complications |
| Q38 | - |  |  | SI | Other complications |
| Q39 | - |  |  | SI | Complication notes |
| Q40 | - |  |  | SI | Other catheter material |
| Q41 | - |  |  | SI | Lot number |
| Q42 | - |  |  | SI | Inflation volume (mL) |
| Q43 | - |  |  | SI | Fluid used to inflate balloon |
| Q44 | - |  |  | SI | Date |
| Q45 | - |  |  | SI | Total duration catheter in situ |
| Q46 | - |  |  | SI | Duration since catheter insertion |
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