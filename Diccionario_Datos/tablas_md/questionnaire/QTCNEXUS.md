# questionnaire.QTCNEXUS

> NEXUS Chest Decision Instrument for Blunt Chest Trauma

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* NEXUS Chest Decision Instrument for Blunt Chest Trauma

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Age > 60 years |
| Q04 | varchar |  |  | SI | Rapid deceleration mechanism |
| Q05 | varchar |  |  | SI | Fall from > 20 ft (> 6m) or motor vehicle crash (M... |
| Q06 | varchar |  |  | SI | Chest pain |
| Q07 | varchar |  |  | SI | Intoxication |
| Q08 | varchar |  |  | SI | Altered mental status |
| Q09 | varchar |  |  | SI | Distracting painful injury |
| Q10 | varchar |  |  | SI | Tenderness to chest wall palpation |
| Q11 | varchar |  |  | SI | Valid for use with patients ≥ 15 years old with bl... |
| Q12 | varchar |  |  | SI | No thoracic imaging required |
| Q13 | varchar |  |  | SI | In well-appearing patient with no evidence of mult... |
| Q14 | varchar |  |  | SI | In ill - appearing patients and/or those who will ... |
| Q15 | varchar |  |  | SI | When to use |
| Q16 | varchar |  |  | SI | Pregnant patients with minor trauma |
| Q17 | varchar |  |  | SI | Patients who are of indeterminate risk |
| Q18 | varchar |  |  | SI | Young patients, in whom radiation exposure is more... |
| Q19 | varchar |  |  | SI | Why use |
| Q20 | varchar |  |  | SI | This decision instrument can help reduce unnecessa... |
| Q21 | varchar |  |  | SI | which reduces radiation exposure and provides fast... |
| Q22 | varchar |  |  | SI | allowing them to focus on treatment, evaluation of... |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | 0 |
| Q26 | varchar |  |  | SI | 1 - 7 |
| Q27 | varchar |  |  | SI | 0 points: |
| Q28 | varchar |  |  | SI | 1 - 7 points: |
| Q29 | varchar |  |  | SI | 1 - 7: Consider chest X-ray with / without chest C... |
| Q30 | varchar |  |  | SI | Consider chest X-ray with / without chest CT scan ... |
| Q31 | varchar |  |  | SI | Used to determine which patients require chest ima... |
| Q32 | varchar |  |  | SI | which reduces radiation exposure and provides fast... |
| Q33 | varchar |  |  | SI | allowing them to focus on treatment, evaluation of... |
| Q34 | varchar |  |  | SI | No thoracic imaging required -> Review guidelines |
| Q35 | varchar |  |  | SI | Consider Chest X-ray and CT -> Review guidelines |
| Q36 | varchar |  |  | SI | 0: No thoracic imaging required -> Review guidelin... |
| Q37 | varchar |  |  | SI | 1 - 7: Consider Chest X-ray and CT -> Review guide... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*