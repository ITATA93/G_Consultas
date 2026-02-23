# questionnaire.QTCLEFS

> The Lower Extremity Functional Scale

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Lower Extremity Functional Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | We are interested in knowing whether you are havin... |
| Q04 | varchar |  |  | SI | Please provide an answer for each activity. |
| Q05 | varchar |  |  | SI | Today, do you or would you have any difficulty at ... |
| Q06 | varchar |  |  | SI | Any of your usual work, housework, or school activ... |
| Q07 | varchar |  |  | SI | Your usual hobbies, recreational, or sporting acti... |
| Q08 | varchar |  |  | SI | Getting into or out of the bath |
| Q09 | varchar |  |  | SI | Walking between rooms |
| Q10 | varchar |  |  | SI | Putting on your shoes or socks |
| Q11 | varchar |  |  | SI | Squatting |
| Q12 | varchar |  |  | SI | Lifting an object, like a bag of groceries from th... |
| Q13 | varchar |  |  | SI | Performing light activities around your home |
| Q14 | varchar |  |  | SI | Performing heavy activities around your home |
| Q15 | varchar |  |  | SI | Getting into or out of a car |
| Q16 | varchar |  |  | SI | Walking 2 blocks |
| Q17 | varchar |  |  | SI | Walking a mile |
| Q18 | varchar |  |  | SI | Going up or down 10 stairs (about 1 flight of stai... |
| Q19 | varchar |  |  | SI | Standing for 1 hour |
| Q20 | varchar |  |  | SI | Sitting for 1 hour |
| Q21 | varchar |  |  | SI | Running on even ground |
| Q22 | varchar |  |  | SI | Running on uneven ground |
| Q23 | varchar |  |  | SI | Making sharp turns while running fast |
| Q24 | varchar |  |  | SI | Hopping |
| Q25 | varchar |  |  | SI | Rolling over in bed |
| Q26 | varchar |  |  | SI | Minimum level of detectable change (90% confidence... |
| Q27 | varchar |  |  | SI | The higher the score indicates a higher functional... |
| Q28 | varchar |  |  | SI | Binkley JM, Stratford PW, Lott SA, Riddle DL. The ... |
| Q29 | varchar |  |  | SI | The Lower Extremity Functional Scale (LEFS) can be... |
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