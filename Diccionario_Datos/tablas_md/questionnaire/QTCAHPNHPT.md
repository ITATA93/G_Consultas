# questionnaire.QTCAHPNHPT

> Nine Hole Peg Test

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nine Hole Peg Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Dominant Hand (select one): |
| Q02 | varchar |  |  | SI | Time to complete the test in seconds: |
| Q03 | numeric |  |  | SI | Dominant Hand: |
| Q04 | numeric |  |  | SI | Non-Dominant Hand: |
| Q05 | varchar |  |  | SI | sec |
| Q06 | varchar |  |  | SI | sec |
| Q07 | varchar |  |  | SI | General Information: |
| Q08 | varchar |  |  | SI | •  The Nine Hole Peg Test should be conducted with... |
| Q09 | varchar |  |  | SI | •  One practice trial (per arm) should be provided... |
| Q10 | varchar |  |  | SI | •  Timing should be performed with a stopwatch and... |
| Q11 | varchar |  |  | SI | •  The stop watch is started when the patient touc... |
| Q12 | varchar |  |  | SI | •  The stop watch is stopped when the patient plac... |
| Q13 | varchar |  |  | SI | Set-up (Mathiowetz et al, 1985): |
| Q14 | varchar |  |  | SI | •  A square board with 9 holes, |
| Q15 | varchar |  |  | SI | -  holes are spaced 3.2 cm (1.25 inches) apart |
| Q16 | varchar |  |  | SI | -  each hole is 1.3 cm (.5 inches) deep |
| Q17 | varchar |  |  | SI | •  9 wooden pegs should be .64 cm (.25 inches) in ... |
| Q18 | varchar |  |  | SI | •  A container that is constructed from .7 cm (.25... |
| Q19 | varchar |  |  | SI | •  The peg board should have a mechanism to decrea... |
| Q20 | varchar |  |  | SI | •  The pegboard should be placed in front of the p... |
| Q21 | varchar |  |  | SI | Patient Instructions (Mathiowetz et al, 1985): |
| Q22 | varchar |  |  | SI | •  The instructions should be provided while the a... |
| Q23 | varchar |  |  | SI | •  The patient’s dominant arm is tested first. |
| Q24 | varchar |  |  | SI | •  Instruct the patient to: |
| Q25 | varchar |  |  | SI | -  Pick up the pegs one at a time, using your righ... |
| Q26 | varchar |  |  | SI | Stabilize the peg board with your left (or right) ... |
| Q27 | varchar |  |  | SI | •  After the patient performs the practice trial, ... |
| Q28 | varchar |  |  | SI | -  This will be the actual test. The instructions ... |
| Q29 | varchar |  |  | SI | -  While the patient is performing the test say: F... |
| Q30 | varchar |  |  | SI | -  When the patient places the last peg on the boa... |
| Q31 | varchar |  |  | SI | -  Stop the stop watch when the last peg hits the ... |
| Q32 | varchar |  |  | SI | •  Place the container on the opposite side of the... |
| Q33 | varchar |  |  | SI | References: Mathiowetz V, Weber K, Kashman N, Voll... |
| Q34 | varchar |  |  | SI | Downloaded from www.rehabmeasures.org Test instruc... |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
| Q37 | varchar |  |  | SI | Notes |
| Q38 | varchar |  |  | SI | Mathiowetz V, Weber K, Kashman N, Volland G. Adult... |
| Q39 | varchar |  |  | SI | Downloaded from www.rehabmeasures.org Test instruc... |
| Q40 | varchar |  |  | SI | Assessment Norms |
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