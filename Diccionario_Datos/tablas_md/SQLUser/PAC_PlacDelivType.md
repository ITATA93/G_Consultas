# SQLUser.PAC_PlacDelivType

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLDT_RowId | bigint | PK |  | NO | - |
| PLDT_Code | varchar |  |  | NO | Code |
| PLDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLDT_CreatedDate | date |  |  | SI | Created Date |
| PLDT_CreatedTime | time |  |  | SI | Created Time |
| PLDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLDT_DateFrom | date |  |  | SI | Date From |
| PLDT_DateTo | date |  |  | SI | Date To |
| PLDT_Desc | varchar |  |  | NO | Description |
| PLDT_NationalCode | varchar |  |  | SI | National Code |
| PLDT_Owner | varchar |  |  | SI | Owner |
| PLDT_UpdatedDate | date |  |  | SI | Updated Date |
| PLDT_UpdatedTime | time |  |  | SI | Updated Time |
| PLDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Has allergy status been checked? |
| Q10 | - |  |  | SI | Are there any individual patient issues? |
| Q11 | - |  |  | SI | If Yes, please detail |
| Q12 | - |  |  | SI | Additional comments |
| Q13 | - |  |  | SI | Date |
| Q14 | - |  |  | SI | Time |
| Q2 | - |  |  | SI | Patient has given consent to procedure |
| Q3 | - |  |  | SI | Operation site verified by patient against consent |
| Q4 | - |  |  | SI | Operation site is prepared (if applicable) |
| Q5 | - |  |  | SI | All jewellery removed from operative limb (if appl... |
| Q6 | - |  |  | SI | Any implants in situ? (e.g. cardiac pacemaker) |
| Q7 | - |  |  | SI | If Yes, please detail |
| Q8 | - |  |  | SI | Confirm patient's temperature is 36 degrees or abo... |
| Q9 | - |  |  | SI | Observations checked and within normal limits? |
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