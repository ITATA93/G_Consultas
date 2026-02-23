# questionnaire.QGXXXPAIN

> Pain Assessment

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pain Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q01a | time |  |  | SI | Time |
| Q02 | varchar |  |  | SI | Pain |
| Q02a | varchar |  |  | SI | Pain |
| Q03 | date |  |  | SI | Since |
| Q04 | time |  |  | SI | Since |
| Q05 | varchar |  |  | SI | Localisation |
| Q06 | varchar |  |  | SI | Bodymap |
| Q07 | varchar |  |  | SI | Type |
| Q08 | varchar |  |  | SI | Duration |
| Q09 | varchar |  |  | SI | Continuous |
| Q10 | varchar |  |  | SI | Time |
| Q11 | varchar |  |  | SI | Description of the patient |
| Q12 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | 0: No pain |
| Q21 | varchar |  |  | SI | 1-2: Mild Pain |
| Q22 | varchar |  |  | SI | 3-4: Moderate Pain |
| Q23 | varchar |  |  | SI | 5-6: Severe Pain |
| Q24 | varchar |  |  | SI | 7-8: Very Severe Pain |
| Q25 | varchar |  |  | SI | 9-10: Worst Possible Pain |
| Q26 | varchar |  |  | SI | This is a detailed Pain Assessment and verbal scal... |
| Q27 | varchar |  |  | SI | Analgesia |
| Q28 | varchar |  |  | SI | 0 |
| Q29 | varchar |  |  | SI | No pain |
| Q30 | varchar |  |  | SI | 1 - 2 |
| Q31 | varchar |  |  | SI | Mild Pain |
| Q32 | varchar |  |  | SI | 3 - 4 |
| Q33 | varchar |  |  | SI | Moderate Pain |
| Q34 | varchar |  |  | SI | 5 - 6 |
| Q35 | varchar |  |  | SI | Severe Pain |
| Q36 | varchar |  |  | SI | 7 - 8 |
| Q37 | varchar |  |  | SI | Very Severe Pain |
| Q38 | varchar |  |  | SI | 9 - 10 |
| Q39 | varchar |  |  | SI | Worst Possible Pain |
| Q40 | varchar |  |  | SI | Classification |
| Q41 | varchar |  |  | SI | Score |
| Q42 | varchar |  |  | SI | Localization (multiple choice) |
| Q43 | varchar |  |  | SI | Score |
| Q43ObsDR | varchar |  | FK | SI | Score DR |
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