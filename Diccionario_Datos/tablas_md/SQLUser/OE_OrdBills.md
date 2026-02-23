# SQLUser.OE_OrdBills

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILL_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| BILL_ARPBLItem_DR | varchar |  | FK | SI | Des Ref ARPBL Item |
| BILL_Amount | double |  |  | SI | Amount |
| BILL_Childsub | double |  |  | NO | Childsub |
| BILL_Dispensing | varchar |  |  | SI | Dispensing nodes |
| BILL_PackagePrice | varchar |  |  | SI | PackagePrice - At the moment, this field stores a ... |
| BILL_PayorType | varchar |  |  | SI | Payor Type |
| BILL_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Dominant Hand (select one): |
| Q02 | - |  |  | SI | Time to complete the test in seconds: |
| Q03 | - |  |  | SI | Dominant Hand: |
| Q04 | - |  |  | SI | Non-Dominant Hand: |
| Q05 | - |  |  | SI | sec |
| Q06 | - |  |  | SI | sec |
| Q07 | - |  |  | SI | General Information: |
| Q08 | - |  |  | SI | •  The Nine Hole Peg Test should be conducted with... |
| Q09 | - |  |  | SI | •  One practice trial (per arm) should be provided... |
| Q10 | - |  |  | SI | •  Timing should be performed with a stopwatch and... |
| Q11 | - |  |  | SI | •  The stop watch is started when the patient touc... |
| Q12 | - |  |  | SI | •  The stop watch is stopped when the patient plac... |
| Q13 | - |  |  | SI | Set-up (Mathiowetz et al, 1985): |
| Q14 | - |  |  | SI | •  A square board with 9 holes, |
| Q15 | - |  |  | SI | -  holes are spaced 3.2 cm (1.25 inches) apart |
| Q16 | - |  |  | SI | -  each hole is 1.3 cm (.5 inches) deep |
| Q17 | - |  |  | SI | •  9 wooden pegs should be .64 cm (.25 inches) in ... |
| Q18 | - |  |  | SI | •  A container that is constructed from .7 cm (.25... |
| Q19 | - |  |  | SI | •  The peg board should have a mechanism to decrea... |
| Q20 | - |  |  | SI | •  The pegboard should be placed in front of the p... |
| Q21 | - |  |  | SI | Patient Instructions (Mathiowetz et al, 1985): |
| Q22 | - |  |  | SI | •  The instructions should be provided while the a... |
| Q23 | - |  |  | SI | •  The patient’s dominant arm is tested first. |
| Q24 | - |  |  | SI | •  Instruct the patient to: |
| Q25 | - |  |  | SI | -  Pick up the pegs one at a time, using your righ... |
| Q26 | - |  |  | SI | Stabilize the peg board with your left (or right) ... |
| Q27 | - |  |  | SI | •  After the patient performs the practice trial, ... |
| Q28 | - |  |  | SI | -  This will be the actual test. The instructions ... |
| Q29 | - |  |  | SI | -  While the patient is performing the test say: F... |
| Q30 | - |  |  | SI | -  When the patient places the last peg on the boa... |
| Q31 | - |  |  | SI | -  Stop the stop watch when the last peg hits the ... |
| Q32 | - |  |  | SI | •  Place the container on the opposite side of the... |
| Q33 | - |  |  | SI | References: Mathiowetz V, Weber K, Kashman N, Voll... |
| Q34 | - |  |  | SI | Downloaded from www.rehabmeasures.org Test instruc... |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
| Q37 | - |  |  | SI | Notes |
| Q38 | - |  |  | SI | Mathiowetz V, Weber K, Kashman N, Volland G. Adult... |
| Q39 | - |  |  | SI | Downloaded from www.rehabmeasures.org Test instruc... |
| Q40 | - |  |  | SI | Assessment Norms |
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