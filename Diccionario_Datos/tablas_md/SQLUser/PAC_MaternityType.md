# SQLUser.PAC_MaternityType

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MAT_RowId | bigint | PK |  | NO | - |
| MAT_Code | varchar |  |  | NO | Code |
| MAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MAT_CreatedDate | date |  |  | SI | Created Date |
| MAT_CreatedTime | time |  |  | SI | Created Time |
| MAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MAT_DateFrom | date |  |  | SI | Date From |
| MAT_DateTo | date |  |  | SI | Date To |
| MAT_Desc | varchar |  |  | NO | Description |
| MAT_Owner | varchar |  |  | SI | Owner |
| MAT_UpdatedDate | date |  |  | SI | Updated Date |
| MAT_UpdatedTime | time |  |  | SI | Updated Time |
| MAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Chest pain |
| Q04 | - |  |  | SI | Feeling tense |
| Q05 | - |  |  | SI | Blurred vision |
| Q06 | - |  |  | SI | Dizzy spells |
| Q07 | - |  |  | SI | Feeling confused |
| Q08 | - |  |  | SI | Faster or deeper breathing |
| Q09 | - |  |  | SI | Short of breath |
| Q10 | - |  |  | SI | Tight feelings in chest |
| Q11 | - |  |  | SI | Bloated feeling in stomach |
| Q12 | - |  |  | SI | Tingling fingers |
| Q13 | - |  |  | SI | Unable to breath deeply |
| Q14 | - |  |  | SI | Stiff fingers or arms |
| Q15 | - |  |  | SI | Tight feelings round mouth |
| Q16 | - |  |  | SI | Cold hands or feet |
| Q17 | - |  |  | SI | Palpitations |
| Q18 | - |  |  | SI | Feeling of anxiety |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 - 64 |
| Q22 | - |  |  | SI | A score less than 23 indicates hyperventilation sy... |
| Q23 | - |  |  | SI | 0 - 64: A score less than 23 indicates hyperventil... |
| Q24 | - |  |  | SI | The Nijmegen questionnaire gives a broad view of s... |
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