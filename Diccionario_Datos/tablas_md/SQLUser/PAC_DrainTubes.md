# SQLUser.PAC_DrainTubes

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRT_RowId | bigint | PK |  | NO | - |
| DRT_Code | varchar |  |  | NO | Code |
| DRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRT_CreatedDate | date |  |  | SI | Created Date |
| DRT_CreatedTime | time |  |  | SI | Created Time |
| DRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRT_DateFrom | date |  |  | SI | Date From |
| DRT_DateTo | date |  |  | SI | Date To |
| DRT_Desc | varchar |  |  | NO | Description |
| DRT_Owner | varchar |  |  | SI | Owner |
| DRT_UpdatedDate | date |  |  | SI | Updated Date |
| DRT_UpdatedTime | time |  |  | SI | Updated Time |
| DRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Stool frequency |
| Q02 | - |  |  | SI | Rectal bleeding |
| Q03 | - |  |  | SI | 3 points requires patients to have ≥50% of |
| Q04 | - |  |  | SI | bowel movement |
| Q05 | - |  |  | SI | with visible blood AND ≥1 |
| Q06 | - |  |  | SI | bowel movement |
| Q07 | - |  |  | SI | with blood alone. |
| Q08 | - |  |  | SI | Mucosal appearance at endoscopy |
| Q09 | - |  |  | SI | Physician rating of disease activity |
| Q10 | - |  |  | SI | 3 points requires patients to have ≥50% of |
| Q11 | - |  |  | SI | bowel movement |
| Q12 | - |  |  | SI | with visible blood AND ≥ 1 |
| Q13 | - |  |  | SI | bowel movement |
| Q14 | - |  |  | SI | with blood alone. |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | 0 - 12 |
| Q18 | - |  |  | SI | The higher the score, the more severe the case of ... |
| Q19 | - |  |  | SI | 0 - 12: The higher the score, the more severe the ... |
| Q20 | - |  |  | SI | Date |
| Q21 | - |  |  | SI | Time |
| Q22 | - |  |  | SI | The Mayo Score for ulcerative colitis disease acti... |
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