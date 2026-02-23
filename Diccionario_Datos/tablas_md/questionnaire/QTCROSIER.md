# questionnaire.QTCROSIER

> Recognition of Stroke in the Emergency Room (ROSIER) Scale

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Recognition of Stroke in the Emergency Room (ROSIER) Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Pre-Assessment Conditions |
| Q04 | date |  |  | SI | Symptom onset date |
| Q05 | time |  |  | SI | Symptom onset time |
| Q06 | varchar |  |  | SI | Glasgow Coma Score (GCS) |
| Q07 | varchar |  |  | SI | Eye opening |
| Q07ObsDR | varchar |  | FK | SI | Eye opening DR |
| Q08 | varchar |  |  | SI | Verbal |
| Q08ObsDR | varchar |  | FK | SI | Verbal DR |
| Q09 | varchar |  |  | SI | Motor |
| Q09ObsDR | varchar |  | FK | SI | Motor DR |
| Q10 | varchar |  |  | SI | Systolic non invasive blood pressure (mmHg) |
| Q10ObsDR | varchar |  | FK | SI | Systolic non invasive blood pressure (mmHg) DR |
| Q11 | varchar |  |  | SI | Diastolic non invasive blood pressure (mmHg) |
| Q11ObsDR | varchar |  | FK | SI | Diastolic non invasive blood pressure (mmHg) DR |
| Q12 | varchar |  |  | SI | Blood glucose level (mmol/L) |
| Q12ObsDR | varchar |  | FK | SI | Blood glucose level (mmol/L) DR |
| Q13 | varchar |  |  | SI | If blood glucose level < 3·5 mmol/L treat urgently... |
| Q14 | varchar |  |  | SI | ROSIER Scale |
| Q15 | varchar |  |  | SI | Has there been loss of consciousness or syncope? |
| Q16 | varchar |  |  | SI | Has there been seizure activity? |
| Q17 | varchar |  |  | SI | Is there a NEW ACUTE onset of the following (or on... |
| Q18 | varchar |  |  | SI | I. Asymmetric facial weakness |
| Q19 | varchar |  |  | SI | II. Asymmetric arm weakness |
| Q20 | varchar |  |  | SI | III. Asymmetric leg weakness |
| Q21 | varchar |  |  | SI | IV. Speech disturbance |
| Q22 | varchar |  |  | SI | V. Visual field defect |
| Q23 | varchar |  |  | SI | Provisional Diagnosis |
| Q24 | varchar |  |  | SI | Provisional diagnosis |
| Q25 | varchar |  |  | SI | Specify |
| Q26 | varchar |  |  | SI | Guidelines |
| Q27 | varchar |  |  | SI | Stroke is unlikely but not completely excluded if ... |
| Q28 | varchar |  |  | SI | Dummy 1 |
| Q29 | varchar |  |  | SI | Dummy 2 |
| Q30 | varchar |  |  | SI | Dummy 3 |
| Q31 | varchar |  |  | SI | Dummy 4 |
| Q32 | varchar |  |  | SI | Score |
| Q33 | varchar |  |  | SI | Interpretation |
| Q34 | varchar |  |  | SI | >0 |
| Q35 | varchar |  |  | SI | Stroke is likely |
| Q36 | varchar |  |  | SI | ≤0 |
| Q37 | varchar |  |  | SI | Low probability of stroke but not excluded |
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