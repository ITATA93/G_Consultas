# questionnaire.QTCPAIN2

> Pain Assessment (General)

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pain Assessment (General)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Pain onset |
| Q04 | time |  |  | SI | Pain onset time |
| Q05 | varchar |  |  | SI | Details of event leading to onset |
| Q06 | varchar |  |  | SI | Pain rating scale |
| Q07 | varchar |  |  | SI | Please see guidelines section  for details on all ... |
| Q08 | varchar |  |  | SI | Numerical rating pain scale (0 to 10) |
| Q09 | varchar |  |  | SI | 4 point verbal rating pain scale |
| Q09ObsDR | varchar |  | FK | SI | 4 point verbal rating pain scale DR |
| Q10 | varchar |  |  | SI | Visual Analogue Scale (0 to 10) |
| Q10ObsDR | varchar |  | FK | SI | Visual Analogue Scale (0 to 10) DR |
| Q11 | varchar |  |  | SI | Wong-Baker FACES pain rating scale |
| Q11ObsDR | varchar |  | FK | SI | Wong-Baker FACES pain rating scale DR |
| Q12 | varchar |  |  | SI | Patient's description of pain |
| Q12ObsDR | varchar |  | FK | SI | Patient's description of pain DR |
| Q13 | varchar |  |  | SI | Pattern |
| Q14 | varchar |  |  | SI | Aggravating factors - what makes the pain worse? |
| Q14ObsDR | varchar |  | FK | SI | Aggravating factors - what makes the pain worse? D... |
| Q15 | varchar |  |  | SI | Relieving factors - what makes the pain better? |
| Q15ObsDR | varchar |  | FK | SI | Relieving factors - what makes the pain better? DR |
| Q16 | varchar |  |  | SI | Care provider type |
| Q17 | varchar |  |  | SI | Specialty |
| Q18 | varchar |  |  | SI | Numeric Rating Scale (0 - 10) |
| Q19 | varchar |  |  | SI | Visual Analogue Scale (VAS) |
| Q20 | varchar |  |  | SI | A VAS is usually a 100-mm long horizontal line wit... |
| Q21 | varchar |  |  | SI | Patients are instructed to mark the point on the l... |
| Q22 | varchar |  |  | SI | When reading the VAS, the position of the responde... |
| Q23 | varchar |  |  | SI | The VAS should not have any markings (e. g., ident... |
| Q24 | varchar |  |  | SI | Wong - Baker FACES® Pain Rating Scale Image |
| Q25 | varchar |  |  | SI | 4 Point Verbal Rating Scale |
| Q26 | varchar |  |  | SI | None: Negative response to questioning |
| Q27 | varchar |  |  | SI | Mild: Pain reported in response to questioning onl... |
| Q28 | varchar |  |  | SI | Moderate: Pain reported in response to questioning... |
| Q29 | varchar |  |  | SI | Severe: Strong verbal response or response accompa... |
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