# SQLUser.PAC_BookingChangeManag

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BCM_RowId | bigint | PK |  | NO | - |
| BCM_Code | varchar |  |  | NO | Code |
| BCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BCM_CreatedDate | date |  |  | SI | Created Date |
| BCM_CreatedTime | time |  |  | SI | Created Time |
| BCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BCM_DateFrom | date |  |  | SI | Date From |
| BCM_DateTo | date |  |  | SI | Date To |
| BCM_Desc | varchar |  |  | NO | Description |
| BCM_NationalCode | varchar |  |  | SI | National Code |
| BCM_Owner | varchar |  |  | SI | Owner |
| BCM_UpdatedDate | date |  |  | SI | Updated Date |
| BCM_UpdatedTime | time |  |  | SI | Updated Time |
| BCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Evaluation period |
| Q04 | - |  |  | SI | Grade symptoms at the highest activity level at wh... |
| Q05 | - |  |  | SI | 1. What is the highest level of activity that you ... |
| Q06 | - |  |  | SI | 2. During the past 4 weeks, or since your injury, ... |
| Q07 | - |  |  | SI | ( 0 = Never, 10 = Constant) |
| Q08 | - |  |  | SI | 3. If you have pain, how severe is it? (0 = No pai... |
| Q09 | - |  |  | SI | ( 0 = No pain, 10 = Worst pain) |
| Q10 | - |  |  | SI | 4. During the past 4 weeks, or since your injury, ... |
| Q11 | - |  |  | SI | 5. What is the highest level of activity you can p... |
| Q12 | - |  |  | SI | 6. During the past 4 weeks, or since your injury, ... |
| Q13 | - |  |  | SI | 7. What is the highest level of activity you can p... |
| Q14 | - |  |  | SI | 8. What is the highest level of activity you can p... |
| Q15 | - |  |  | SI | 9. How does your knee affect your ability to: |
| Q16 | - |  |  | SI | a. Go up stairs |
| Q17 | - |  |  | SI | b. Go down stairs |
| Q18 | - |  |  | SI | c. Kneel on the front of your knee |
| Q19 | - |  |  | SI | d. Squat |
| Q20 | - |  |  | SI | e. Sit with your knee bent |
| Q21 | - |  |  | SI | f. Rise from a chair |
| Q22 | - |  |  | SI | g. Run straight ahead |
| Q23 | - |  |  | SI | h. Jump and land on your involved leg |
| Q24 | - |  |  | SI | i. Stop and start quickly |
| Q25 | - |  |  | SI | 10.  How would you rate the function of your knee ... |
| Q26 | - |  |  | SI | Function prior to your knee injury |
| Q27 | - |  |  | SI | Current function of your knee |
| Q28 | - |  |  | SI | IKDC Score |
| Q29 | - |  |  | SI | Subjective Knee Form (IKDC) was designed to assess... |
| Q30 | - |  |  | SI | Date of injury |
| Q31 | - |  |  | SI | % |
| Q32 | - |  |  | SI | 2. During the past 4 weeks, or since your injury, ... |
| Q33 | - |  |  | SI | 3. If you have pain, how severe is it? (0 = No pai... |
| Q34 | - |  |  | SI | IKDC Score |
| Q35 | - |  |  | SI | Consulting doctor |
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