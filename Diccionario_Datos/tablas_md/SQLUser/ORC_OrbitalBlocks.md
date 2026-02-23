# SQLUser.ORC_OrbitalBlocks

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORBBLO_RowId | bigint | PK |  | NO | - |
| ORBBLO_Code | varchar |  |  | NO | Code |
| ORBBLO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORBBLO_CreatedDate | date |  |  | SI | Created Date |
| ORBBLO_CreatedTime | time |  |  | SI | Created Time |
| ORBBLO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORBBLO_DateFrom | date |  |  | SI | Date From |
| ORBBLO_DateTo | date |  |  | SI | Date To |
| ORBBLO_Desc | varchar |  |  | NO | Description |
| ORBBLO_Owner | varchar |  |  | SI | Owner |
| ORBBLO_UpdatedDate | date |  |  | SI | Updated Date |
| ORBBLO_UpdatedTime | time |  |  | SI | Updated Time |
| ORBBLO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Ambulation |
| Q02 | - |  |  | SI | Pyramidal |
| Q03 | - |  |  | SI | Cerebellar |
| Q04 | - |  |  | SI | Brainstem |
| Q05 | - |  |  | SI | Sensory |
| Q06 | - |  |  | SI | Bowel and bladder |
| Q07 | - |  |  | SI | Visual |
| Q08 | - |  |  | SI | Cerebral |
| Q09 | - |  |  | SI | Other |
| Q10 | - |  |  | SI | Expanded Disability and Functional Status Scale is... |
| Q11 | - |  |  | SI | Normal ambulation |
| Q12 | - |  |  | SI | 1.0 - 4.5 |
| Q13 | - |  |  | SI | Impaired ambulation |
| Q14 | - |  |  | SI | 5.0 - 9.5 |
| Q15 | - |  |  | SI | Ambulation Score |
| Q16 | - |  |  | SI | Functional Systems Score |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | 1.0 - 4.5: Normal ambulation |
| Q20 | - |  |  | SI | 5.0 - 9.5: Impaired ambulation |
| Q21 | - |  |  | SI | Ambulation Score Interpretation |
| Q22 | - |  |  | SI | Functional Systems Score Interpretation |
| Q23 | - |  |  | SI | Score range of 1-40	 |
| Q24 | - |  |  | SI | Higher score indicates more functional disability |
| Q25 | - |  |  | SI | Lower score indicates less functional disability |
| Q26 | - |  |  | SI | Score range of 1-40: Higher score indicates more f... |
| Q27 | - |  |  | SI | Score range of 1-40: Lower score indicates less fu... |
| Q28 | - |  |  | SI | Normal functional systems |
| Q29 | - |  |  | SI | Fully ambulatory |
| Q30 | - |  |  | SI | Death due to Multiple Sclerosis |
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