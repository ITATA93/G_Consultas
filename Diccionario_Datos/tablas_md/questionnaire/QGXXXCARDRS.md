# questionnaire.QGXXXCARDRS

> Cardiology Procedures Result

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiology Procedures Result

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bigint |  |  | SI | Result Findings |
| Q01TxtOnly | bigint |  |  | SI | Result Findings Plain Text Only |
| Q02 | numeric |  |  | SI | Frequency (Hz) |
| Q03 | numeric |  |  | SI | Saple Time (Sec) |
| Q04 | numeric |  |  | SI | Heart Rate (bpm) |
| Q05 | numeric |  |  | SI | P Duration (ms) |
| Q06 | numeric |  |  | SI | QRS Duration (ms) |
| Q07 | numeric |  |  | SI | T Duration (ms) |
| Q08 | numeric |  |  | SI | PR Interval (ms) |
| Q09 | numeric |  |  | SI | QT Interval (ms) |
| Q10 | numeric |  |  | SI | QTc Interval (ms) |
| Q11 | numeric |  |  | SI | P axis |
| Q12 | numeric |  |  | SI | QRS Axis |
| Q13 | numeric |  |  | SI | T Axis |
| Q14 | varchar |  |  | SI | Suggestion |
| Q15 | numeric |  |  | SI | Left atrial size—M-mode on echocardiography |
| Q16 | numeric |  |  | SI | Left atrial volume on echocardiography  |
| Q17 | numeric |  |  | SI | Left ventricular diastolic diameter  |
| Q18 | varchar |  |  | SI | Left ventricular systolic function Subjective asse... |
| Q19 | numeric |  |  | SI | Ejection Fraction |
| Q20 | varchar |  |  | SI | Left ventricular diastolic function Categories |
| Q21 | numeric |  |  | SI | Left ventricular wall thickness |
| Q22 | varchar |  |  | SI | Thrombus with location  |
| Q23 | varchar |  |  | SI | Mitral valve morphology  |
| Q24 | varchar |  |  | SI | Mitral valve mmorphology (other) |
| Q25 | numeric |  |  | SI | Mitral stenosis  |
| Q26 | varchar |  |  | SI | Mitral regurgitation |
| Q27 | varchar |  |  | SI | Additional Result Information |
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