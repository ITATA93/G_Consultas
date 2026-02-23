# questionnaire.QTCUCIC

> Urinary Catheter Insertion and Care

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Urinary Catheter Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient identified |
| Q04 | varchar |  |  | SI | Informed consent obtained from patient? |
| Q05 | varchar |  |  | SI | Pre-procedure checklist |
| Q06 | varchar |  |  | SI | Pre-procedure notes |
| Q07 | varchar |  |  | SI | Insertion status |
| Q08 | date |  |  | SI | Insertion date |
| Q09 | time |  |  | SI | Insertion time |
| Q10 | varchar |  |  | SI | Catheter type |
| Q10ObsDR | varchar |  | FK | SI | Catheter type DR |
| Q11 | varchar |  |  | SI | Insertion reason |
| Q12 | varchar |  |  | SI | Other insertion reason |
| Q13 | varchar |  |  | SI | Catheter material |
| Q13ObsDR | varchar |  | FK | SI | Catheter material DR |
| Q14 | varchar |  |  | SI | Urinary catheter size (Fr) |
| Q14ObsDR | varchar |  | FK | SI | Urinary catheter size (Fr) DR |
| Q15 | varchar |  |  | SI | Patient location at time of insertion |
| Q16 | numeric |  |  | SI | Number of attempts |
| Q17 | numeric |  |  | SI | Total catheter balloon capacity (mL) |
| Q18 | varchar |  |  | SI | Fluid used to inflate balloon and inflation volume... |
| Q19 | varchar |  |  | SI | Procedure outcome |
| Q20 | varchar |  |  | SI | Post-insertion checklist |
| Q21 | varchar |  |  | SI | Urine collection device used |
| Q22 | varchar |  |  | SI | Insertion notes |
| Q23 | varchar |  |  | SI | Inserted by |
| Q24 | varchar |  |  | SI | Assistant |
| Q25 | varchar |  |  | SI | Duration in situ |
| Q26 | date |  |  | SI | Due date for catheter change |
| Q27 | date |  |  | SI | Due date for catheter bag change |
| Q29 | date |  |  | SI | Removal date |
| Q30 | time |  |  | SI | Removal time |
| Q31 | varchar |  |  | SI |  Removal reason |
| Q32 | varchar |  |  | SI | Removal outcome |
| Q33 | varchar |  |  | SI | Suprapubic catheter suture removed |
| Q34 | varchar |  |  | SI | Catheter tip sent for microbiology culture and sen... |
| Q35 | varchar |  |  | SI | Catheter removal notes |
| Q36 | varchar |  |  | SI | Removed by |
| Q37 | varchar |  |  | SI | Complications |
| Q38 | varchar |  |  | SI | Other complications |
| Q39 | varchar |  |  | SI | Complication notes |
| Q40 | varchar |  |  | SI | Other catheter material |
| Q41 | varchar |  |  | SI | Lot number |
| Q42 | numeric |  |  | SI | Inflation volume (mL) |
| Q43 | varchar |  |  | SI | Fluid used to inflate balloon |
| Q44 | varchar |  |  | SI | Date |
| Q45 | varchar |  |  | SI | Total duration catheter in situ |
| Q46 | varchar |  |  | SI | Duration since catheter insertion |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*