# SQLUser.ORC_CertificationAuthoriser

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CERAUT_RowId | bigint | PK |  | NO | - |
| CERAUT_Code | varchar |  |  | NO | Code |
| CERAUT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CERAUT_CreatedDate | date |  |  | SI | Created Date |
| CERAUT_CreatedTime | time |  |  | SI | Created Time |
| CERAUT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CERAUT_DateFrom | date |  |  | SI | Date From |
| CERAUT_DateTo | date |  |  | SI | Date To |
| CERAUT_Desc | varchar |  |  | NO | Description |
| CERAUT_Owner | varchar |  |  | SI | Owner |
| CERAUT_UpdatedDate | date |  |  | SI | Updated Date |
| CERAUT_UpdatedTime | time |  |  | SI | Updated Time |
| CERAUT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Bilirubin (total) |
| Q02 | - |  |  | SI | Albumin |
| Q03 | - |  |  | SI | INR |
| Q04 | - |  |  | SI | Ascites |
| Q05 | - |  |  | SI | Encephalopathy |
| Q06 | - |  |  | SI | Score Interpretation |
| Q07 | - |  |  | SI | • Child Class A |
| Q08 | - |  |  | SI | Life Expectancy : 15 - 20 years |
| Q09 | - |  |  | SI | Abdominal surgery peri-operative mortality: 10% |
| Q10 | - |  |  | SI | • Child Class B |
| Q11 | - |  |  | SI | Indication for transplant evaluation |
| Q12 | - |  |  | SI | Abdominal surgery peri-operative mortality: 30% |
| Q13 | - |  |  | SI | • Child Class C |
| Q14 | - |  |  | SI | Life Expectancy : 1 - 3 years |
| Q15 | - |  |  | SI | Abdominal surgery peri-operative mortality: 82% |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Classification |
| Q18 | - |  |  | SI | 5 – 6 |
| Q19 | - |  |  | SI | Child Class A - Life Expectancy: 15-20 years - Abd... |
| Q20 | - |  |  | SI | 7 – 9 |
| Q21 | - |  |  | SI | Child Class B - Indication for transplant evaluati... |
| Q22 | - |  |  | SI | 10 – 15 |
| Q23 | - |  |  | SI | Child Class C - Life Expectancy: 1 - 3 years - Abd... |
| Q24 | - |  |  | SI | 5 – 6: Child Class A - Life Expectancy: 15 - 20 ye... |
| Q25 | - |  |  | SI | 7 – 9: Child Class B - Indication for transplant e... |
| Q26 | - |  |  | SI | 10 – 15: Child Class C - Life Expectancy: 1 - 3 ye... |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
| Q29 | - |  |  | SI | The Child-Pugh score is a system for assessing the... |
| Q30 | - |  |  | SI | It provides a forecast of the increasing severity ... |
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