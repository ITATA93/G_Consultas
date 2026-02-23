# questionnaire.QTCSPADI

> Shoulder Pain and Disability Index (SPADI)

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Pain and Disability Index (SPADI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please score based on what best represents your ex... |
| Q02 | varchar |  |  | SI | How severe is your pain? |
| Q03 | varchar |  |  | SI | Best describe your pain where: 0 = no pain and 10 ... |
| Q04 | varchar |  |  | SI | At its worst? |
| Q05 | varchar |  |  | SI | When lying on the involved side? |
| Q06 | varchar |  |  | SI | Reaching for something on a high shelf? |
| Q07 | varchar |  |  | SI | Touching the back of your neck? |
| Q08 | varchar |  |  | SI | Pushing with the involved arm? |
| Q09 | varchar |  |  | SI | How much difficulty do you have? |
| Q10 | varchar |  |  | SI | Best describe your experience where: 0 = no diffic... |
| Q11 | varchar |  |  | SI | Washing your hair? |
| Q12 | varchar |  |  | SI | Washing your back? |
| Q13 | varchar |  |  | SI | Putting on an undershirt or jumper? |
| Q14 | varchar |  |  | SI | Putting on a shirt that buttons down the front? |
| Q15 | varchar |  |  | SI | Putting on your pants? |
| Q16 | varchar |  |  | SI | Placing an object on a high shelf? |
| Q17 | varchar |  |  | SI | Carrying a heavy object of 10 pounds (4.5 kilogram... |
| Q18 | varchar |  |  | SI | Removing something from your back pocket? |
| Q19 | varchar |  |  | SI | Pain Score |
| Q20 | varchar |  |  | SI | Disability Score |
| Q21 | varchar |  |  | SI | Total Pain Score (%) |
| Q22 | varchar |  |  | SI | Total Disability Score (%) |
| Q23 | varchar |  |  | SI | Total SPADI Score (%) |
| Q24 | varchar |  |  | SI | Total score ranging from 0 (best) to 100 (worst) |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification |
| Q27 | varchar |  |  | SI | Score ranges from 1% (no Shoulder pain) to 100 % (... |
| Q28 | varchar |  |  | SI | Score ranges from 1% (no Disability) to 100 % (sev... |
| Q29 | varchar |  |  | SI | The Shoulder Pain and Disability Index (SPADI) is ... |
| Q30 | date |  |  | SI | Date |
| Q31 | time |  |  | SI | Time |
| Q32 | varchar |  |  | SI | Total Pain Score (%) - Display only |
| Q33 | varchar |  |  | SI | Total Disability Score (%) - Display only |
| Q34 | varchar |  |  | SI | Total SPADI Score (%) - Display only |
| Q35 | varchar |  |  | SI | Total Pain Score (%) Caption |
| Q36 | varchar |  |  | SI | Total Disability Score (%) Caption |
| Q37 | varchar |  |  | SI | Total SPADI Score (%) Caption |
| Q38 | varchar |  |  | SI | Total SPADI Score (%) Caption |
| Q39 | varchar |  |  | SI | Total Pain Score (%) |
| Q40 | varchar |  |  | SI | Total Disability Score (%) |
| Q41 | varchar |  |  | SI | Total SPADI Score (%) |
| Q42 | varchar |  |  | SI | Please click Apply then Update to get the score ca... |
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