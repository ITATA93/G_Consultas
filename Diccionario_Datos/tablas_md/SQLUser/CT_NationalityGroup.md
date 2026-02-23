# SQLUser.CT_NationalityGroup

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NATGRP_RowId | bigint | PK |  | NO | - |
| ChildQ26DR | - |  |  | SI | Child Reference: Arterial line assessment |
| NATGRP_Code | varchar |  |  | NO | Code |
| NATGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NATGRP_CreatedDate | date |  |  | SI | Created Date |
| NATGRP_CreatedTime | time |  |  | SI | Created Time |
| NATGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NATGRP_DateFrom | date |  |  | SI | Date From |
| NATGRP_DateTo | date |  |  | SI | Date To |
| NATGRP_Desc | varchar |  |  | NO | Description |
| NATGRP_Owner | varchar |  |  | SI | Owner |
| NATGRP_UpdatedDate | date |  |  | SI | Updated Date |
| NATGRP_UpdatedTime | time |  |  | SI | Updated Time |
| NATGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Arterial line present |
| Q06 | - |  |  | SI | Insertion time |
| Q07 | - |  |  | SI | Total days of insertion |
| Q08 | - |  |  | SI | Procedure type |
| Q09 | - |  |  | SI | Catheter type |
| Q10 | - |  |  | SI | Laterality |
| Q11 | - |  |  | SI | Site |
| Q12 | - |  |  | SI | Size |
| Q13 | - |  |  | SI | Length |
| Q14 | - |  |  | SI | Reason for insertion |
| Q15 | - |  |  | SI | Patient identified |
| Q16 | - |  |  | SI | Insertion unit |
| Q17 | - |  |  | SI | Performing provider |
| Q18 | - |  |  | SI | Assisting in insertion |
| Q19 | - |  |  | SI | Procedure preparation |
| Q20 | - |  |  | SI | Sterile field maintained |
| Q21 | - |  |  | SI | Maximal sterile barrier precautions compliance |
| Q22 | - |  |  | SI | Non - compliant maximal sterile barrier precaution... |
| Q23 | - |  |  | SI | Procedure result |
| Q24 | - |  |  | SI | Number of attempts |
| Q25 | - |  |  | SI | Comment |
| Q28 | - |  |  | SI | Collateral flow assured |
| Q29 | - |  |  | SI | Allen test |
| Q30 | - |  |  | SI | Discontinue date and time |
| Q31 | - |  |  | SI | Discontinue time |
| Q32 | - |  |  | SI | Care provider discontinued the line |
| Q33 | - |  |  | SI | Removal reason |
| Q34 | - |  |  | SI | Unexpected events |
| Q35 | - |  |  | SI | Removal result |
| Q36 | - |  |  | SI | Removal result |
| Q37 | - |  |  | SI | Direct pressure duration (Minutes) |
| Q38 | - |  |  | SI | Insertion date and time |
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