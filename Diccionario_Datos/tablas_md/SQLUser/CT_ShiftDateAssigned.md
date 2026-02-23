# SQLUser.CT_ShiftDateAssigned

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DATE_ParRef | varchar | PK |  | NO | CT_Shift Parent Reference |
| DATE_Childsub | double |  |  | NO | Childsub |
| DATE_Count | double |  |  | SI | Count |
| DATE_CreatedDate | date |  |  | SI | Created Date |
| DATE_CreatedTime | time |  |  | SI | Created Time |
| DATE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DATE_Date | date |  |  | SI | Date |
| DATE_RowId | varchar |  |  | NO | - |
| DATE_UpdatedDate | date |  |  | SI | Updated Date |
| DATE_UpdatedTime | time |  |  | SI | Updated Time |
| DATE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Cervical rotation (mean of left & right) |
| Q02 | - |  |  | SI | Tragus to wall (mean of left & right) |
| Q03 | - |  |  | SI | Lumbar side flexion (mean of left & right) |
| Q04 | - |  |  | SI | Lumbar flexion (modified Schober's) |
| Q05 | - |  |  | SI | Intermalleolar distance |
| Q06 | - |  |  | SI | 10 - Severe limitation of movement / 0 - Mild limi... |
| Q07 | - |  |  | SI | The higher the BASMI-2 score the more severe the l... |
| Q08 | - |  |  | SI | BASMI-2 (Bath Ankylosing Spondylitis Metrology Ind... |
| Q09 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Time |
| Q11 | - |  |  | SI | 1. Jenkinson TR, Mallorie PA, Whitelock HC, Kenned... |
| Q12 | - |  |  | SI | 2. Heijde D van der, Landewé R, Feldtkeller E. Pro... |
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