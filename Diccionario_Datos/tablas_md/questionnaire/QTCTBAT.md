# questionnaire.QTCTBAT

> Tinetti Balance Assessment Tool

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tinetti Balance Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Patient seated on a hard, armless chair |
| Q02 | varchar |  |  | SI | Sitting balance |
| Q03 | varchar |  |  | SI | Rising from chair |
| Q04 | varchar |  |  | SI | Attempts to rise |
| Q05 | varchar |  |  | SI | Immediate standing balance (first 5 seconds) |
| Q06 | varchar |  |  | SI | Standing balance |
| Q07 | varchar |  |  | SI | Sternal nudge (feet close together) |
| Q08 | varchar |  |  | SI | Eyes closed (feet together) |
| Q09 | varchar |  |  | SI | Turning 360 degrees |
| Q09b | varchar |  |  | SI | Turning 360 degress |
| Q10 | varchar |  |  | SI | Sitting down |
| Q11 | varchar |  |  | SI | Balance Score |
| Q13 | varchar |  |  | SI | Patient stands with therapist, walks across room (... |
| Q14 | varchar |  |  | SI | Initiation of gait (Immediately after told to ‘go’... |
| Q15 | varchar |  |  | SI | Step length and height |
| Q16 | varchar |  |  | SI | Foot clearance |
| Q17 | varchar |  |  | SI | Step symmetry |
| Q18 | varchar |  |  | SI | Step continuity |
| Q19 | varchar |  |  | SI | Path |
| Q20 | varchar |  |  | SI | Trunk |
| Q21 | varchar |  |  | SI | Walking time |
| Q22 | varchar |  |  | SI | Gait Score |
| Q23 | varchar |  |  | SI | Total Score (Balance + Gait) |
| Q24 | varchar |  |  | SI | Risk Indicators: |
| Q25 | varchar |  |  | SI | Tinetti Total Score |
| Q26 | varchar |  |  | SI | ≤ 18 |
| Q27 | varchar |  |  | SI | 19 - 23 |
| Q28 | varchar |  |  | SI | ≥ 24 |
| Q29 | varchar |  |  | SI | Risk for Falls |
| Q30 | varchar |  |  | SI | High |
| Q31 | varchar |  |  | SI | Moderate |
| Q32 | varchar |  |  | SI | Low |
| Q33 | longvarbinary |  |  | SI | Signature |
| Q33UDt | date |  |  | SI | Signature Last Updated Date |
| Q33UTm | time |  |  | SI | Signature Last Updated Time |
| Q34 | varchar |  |  | SI | Evaluated Function |
| Q35 | varchar |  |  | SI | Evaluated Function |
| Q36 | varchar |  |  | SI | Scoring |
| Q37 | varchar |  |  | SI | Scoring |
| Q38 | varchar |  |  | SI | / 12 |
| Q39 | varchar |  |  | SI | / 16 |
| Q40 | varchar |  |  | SI | / 28 |
| Q41 | varchar |  |  | SI | The Tinetti Balance Assesssment Tool, or Performan... |
| Q42 | varchar |  |  | SI | ≤ 18: High |
| Q43 | varchar |  |  | SI | 19 - 23: Moderate |
| Q44 | varchar |  |  | SI | ≥ 24: Low |
| Q45 | date |  |  | SI | Date |
| Q46 | time |  |  | SI | Time |
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