# SQLUser.PAC_AbortionReason

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ABOR_RowId | bigint | PK |  | NO | - |
| ABOR_Code | varchar |  |  | NO | Code |
| ABOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ABOR_CreatedDate | date |  |  | SI | Created Date |
| ABOR_CreatedTime | time |  |  | SI | Created Time |
| ABOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ABOR_DateFrom | date |  |  | SI | DateFrom |
| ABOR_DateTo | date |  |  | SI | DateTo |
| ABOR_Desc | varchar |  |  | NO | Description |
| ABOR_Owner | varchar |  |  | SI | Owner |
| ABOR_UpdatedDate | date |  |  | SI | Updated Date |
| ABOR_UpdatedTime | time |  |  | SI | Updated Time |
| ABOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Assessment Date |
| Q02 | - |  |  | SI | Assessment Time |
| Q03 | - |  |  | SI | Abdomen |
| Q03ObsDR | - |  |  | SI | Abdomen DR |
| Q04 | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Vulva |
| Q05ObsDR | - |  |  | SI | Vulva DR |
| Q06 | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Vagina |
| Q07ObsDR | - |  |  | SI | Vagina DR |
| Q08 | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Cervix |
| Q09ObsDR | - |  |  | SI | Cervix DR |
| Q10 | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Uterus position |
| Q11ObsDR | - |  |  | SI | Uterus position DR |
| Q12 | - |  |  | SI | Note |
| Q13 | - |  |  | SI | Uterus size |
| Q13ObsDR | - |  |  | SI | Uterus size DR |
| Q14 | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Prolapse |
| Q15ObsDR | - |  |  | SI | Prolapse DR |
| Q16 | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Adnexa |
| Q17ObsDR | - |  |  | SI | Adnexa DR |
| Q18 | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Note (Other) |
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