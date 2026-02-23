# SQLUser.ORC_SurfaceLandmark

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SURLAN_RowId | bigint | PK |  | NO | - |
| Q02 | - |  |  | SI | Body fat	 |
| Q03 | - |  |  | SI | Fat mass	 |
| Q04 | - |  |  | SI | Obesity related comorbidities	 |
| Q05 | - |  |  | SI | Diastolic BP	 |
| Q05ObsDR | - |  |  | SI | Diastolic BP	 DR |
| Q06 | - |  |  | SI | Systolic BP	 |
| Q06ObsDR | - |  |  | SI | Systolic BP	 DR |
| Q07 | - |  |  | SI | Past weight history	 |
| Q08 | - |  |  | SI | Name of slimming pills	 |
| Q09 | - |  |  | SI | Age of onset of weight problems	 |
| Q10 | - |  |  | SI | Eating habits	 |
| Q11 | - |  |  | SI | Binge eater	 |
| Q12 | - |  |  | SI | Comfort eater	 |
| Q13 | - |  |  | SI | Questionnaire received back from the patient	 |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Lying Systolic |
| Q15ObsDR | - |  |  | SI | Lying Systolic DR |
| Q16 | - |  |  | SI | Lying Diastolic |
| Q16ObsDR | - |  |  | SI | Lying Diastolic DR |
| Q17 | - |  |  | SI | Standing Systolic |
| Q17ObsDR | - |  |  | SI | Standing Systolic DR |
| Q18 | - |  |  | SI | Standing Diastolic |
| Q18ObsDR | - |  |  | SI | Standing Diastolic DR |
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
| SURLAN_Code | varchar |  |  | NO | Code |
| SURLAN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SURLAN_CreatedDate | date |  |  | SI | Created Date |
| SURLAN_CreatedTime | time |  |  | SI | Created Time |
| SURLAN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SURLAN_DateFrom | date |  |  | SI | Date From |
| SURLAN_DateTo | date |  |  | SI | Date To |
| SURLAN_Desc | varchar |  |  | NO | Description |
| SURLAN_Owner | varchar |  |  | SI | Owner |
| SURLAN_UpdatedDate | date |  |  | SI | Updated Date |
| SURLAN_UpdatedTime | time |  |  | SI | Updated Time |
| SURLAN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*