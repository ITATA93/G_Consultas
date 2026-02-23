# SQLUser.PAC_SourceOfAddition

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SADD_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Suprasternal retractions present	 |
| Q04 | - |  |  | SI | Scalene muscle contractions present	 |
| Q05 | - |  |  | SI | Air entry - If asymmetry, use the most severely af... |
| Q06 | - |  |  | SI | Wheezing -  If asymmetry, use the two most severel... |
| Q07 | - |  |  | SI | O₂ saturation |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Classification	 |
| Q10 | - |  |  | SI | 0-3 |
| Q11 | - |  |  | SI | 4-7 |
| Q12 | - |  |  | SI | 8-12 |
| Q13 | - |  |  | SI | Mild Asthma |
| Q14 | - |  |  | SI | Moderate Asthma |
| Q15 | - |  |  | SI | Severe Asthma |
| Q16 | - |  |  | SI | Pediatric Respiratory Assessment Measure (PRAM) fo... |
| Q17 | - |  |  | SI | Pediatric Respiratory Assessment Measure (PRAM) |
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
| SADD_Code | varchar |  |  | NO | Code |
| SADD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SADD_CreatedDate | date |  |  | SI | Created Date |
| SADD_CreatedTime | time |  |  | SI | Created Time |
| SADD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SADD_DateFrom | date |  |  | SI | Date From |
| SADD_DateTo | date |  |  | SI | Date To |
| SADD_Desc | varchar |  |  | NO | Description |
| SADD_NationCode | varchar |  |  | SI | National Code |
| SADD_Owner | varchar |  |  | SI | Owner |
| SADD_RefType | varchar |  |  | SI | Referrer Type |
| SADD_UpdatedDate | date |  |  | SI | Updated Date |
| SADD_UpdatedTime | time |  |  | SI | Updated Time |
| SADD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*