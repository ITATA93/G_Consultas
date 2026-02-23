# questionnaire.QTCBBTF

> Box and Blocks Testing Form

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Box and Blocks Testing Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Dominant Hand |
| Q02 | varchar |  |  | SI | Number of blocks transported in 1 minute |
| Q03 | numeric |  |  | SI | Dominant hand |
| Q04 | numeric |  |  | SI | Non-dominant hand |
| Q05 | varchar |  |  | SI | blocks |
| Q06 | varchar |  |  | SI | blocks |
| Q07 | varchar |  |  | SI | The patient is allowed a 15-second trial period pr... |
| Q08 | varchar |  |  | SI | Immediately before testing begins, the patient sho... |
| Q09 | varchar |  |  | SI | When testing begins, the patient should grasp one ... |
| Q10 | varchar |  |  | SI | The patient should continue doing this for one min... |
| Q11 | varchar |  |  | SI | The procedure should then be repeated with the non... |
| Q12 | varchar |  |  | SI | After testing, the examiner should count the block... |
| Q13 | varchar |  |  | SI | If a patient transports two or more blocks at the ... |
| Q14 | varchar |  |  | SI | No penalty should be made if the subjects transpor... |
| Q15 | varchar |  |  | SI | A test box with 150 blocks and a partition in the ... |
| Q16 | varchar |  |  | SI | The patient should be seated on a standard-height ... |
| Q17 | varchar |  |  | SI | 150 blocks should be in the compartment of the tes... |
| Q18 | varchar |  |  | SI | The examiner should face the patient so she or he ... |
| Q19 | varchar |  |  | SI | “I want to see how quickly you can pick up one blo... |
| Q20 | varchar |  |  | SI | Carry it to the other side of the box and drop it.... |
| Q21 | varchar |  |  | SI | Transport three cubes over the partition in the sa... |
| Q22 | varchar |  |  | SI | “If you pick up two blocks at a time, they will co... |
| Q23 | varchar |  |  | SI |  If you toss the blocks without your fingertips cr... |
| Q24 | varchar |  |  | SI |  Before you start, you will have a chance to pract... |
| Q25 | varchar |  |  | SI | “Place your hands on the sides of the box. When it... |
| Q26 | varchar |  |  | SI | Trial period: Start the stop watch at the word go.... |
| Q27 | varchar |  |  | SI | If mistakes are made during the practice period, c... |
| Q28 | varchar |  |  | SI | On completion of the practice period, transport th... |
| Q29 | varchar |  |  | SI | Continued with the following directions: |
| Q30 | varchar |  |  | SI | “This will be the actual test. The instructions ar... |
| Q31 | varchar |  |  | SI | Ready.” [Wait 3 seconds]  |
| Q32 | varchar |  |  | SI | “Go.” |
| Q33 | varchar |  |  | SI | “Stop.” [After 1 minute, count the blocks and reco... |
| Q34 | varchar |  |  | SI | “Now you are to do the same thing with your left (... |
| Q35 | varchar |  |  | SI | Put your hands on the sides of the box as before. ... |
| Q36 | varchar |  |  | SI | “Ready.” [Wait 3 seconds] |
| Q37 | varchar |  |  | SI | “Go.” |
| Q38 | varchar |  |  | SI | “Stop.” [After 15 seconds] |
| Q39 | varchar |  |  | SI | Return the transported blocks to the compartment a... |
| Q40 | varchar |  |  | SI | “This will be the actual test. The instructions ar... |
| Q41 | varchar |  |  | SI | “Ready.” [Wait 3 seconds]  |
| Q42 | varchar |  |  | SI | “Go.” |
| Q43 | varchar |  |  | SI | “Stop.” [After 1 minute, count the blocks and reco... |
| Q44 | varchar |  |  | SI | The score is the number of blocks carried from one... |
| Q45 | varchar |  |  | SI | Score each hand separately. |
| Q46 | bit |  |  | SI | Dominant |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
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