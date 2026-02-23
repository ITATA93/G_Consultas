# SQLUser.PAC_Toileting

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOIL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | I have reviewed updated physician's order and rela... |
| Q04 | - |  |  | SI | General appearance |
| Q05 | - |  |  | SI | Level of consciousness |
| Q05ObsDR | - |  |  | SI | Level of consciousness DR |
| Q06 | - |  |  | SI | Range of motion examination |
| Q07 | - |  |  | SI | Range of motion summary |
| Q08 | - |  |  | SI | Accessory movement examination |
| Q09 | - |  |  | SI | Accessory movement summary |
| Q10 | - |  |  | SI | Palpation examination |
| Q11 | - |  |  | SI | Palpation summary |
| Q12 | - |  |  | SI | Muscle strength examination |
| Q13 | - |  |  | SI | Muscle strength summary |
| Q14 | - |  |  | SI | Rolling |
| Q14ObsDR | - |  |  | SI | Rolling DR |
| Q15 | - |  |  | SI | Come to sit |
| Q15ObsDR | - |  |  | SI | Come to sit  DR |
| Q16 | - |  |  | SI | Come to stand |
| Q16ObsDR | - |  |  | SI | Come to stand  DR |
| Q17 | - |  |  | SI | Ambulatory status |
| Q17ObsDR | - |  |  | SI | Ambulatory status DR |
| Q18 | - |  |  | SI | Transferring |
| Q18ObsDR | - |  |  | SI | Transferring DR |
| Q19 | - |  |  | SI | Sensation examination |
| Q20 | - |  |  | SI | Sensation summary |
| Q21 | - |  |  | SI | Other examination summary |
| Q22 | - |  |  | SI | To document specific examinations, please complete... |
| Q23 | - |  |  | SI | Examples: |
| Q24 | - |  |  | SI | Range of Motion |
| Q25 | - |  |  | SI | Manual Muscle Testing |
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
| TOIL_Code | varchar |  |  | NO | Code |
| TOIL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TOIL_CreatedDate | date |  |  | SI | Created Date |
| TOIL_CreatedTime | time |  |  | SI | Created Time |
| TOIL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOIL_DateFrom | date |  |  | SI | Date From |
| TOIL_DateTo | date |  |  | SI | Date To |
| TOIL_Desc | varchar |  |  | NO | Description |
| TOIL_NationCode | varchar |  |  | SI | National Code |
| TOIL_NumericVal | double |  |  | SI | Numeric Value |
| TOIL_Owner | varchar |  |  | SI | Owner |
| TOIL_UpdatedDate | date |  |  | SI | Updated Date |
| TOIL_UpdatedTime | time |  |  | SI | Updated Time |
| TOIL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*