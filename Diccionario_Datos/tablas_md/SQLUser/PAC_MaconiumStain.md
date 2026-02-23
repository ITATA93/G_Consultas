# SQLUser.PAC_MaconiumStain

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MACS_RowId | bigint | PK |  | NO | - |
| MACS_Code | varchar |  |  | NO | Code |
| MACS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MACS_CreatedDate | date |  |  | SI | Created Date |
| MACS_CreatedTime | time |  |  | SI | Created Time |
| MACS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MACS_DateFrom | date |  |  | SI | Date From |
| MACS_DateTo | date |  |  | SI | Date To |
| MACS_Desc | varchar |  |  | NO | Description |
| MACS_Owner | varchar |  |  | SI | Owner |
| MACS_UpdatedDate | date |  |  | SI | Updated Date |
| MACS_UpdatedTime | time |  |  | SI | Updated Time |
| MACS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age > 60 years |
| Q04 | - |  |  | SI | Rapid deceleration mechanism |
| Q05 | - |  |  | SI | Fall from > 20 ft (> 6m) or motor vehicle crash (M... |
| Q06 | - |  |  | SI | Chest pain |
| Q07 | - |  |  | SI | Intoxication |
| Q08 | - |  |  | SI | Altered mental status |
| Q09 | - |  |  | SI | Distracting painful injury |
| Q10 | - |  |  | SI | Tenderness to chest wall palpation |
| Q11 | - |  |  | SI | Valid for use with patients ≥ 15 years old with bl... |
| Q12 | - |  |  | SI | No thoracic imaging required |
| Q13 | - |  |  | SI | In well-appearing patient with no evidence of mult... |
| Q14 | - |  |  | SI | In ill - appearing patients and/or those who will ... |
| Q15 | - |  |  | SI | When to use |
| Q16 | - |  |  | SI | Pregnant patients with minor trauma |
| Q17 | - |  |  | SI | Patients who are of indeterminate risk |
| Q18 | - |  |  | SI | Young patients, in whom radiation exposure is more... |
| Q19 | - |  |  | SI | Why use |
| Q20 | - |  |  | SI | This decision instrument can help reduce unnecessa... |
| Q21 | - |  |  | SI | which reduces radiation exposure and provides fast... |
| Q22 | - |  |  | SI | allowing them to focus on treatment, evaluation of... |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | 0 |
| Q26 | - |  |  | SI | 1 - 7 |
| Q27 | - |  |  | SI | 0 points: |
| Q28 | - |  |  | SI | 1 - 7 points: |
| Q29 | - |  |  | SI | 1 - 7: Consider chest X-ray with / without chest C... |
| Q30 | - |  |  | SI | Consider chest X-ray with / without chest CT scan ... |
| Q31 | - |  |  | SI | Used to determine which patients require chest ima... |
| Q32 | - |  |  | SI | which reduces radiation exposure and provides fast... |
| Q33 | - |  |  | SI | allowing them to focus on treatment, evaluation of... |
| Q34 | - |  |  | SI | No thoracic imaging required -> Review guidelines |
| Q35 | - |  |  | SI | Consider Chest X-ray and CT -> Review guidelines |
| Q36 | - |  |  | SI | 0: No thoracic imaging required -> Review guidelin... |
| Q37 | - |  |  | SI | 1 - 7: Consider Chest X-ray and CT -> Review guide... |
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