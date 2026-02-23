# SQLUser.PAC_Station

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STTN_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Temperature |
| Q04 | - |  |  | SI | Tachypnea |
| Q05 | - |  |  | SI | Tachycardia |
| Q06 | - |  |  | SI | Increased capillary refill |
| Q07 | - |  |  | SI | Altered mental state |
| Q08 | - |  |  | SI | Comorbidities present |
| Q09 | - |  |  | SI | Score |
| Q10 | - |  |  | SI | Classification |
| Q11 | - |  |  | SI | ≥ 2 |
| Q12 | - |  |  | SI | Paediatric SEPSIS 6 is positive, therefore there i... |
| Q13 | - |  |  | SI | < 2 |
| Q14 | - |  |  | SI | Paediatric SEPSIS 6 is negative, there is not susp... |
| Q15 | - |  |  | SI | Paediatric sepsis is defined as greater than or eq... |
| Q16 | - |  |  | SI | confirmed or suspected invasive infection, and car... |
| Q17 | - |  |  | SI | ≥ 2: Paediatric SEPSIS 6 is positive, therefore th... |
| Q18 | - |  |  | SI | < 2: Paediatric SEPSIS 6 is negative, there is not... |
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
| STTN_Code | varchar |  |  | NO | Code |
| STTN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STTN_CreatedDate | date |  |  | SI | Created Date |
| STTN_CreatedTime | time |  |  | SI | Created Time |
| STTN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STTN_DateFrom | date |  |  | SI | Date From |
| STTN_DateTo | date |  |  | SI | Date To |
| STTN_Desc | varchar |  |  | NO | Description |
| STTN_Owner | varchar |  |  | SI | Owner |
| STTN_UpdatedDate | date |  |  | SI | Updated Date |
| STTN_UpdatedTime | time |  |  | SI | Updated Time |
| STTN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*