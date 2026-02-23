# SQLUser.OEC_ProsthetImplant

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROSTIMP_RowId | bigint | PK |  | NO | - |
| PROSTIMP_Code | varchar |  |  | NO | Code |
| PROSTIMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROSTIMP_CreatedDate | date |  |  | SI | Created Date |
| PROSTIMP_CreatedTime | time |  |  | SI | Created Time |
| PROSTIMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROSTIMP_DateFrom | date |  |  | SI | DateFrom |
| PROSTIMP_DateTo | date |  |  | SI | DateTo |
| PROSTIMP_Desc | varchar |  |  | NO | Description |
| PROSTIMP_Owner | varchar |  |  | SI | Owner |
| PROSTIMP_UpdatedDate | date |  |  | SI | Updated Date |
| PROSTIMP_UpdatedTime | time |  |  | SI | Updated Time |
| PROSTIMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Determines pediatric asthma severity based on phys... |
| Q02 | - |  |  | SI | Wheezing |
| Q03 | - |  |  | SI | Work of Breathing |
| Q04 | - |  |  | SI | (Use of accessory muscles, retractions). |
| Q05 | - |  |  | SI | (Ratio of expiration to inspiration). |
| Q06 | - |  |  | SI | Prolongation of Expiration |
| Q07 | - |  |  | SI | Score 0 - 1: PASS suggests asthma may be treatable... |
| Q08 | - |  |  | SI | Score 2 - 6: PASS suggests severe asthma, consider... |
| Q09 | - |  |  | SI | Wheezing |
| Q10 | - |  |  | SI | Work of Breathing |
| Q11 | - |  |  | SI | Prolongation of Expiration |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
| Q14 | - |  |  | SI | 0 - 1 |
| Q15 | - |  |  | SI | PASS suggests asthma may be treatable as outpatien... |
| Q16 | - |  |  | SI | 2 - 6 |
| Q17 | - |  |  | SI | PASS suggests severe asthma, consider admission to... |
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