# SQLUser.PAC_CauseOfInjury

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INJU_RowId | bigint | PK |  | NO | - |
| ChildQ24DR | - |  |  | SI | Child Reference: Balloon details |
| INJU_Code | varchar |  |  | NO | Code |
| INJU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INJU_CreatedDate | date |  |  | SI | Created Date |
| INJU_CreatedTime | time |  |  | SI | Created Time |
| INJU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INJU_DateFrom | date |  |  | SI | Date From |
| INJU_DateTo | date |  |  | SI | Date To |
| INJU_Desc | varchar |  |  | NO | Description |
| INJU_NationalCode | varchar |  |  | SI | National Code |
| INJU_Owner | varchar |  |  | SI | Owner |
| INJU_UpdatedDate | date |  |  | SI | Updated Date |
| INJU_UpdatedTime | time |  |  | SI | Updated Time |
| INJU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of procedure |
| Q04 | - |  |  | SI | Care provider 1 |
| Q05 | - |  |  | SI | Care provider 2 |
| Q06 | - |  |  | SI | Care provider 3 |
| Q07 | - |  |  | SI | Access requiring procedure |
| Q08 | - |  |  | SI | Laterality |
| Q09 | - |  |  | SI | Access location |
| Q10 | - |  |  | SI | Other access location |
| Q11 | - |  |  | SI | Procedure |
| Q12 | - |  |  | SI | Procedure code |
| Q13 | - |  |  | SI | Anaesthesia |
| Q14 | - |  |  | SI | Type of contrast used |
| Q15 | - |  |  | SI | Access to fistula |
| Q16 | - |  |  | SI | Sheath size |
| Q17 | - |  |  | SI | Fistulogram stenosis |
| Q18 | - |  |  | SI | Fistulogram - Anastomosis status |
| Q19 | - |  |  | SI | Fistulogram - Peripheral check |
| Q20 | - |  |  | SI | Fistulogram - Central check |
| Q21 | - |  |  | SI | Fistulogram notes |
| Q22 | - |  |  | SI | Flow |
| Q23 | - |  |  | SI | Stenting - Fistuloplasty |
| Q25 | - |  |  | SI | IV heparin dose required |
| Q26 | - |  |  | SI | Heparin comments |
| Q27 | - |  |  | SI | Procedure outcome |
| Q28 | - |  |  | SI | Complications |
| Q29 | - |  |  | SI | Procedure notes |
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