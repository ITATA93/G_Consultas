# questionnaire.QTCBPREPOR

> 24 Hour Ambulatory Blood Pressure Report

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* 24 Hour Ambulatory Blood Pressure Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Recording |
| Q02 | date |  |  | SI | Date of Analysis |
| Q03 | varchar |  |  | SI | Monitor ID |
| Q04 | numeric |  |  | SI | SUCCESS RATE (%) |
| Q05 | varchar |  |  | SI | Height |
| Q05ObsDR | varchar |  | FK | SI | Height DR |
| Q06 | varchar |  |  | SI | Weight |
| Q06ObsDR | varchar |  | FK | SI | Weight DR |
| Q07 | varchar |  |  | SI | Diabetes |
| Q08 | varchar |  |  | SI | Systolic min / max (mmHg) |
| Q08ObsDR | varchar |  | FK | SI | Systolic min / max (mmHg) DR |
| Q09 | varchar |  |  | SI | Systolic min / max 2 |
| Q09ObsDR | varchar |  | FK | SI | Systolic min / max 2 DR |
| Q10 | varchar |  |  | SI | mmHg |
| Q11 | varchar |  |  | SI | Diastolic min / max (mmHg) |
| Q11ObsDR | varchar |  | FK | SI | Diastolic min / max (mmHg) DR |
| Q12 | varchar |  |  | SI | Diastolic min / max 2 |
| Q12ObsDR | varchar |  | FK | SI | Diastolic min / max 2 DR |
| Q13 | varchar |  |  | SI | mmHg |
| Q14 | varchar |  |  | SI | 24 Hour Average BP (mmHg) |
| Q14ObsDR | varchar |  | FK | SI | 24 Hour Average BP (mmHg) DR |
| Q15 | varchar |  |  | SI | Daytime Average (mmHg) |
| Q15ObsDR | varchar |  | FK | SI | Daytime Average (mmHg) DR |
| Q16 | varchar |  |  | SI | Percentage of systolic readings > 120 mmHG |
| Q16ObsDR | varchar |  | FK | SI | Percentage of systolic readings > 120 mmHG DR |
| Q17 | varchar |  |  | SI | Percentage of diastolic readings > 80 mmHG |
| Q17ObsDR | varchar |  | FK | SI | Percentage of diastolic readings > 80 mmHG DR |
| Q18 | varchar |  |  | SI | Nocturnal Average (mmHg) |
| Q18ObsDR | varchar |  | FK | SI | Nocturnal Average (mmHg) DR |
| Q19 | varchar |  |  | SI | Nocturnal Dipper (mmHg) |
| Q19ObsDR | varchar |  | FK | SI | Nocturnal Dipper (mmHg) DR |
| Q20 | varchar |  |  | SI | Percentage of nocturnal systolic readings > 120 mm... |
| Q20ObsDR | varchar |  | FK | SI | Percentage of nocturnal systolic readings > 120 mm... |
| Q21 | varchar |  |  | SI | Percentage of nocturnal diastolic readings > 80 mm... |
| Q21ObsDR | varchar |  | FK | SI | Percentage of nocturnal diastolic readings > 80 mm... |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | Conclusion |
| Q24 | varchar |  |  | SI | Reported by |
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