# SQLUser.PAC_ManagementOfAbortion

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MABORT_RowId | bigint | PK |  | NO | - |
| MABORT_Code | varchar |  |  | NO | Code |
| MABORT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MABORT_CreatedDate | date |  |  | SI | Created Date |
| MABORT_CreatedTime | time |  |  | SI | Created Time |
| MABORT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MABORT_DateFrom | date |  |  | SI | Date From |
| MABORT_DateTo | date |  |  | SI | Date To |
| MABORT_Desc | varchar |  |  | NO | Description |
| MABORT_NationalCode | varchar |  |  | SI | National code |
| MABORT_Owner | varchar |  |  | SI | Owner |
| MABORT_UpdatedDate | date |  |  | SI | Updated Date |
| MABORT_UpdatedTime | time |  |  | SI | Updated Time |
| MABORT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | Sex |
| Q05 | - |  |  | SI | Admission haemoglobin |
| Q06 | - |  |  | SI | Abbreviated Mental Test Score (AMTS-10) |
| Q07 | - |  |  | SI | Living in an institution |
| Q08 | - |  |  | SI | Number of co-morbidities |
| Q09 | - |  |  | SI | Active malignancy within 20 years |
| Q10 | - |  |  | SI | Provenance |
| Q11 | - |  |  | SI | 1. Maxwell MJ, Moran CG, Moppett IK. Development a... |
| Q12 | - |  |  | SI | 2. Moppett IK, Parker M, Griffiths R, Bowers T, Wh... |
| Q13 | - |  |  | SI | References |
| Q14 | - |  |  | SI | Estimated 30-day mortality |
| Q15 | - |  |  | SI | The Nottingham Hip Fracture Score (NHFS) (Revised,... |
| Q16 | - |  |  | SI | % |
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