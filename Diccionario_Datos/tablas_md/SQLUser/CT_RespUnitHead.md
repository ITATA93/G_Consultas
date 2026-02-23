# SQLUser.CT_RespUnitHead

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RUH_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Completed at |
| Q04 | - |  |  | SI | Feeding |
| Q05 | - |  |  | SI | Bathing |
| Q06 | - |  |  | SI | Grooming |
| Q07 | - |  |  | SI | Dressing |
| Q08 | - |  |  | SI | Bowels |
| Q09 | - |  |  | SI | Bladder |
| Q10 | - |  |  | SI | Toilet use |
| Q11 | - |  |  | SI | Transfers (bed to chair and back) |
| Q12 | - |  |  | SI | Mobility (on level surfaces) |
| Q13 | - |  |  | SI | Stairs |
| Q14 | - |  |  | SI | Wheelchair |
| Q15 | - |  |  | SI | 0-24: Total dependency |
| Q16 | - |  |  | SI | 25-49: Severe dependency |
| Q17 | - |  |  | SI | 50-74: Moderate dependency |
| Q18 | - |  |  | SI | 75-90: Slight dependency |
| Q19 | - |  |  | SI | 91-99: Nearly independency |
| Q20 | - |  |  | SI | 100: Complete independency |
| Q21 | - |  |  | SI | The Barthel scale is a scale used to measure perfo... |
| Q22 | - |  |  | SI | General |
| Q23 | - |  |  | SI | • The Index should be used as a record of what a p... |
| Q24 | - |  |  | SI | • The main aim is to establish degree of independe... |
| Q25 | - |  |  | SI | • The need for supervision renders the patient not... |
| Q26 | - |  |  | SI | • A patient's performance should be established us... |
| Q27 | - |  |  | SI | friends / relatives, and nurses will be the usual ... |
| Q28 | - |  |  | SI | • Usually the performance over the preceding 24 – ... |
| Q29 | - |  |  | SI | • Unconscious patients should score '0' throughout... |
| Q30 | - |  |  | SI | • Middle categories imply that the patient supplie... |
| Q31 | - |  |  | SI | • Use of aids to be independent is allowed. |
| Q32 | - |  |  | SI | Wheelchair use must be scored only if mobility sco... |
| Q33 | - |  |  | SI | Score |
| Q34 | - |  |  | SI | Classification |
| Q35 | - |  |  | SI | 0-24 |
| Q36 | - |  |  | SI | Total dependency |
| Q37 | - |  |  | SI | 25-49 |
| Q38 | - |  |  | SI | Severe dependency |
| Q39 | - |  |  | SI | 50-74 |
| Q40 | - |  |  | SI | Moderate dependency |
| Q41 | - |  |  | SI | 75-90 |
| Q42 | - |  |  | SI | Slight dependency |
| Q43 | - |  |  | SI | 91-99 |
| Q44 | - |  |  | SI | Nearly independency	 |
| Q45 | - |  |  | SI | 100 |
| Q46 | - |  |  | SI | Complete independency |
| Q47 | - |  |  | SI | 0-25: Total dependency |
| Q48 | - |  |  | SI | 25-49: Severe dependency |
| Q49 | - |  |  | SI | 50-74: Moderate dependency |
| Q50 | - |  |  | SI | 75-90: Slight dependency |
| Q51 | - |  |  | SI | 91-99: Nearly independency |
| Q52 | - |  |  | SI | 100: Complete independency |
| Q53 | - |  |  | SI | The Barthel scale is a scale used to measure perfo... |
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
| RUH_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| RUH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RUH_CreatedDate | date |  |  | SI | Created Date |
| RUH_CreatedTime | time |  |  | SI | Created Time |
| RUH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RUH_DateFrom | date |  |  | SI | DateFrom |
| RUH_DateTo | date |  |  | SI | DateTo |
| RUH_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| RUH_Owner | varchar |  |  | SI | Owner |
| RUH_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| RUH_UpdatedDate | date |  |  | SI | Updated Date |
| RUH_UpdatedTime | time |  |  | SI | Updated Time |
| RUH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*