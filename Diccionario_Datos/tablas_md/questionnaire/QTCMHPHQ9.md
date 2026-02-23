# questionnaire.QTCMHPHQ9

> Patient Health Questionnaire-9 (PHQ-9)

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Health Questionnaire-9 (PHQ-9)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Over the last two weeks how often have you been bo... |
| Q02 | varchar |  |  | SI | Little interest or pleasure in doing things |
| Q03 | varchar |  |  | SI | Feeling down, depressed or hopeless |
| Q04 | varchar |  |  | SI | Trouble falling or staying asleep or sleeping too ... |
| Q05 | varchar |  |  | SI | Feeling tired or having little energy |
| Q06 | varchar |  |  | SI | Poor appetite or over-eating |
| Q07 | varchar |  |  | SI | Feeling bad about yourself – or that you are a fai... |
| Q08 | varchar |  |  | SI | Trouble concentrating on things, such as reading t... |
| Q09 | varchar |  |  | SI | Moving or speaking so slowly that other people cou... |
| Q10 | varchar |  |  | SI | Thoughts that you would be better off dead or of h... |
| Q11 | varchar |  |  | SI | Score |
| Q12 | varchar |  |  | SI | Classification |
| Q13 | varchar |  |  | SI | None |
| Q14 | varchar |  |  | SI | 0 - 4 |
| Q15 | varchar |  |  | SI | Mild |
| Q16 | varchar |  |  | SI | 5 - 9 |
| Q17 | varchar |  |  | SI | Moderate |
| Q18 | varchar |  |  | SI | 10 - 14 |
| Q19 | varchar |  |  | SI | Moderately Severe |
| Q20 | varchar |  |  | SI | 15 - 19 |
| Q21 | varchar |  |  | SI | Severe |
| Q22 | varchar |  |  | SI | 20 - 27 |
| Q23 | varchar |  |  | SI | 0 to 4: None |
| Q24 | varchar |  |  | SI | 5 to 9: Mild |
| Q25 | varchar |  |  | SI | 10 to 14: Moderate |
| Q26 | varchar |  |  | SI | 15 to 19: Moderately Severe |
| Q27 | varchar |  |  | SI | 20 to 27: Severe |
| Q28 | varchar |  |  | SI | The patient health questionnaire (PHQ-9) is a mult... |
| Q29 | date |  |  | SI | Date |
| Q30 | time |  |  | SI | Time |
| Q31 | varchar |  |  | SI | If you checked off any problems, how difficult hav... |
| Q32 | varchar |  |  | SI | Notes |
| Q33 | varchar |  |  | SI | Kroenke K, Spitzer RL, Williams JBW. The PHQ‐9: Va... |
| Q34 | varchar |  |  | SI | No permission required to reproduce, translate, di... |
| Q35 | varchar |  |  | SI | If you checked off any problems, how difficult hav... |
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