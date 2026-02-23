# SQLUser.PAC_BreastNipple

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BRE_RowId | bigint | PK |  | NO | - |
| BRE_Code | varchar |  |  | NO | Code |
| BRE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BRE_CreatedDate | date |  |  | SI | Created Date |
| BRE_CreatedTime | time |  |  | SI | Created Time |
| BRE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BRE_DateFrom | date |  |  | SI | Date From |
| BRE_DateTo | date |  |  | SI | Date To |
| BRE_Desc | varchar |  |  | NO | Description |
| BRE_Owner | varchar |  |  | SI | Owner |
| BRE_UpdatedDate | date |  |  | SI | Updated Date |
| BRE_UpdatedTime | time |  |  | SI | Updated Time |
| BRE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ18DR | - |  |  | SI | Child Reference: Cervical ripening details and ind... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Induction process explained and verbal consent obt... |
| Q04 | - |  |  | SI | Gravida |
| Q05 | - |  |  | SI | Para |
| Q06 | - |  |  | SI | Gestation |
| Q07 | - |  |  | SI | Weeks |
| Q08 | - |  |  | SI | Gestation (days) |
| Q09 | - |  |  | SI | Days |
| Q10 | - |  |  | SI | Induction indicator |
| Q11 | - |  |  | SI | Induction notes |
| Q12 | - |  |  | SI | Initial Vaginal Examination / Modified Bishop Scor... |
| Q14 | - |  |  | SI | Plurality |
| Q15 | - |  |  | SI | Presentation Fetus 1 |
| Q15ObsDR | - |  |  | SI | Presentation Fetus 1 DR |
| Q16 | - |  |  | SI | Fetal presentation confirmed by |
| Q17 | - |  |  | SI | Cervical Ripening and Induction |
| Q19 | - |  |  | SI | Induction management notes |
| Q20 | - |  |  | SI | Commence partogram for continuation of the inducti... |
| Q21 | - |  |  | SI | Presentation Fetus 2 |
| Q21ObsDR | - |  |  | SI | Presentation Fetus 2 DR |
| Q22 | - |  |  | SI | Presentation Fetus 3 |
| Q22ObsDR | - |  |  | SI | Presentation Fetus 3 DR |
| Q23 | - |  |  | SI | Induction indicator |
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