# SQLUser.PAC_FreqAttendConcernLev

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FCL_RowId | bigint | PK |  | NO | - |
| FCL_Code | varchar |  |  | NO | Code |
| FCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FCL_CreatedDate | date |  |  | SI | Created Date |
| FCL_CreatedTime | time |  |  | SI | Created Time |
| FCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FCL_DateFrom | date |  |  | SI | DateFrom |
| FCL_DateTo | date |  |  | SI | DateTo |
| FCL_Desc | varchar |  |  | NO | Description |
| FCL_Owner | varchar |  |  | SI | Owner |
| FCL_UpdatedDate | date |  |  | SI | Updated Date |
| FCL_UpdatedTime | time |  |  | SI | Updated Time |
| FCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Motor dysfunction score of the upper extremities |
| Q04 | - |  |  | SI | Motor dysfunction score of the lower extremities |
| Q05 | - |  |  | SI | Sensation |
| Q06 | - |  |  | SI | Sphincter dysfunction |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | 18 |
| Q10 | - |  |  | SI | No myelopathy |
| Q11 | - |  |  | SI | 15 - 17 |
| Q12 | - |  |  | SI | Mild myelopathy |
| Q13 | - |  |  | SI | 12 - 14 |
| Q14 | - |  |  | SI | Moderate myelopathy |
| Q15 | - |  |  | SI | 0 - 11 |
| Q16 | - |  |  | SI | Severe myelopathy |
| Q17 | - |  |  | SI | 18: No myelopathy |
| Q18 | - |  |  | SI | 15 - 17: Mild myelopathy |
| Q19 | - |  |  | SI | 12 - 14: Moderate myelopathy |
| Q20 | - |  |  | SI | 0 - 11: Severe myelopathy |
| Q21 | - |  |  | SI | The modified Japanese Orthopaedic Association (mJO... |
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