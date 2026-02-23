# SQLUser.PAC_TriageSymptoms

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRISYM_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of access |
| Q04 | - |  |  | SI | Access location |
| Q05 | - |  |  | SI | Other access location notes |
| Q06 | - |  |  | SI | Laterality |
| Q07 | - |  |  | SI | Reason for review - Fistula / Graft |
| Q08 | - |  |  | SI | Other reason for review notes - Fistula / Graft&nb... |
| Q09 | - |  |  | SI | Reason for review - Haemodialysis catheter |
| Q10 | - |  |  | SI | Other reason for review - HD catheter notes |
| Q11 | - |  |  | SI | Assessment findings |
| Q12 | - |  |  | SI | Intervention required |
| Q13 | - |  |  | SI | Other intervention |
| Q14 | - |  |  | SI | Notes |
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
| TRISYM_AgeFrom | double |  |  | SI | Age Restriction From (Years) |
| TRISYM_AgeTo | double |  |  | SI | Age Restriction To (Years) |
| TRISYM_Category_DR | bigint |  | FK | SI | Triage Symptom Category |
| TRISYM_Code | varchar |  |  | NO | Code |
| TRISYM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRISYM_CreatedDate | date |  |  | SI | Created Date |
| TRISYM_CreatedTime | time |  |  | SI | Created Time |
| TRISYM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRISYM_DateFrom | date |  |  | SI | Date From |
| TRISYM_DateTo | date |  |  | SI | Date To |
| TRISYM_Desc | varchar |  |  | NO | Description |
| TRISYM_Details | varchar |  |  | SI | Triage Symptoms Details |
| TRISYM_Owner | varchar |  |  | SI | Owner |
| TRISYM_Subregion_DR | bigint |  | FK | SI | Subregion  |
| TRISYM_UpdatedDate | date |  |  | SI | Updated Date |
| TRISYM_UpdatedTime | time |  |  | SI | Updated Time |
| TRISYM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*