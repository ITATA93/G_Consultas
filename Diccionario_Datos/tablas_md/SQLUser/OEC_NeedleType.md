# SQLUser.OEC_NeedleType

**Schema:** SQLUser
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NEDT_RowId | bigint | PK |  | NO | - |
| NEDT_Code | varchar |  |  | NO | Code |
| NEDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NEDT_CreatedDate | date |  |  | SI | Created Date |
| NEDT_CreatedTime | time |  |  | SI | Created Time |
| NEDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NEDT_DateFrom | date |  |  | SI | Date From |
| NEDT_DateTo | date |  |  | SI | Date To |
| NEDT_Desc | varchar |  |  | NO | Description |
| NEDT_NeuroAxial | varchar |  |  | SI | Neuro Axial |
| NEDT_Orbital | varchar |  |  | SI | Orbital |
| NEDT_Owner | varchar |  |  | SI | Owner |
| NEDT_UpdatedDate | date |  |  | SI | Updated Date |
| NEDT_UpdatedTime | time |  |  | SI | Updated Time |
| NEDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Visual Acuity - Uncorrected |
| Q02 | - |  |  | SI | Right eye |
| Q03 | - |  |  | SI | Left eye |
| Q04 | - |  |  | SI | Both eyes |
| Q05 | - |  |  | SI | VA-Dt |
| Q06 | - |  |  | SI | Va-dt2 |
| Q07 | - |  |  | SI | Va-dt3 |
| Q08 | - |  |  | SI | VA-PH |
| Q09 | - |  |  | SI | VA-ph2 |
| Q10 | - |  |  | SI | vA-Ph3 |
| Q11 | - |  |  | SI | VA-Nr |
| Q12 | - |  |  | SI | va-nr2 |
| Q13 | - |  |  | SI | va-nr3 |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Visual Acuity - Corrected |
| Q16 | - |  |  | SI | Right eye |
| Q17 | - |  |  | SI | Left eye |
| Q18 | - |  |  | SI | Sph |
| Q19 | - |  |  | SI | sph2 |
| Q20 | - |  |  | SI | Cyl |
| Q21 | - |  |  | SI | Cyl2 |
| Q22 | - |  |  | SI | Axis |
| Q23 | - |  |  | SI | axis2 |
| Q24 | - |  |  | SI | Add |
| Q25 | - |  |  | SI | VA-Dt |
| Q26 | - |  |  | SI | VA-dt2 |
| Q27 | - |  |  | SI | Va-dt3 |
| Q28 | - |  |  | SI | Both eyes |
| Q29 | - |  |  | SI | VA-Nr |
| Q30 | - |  |  | SI | VA-Nr2 |
| Q31 | - |  |  | SI | VA-Nr3 |
| Q32 | - |  |  | SI | Notes |
| Q33 | - |  |  | SI | Eye dilated? |
| Q36 | - |  |  | SI | This shows the visual acuity recordings taken by n... |
| Q361 | - |  |  | SI | Pinhole test |
| Q37 | - |  |  | SI | Previous values are retained here, to create a new... |
| Q371 | - |  |  | SI | Distance |
| Q38 | - |  |  | SI | Distance |
| Q39 | - |  |  | SI | Near |
| Q40 | - |  |  | SI | Near |
| Q41 | - |  |  | SI | Near |
| Q42 | - |  |  | SI | Va-NR-ph1 |
| Q43 | - |  |  | SI | Va-NR-ph2 |
| Q44 | - |  |  | SI | Va-NR-ph3 |
| Q45 | - |  |  | SI | Notes |
| Q46 | - |  |  | SI | Distance |
| Q47 | - |  |  | SI | Right eye |
| Q48 | - |  |  | SI | Left eye |
| Q49 | - |  |  | SI | Both eyes |
| Q50 | - |  |  | SI | Date |
| Q51 | - |  |  | SI | Time |
| Q52 | - |  |  | SI | Distance |
| Q53 | - |  |  | SI | Distance |
| Q54 | - |  |  | SI | Distance |
| Q55 | - |  |  | SI | Distance |
| Q56 | - |  |  | SI | Distance |
| Q57 | - |  |  | SI | Distance |
| Q58 | - |  |  | SI | Distance |
| Q59 | - |  |  | SI | Distance |
| Q60 | - |  |  | SI | Distance |
| Q61 | - |  |  | SI | Near |
| Q62 | - |  |  | SI | Near |
| Q63 | - |  |  | SI | Near |
| Q64 | - |  |  | SI | Near |
| Q65 | - |  |  | SI | Near |
| Q66 | - |  |  | SI | Near |
| Q67 | - |  |  | SI | Near |
| Q68 | - |  |  | SI | Near |
| Q69 | - |  |  | SI | Near |
| Q70 | - |  |  | SI | Notes |
| Q71 | - |  |  | SI | Notes |
| Q72 | - |  |  | SI | Notes |
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