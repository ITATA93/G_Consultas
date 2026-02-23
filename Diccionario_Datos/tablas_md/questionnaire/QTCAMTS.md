# questionnaire.QTCAMTS

> Abbreviated Mental Test Score (AMTS-10)

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Abbreviated Mental Test Score (AMTS-10)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age? |
| Q02 | varchar |  |  | SI | Time? (to the nearest hour) |
| Q03 | varchar |  |  | SI | Address for recall at the end of test: '42 West St... |
| Q03a | varchar |  |  | SI | (this should be repeated by the patient to ensure ... |
| Q03b | varchar |  |  | SI | Address recall correct? |
| Q04 | varchar |  |  | SI | Year? |
| Q05 | varchar |  |  | SI | Name of this place? |
| Q06 | varchar |  |  | SI | Identification of two persons (doctor, nurse etc.)... |
| Q07 | varchar |  |  | SI | Date of birth? |
| Q08 | varchar |  |  | SI | Last year of second world war? |
| Q09 | varchar |  |  | SI | Name of the present monarch? |
| Q10 | varchar |  |  | SI | Count backwards 20 to 1 |
| Q17 | date |  |  | SI | Date |
| Q18 | time |  |  | SI | Time |
| Q19 | varchar |  |  | SI | The Abbreviated Mental Test Score was described in... |
| Q20 | varchar |  |  | SI | 1.&nbsp;Hodkinson HM. Evaluation of a mental test ... |
| Q21 | varchar |  |  | SI | 2.&nbsp;Blessed G, Tomlinson BE, Roth M. The assoc... |
| Q22 | varchar |  |  | SI | 3.&nbsp;Jitapunkul S, Pillay I, Ebrahim S. The Abb... |
| QAMTS | varchar |  |  | SI | The Abbreviated mental test score (AMTS) is a ques... |
| QSCORE1 | varchar |  |  | SI | Significantly Impaired: less than 7 correct answer... |
| QSCORE2 | varchar |  |  | SI | Probably Impaired: 7 correct answers |
| QSCORE3 | varchar |  |  | SI | Normal: 8 or more correct answers |
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