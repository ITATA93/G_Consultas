# questionnaire.QTCIKDC

> IKDC Subjective Knee Evaluation Form

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* IKDC Subjective Knee Evaluation Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Evaluation period |
| Q04 | varchar |  |  | SI | Grade symptoms at the highest activity level at wh... |
| Q05 | varchar |  |  | SI | 1. What is the highest level of activity that you ... |
| Q06 | varchar |  |  | SI | 2. During the past 4 weeks, or since your injury, ... |
| Q07 | varchar |  |  | SI | ( 0 = Never, 10 = Constant) |
| Q08 | varchar |  |  | SI | 3. If you have pain, how severe is it? (0 = No pai... |
| Q09 | varchar |  |  | SI | ( 0 = No pain, 10 = Worst pain) |
| Q10 | varchar |  |  | SI | 4. During the past 4 weeks, or since your injury, ... |
| Q11 | varchar |  |  | SI | 5. What is the highest level of activity you can p... |
| Q12 | varchar |  |  | SI | 6. During the past 4 weeks, or since your injury, ... |
| Q13 | varchar |  |  | SI | 7. What is the highest level of activity you can p... |
| Q14 | varchar |  |  | SI | 8. What is the highest level of activity you can p... |
| Q15 | varchar |  |  | SI | 9. How does your knee affect your ability to:  |
| Q16 | varchar |  |  | SI | a. Go up stairs |
| Q17 | varchar |  |  | SI | b. Go down stairs |
| Q18 | varchar |  |  | SI | c. Kneel on the front of your knee |
| Q19 | varchar |  |  | SI | d. Squat |
| Q20 | varchar |  |  | SI | e. Sit with your knee bent |
| Q21 | varchar |  |  | SI | f. Rise from a chair |
| Q22 | varchar |  |  | SI | g. Run straight ahead |
| Q23 | varchar |  |  | SI | h. Jump and land on your involved leg |
| Q24 | varchar |  |  | SI | i. Stop and start quickly |
| Q25 | varchar |  |  | SI | 10.  How would you rate the function of your knee ... |
| Q26 | varchar |  |  | SI | Function prior to your knee injury |
| Q27 | varchar |  |  | SI | Current function of your knee |
| Q28 | varchar |  |  | SI | IKDC Score |
| Q29 | varchar |  |  | SI | Subjective Knee Form (IKDC) was designed to assess... |
| Q30 | date |  |  | SI | Date of injury |
| Q31 | varchar |  |  | SI | % |
| Q32 | varchar |  |  | SI | 2. During the past 4 weeks, or since your injury, ... |
| Q33 | varchar |  |  | SI | 3. If you have pain, how severe is it? (0 = No pai... |
| Q34 | varchar |  |  | SI | IKDC Score |
| Q35 | varchar |  |  | SI | Consulting doctor |
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