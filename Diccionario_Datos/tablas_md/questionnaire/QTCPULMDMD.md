# questionnaire.QTCPULMDMD

> Performance of the Upper Limb module for Duchenne muscular dystrophy

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Performance of the Upper Limb module for Duchenne muscular dystrophy

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Preferred arm (used for all tests) |
| Q04 | numeric |  |  | SI | Elbow extension ROM: Right |
| Q05 | varchar |  |  | SI | ° |
| Q06 | numeric |  |  | SI | Elbow extension ROM: Left |
| Q07 | varchar |  |  | SI | ° |
| Q08 | varchar |  |  | SI | Supination ROM: Right |
| Q09 | varchar |  |  | SI | Supination ROM: Left |
| Q10 | varchar |  |  | SI | Start with A to identify starting point for subseq... |
| Q11 | varchar |  |  | SI | A. Entry Item |
| Q12 | varchar |  |  | SI | Item 1:  Shoulder abduction both arms above head |
| Q13 | varchar |  |  | SI | ''Raise your arms out to the side and above your h... |
| Q14 | varchar |  |  | SI | Item 2: Raise both arms to shoulder height (elbows... |
| Q15 | varchar |  |  | SI | ''Raise your arms to shoulder level'' |
| Q16 | varchar |  |  | SI | Item 3: Shoulder flexion to shoulder height (no we... |
| Q17 | varchar |  |  | SI | ''Reach out and touch my hand'' |
| Q18 | varchar |  |  | SI | Item 4: Shoulder flexion to shoulder height with 5... |
| Q19 | varchar |  |  | SI | ''Reach out and touch my hand'' |
| Q20 | varchar |  |  | SI | Item 5: Shoulder flexion above  shoulder height wi... |
| Q21 | varchar |  |  | SI | Hand on lap - ''Give me the weight'' |
| Q22 | varchar |  |  | SI | Item 6: Shoulder flexion above shoulder height wit... |
| Q23 | varchar |  |  | SI | Hand on lap - ''Give me the weight'' |
| Q24 | varchar |  |  | SI | Item 7: Hand(s) to mouth |
| Q25 | varchar |  |  | SI | ''Bring the cup to your mouth with one hand'' |
| Q26 | varchar |  |  | SI | Item 8: Hands to table from lap |
| Q27 | varchar |  |  | SI | ''Bring both hands from lap to table'' |
| Q28 | varchar |  |  | SI | Item 9: Move weight on table 100g |
| Q29 | varchar |  |  | SI | “Move the weight from outside circle to centre cir... |
| Q30 | varchar |  |  | SI | Item 10: Move weight on table 500g |
| Q31 | varchar |  |  | SI | ''Move the weight from outside circle to centre ci... |
| Q32 | varchar |  |  | SI | Item 11: Move weight on table 1kg |
| Q33 | varchar |  |  | SI | ''Move the weight from outside circle to centre ci... |
| Q34 | varchar |  |  | SI | Item 12: Lift heavy can diagonally |
| Q35 | varchar |  |  | SI | ''Lift can from this circle nearest your hand to t... |
| Q36 | varchar |  |  | SI | Item 13: Stack of three cans |
| Q37 | varchar |  |  | SI | ''Stack these two cans, one at a time on the middl... |
| Q38 | varchar |  |  | SI | Item 14: Stack of five cans |
| Q39 | varchar |  |  | SI | ''Stack these two additional cans, one at a time o... |
| Q40 | varchar |  |  | SI | Item 15: Remove lid from container |
| Q41 | varchar |  |  | SI | ''Use your hands to open this container'' |
| Q42 | varchar |  |  | SI | Item 16: Tearing paper |
| Q43 | varchar |  |  | SI | ''Tear the sheet of paper beginning from here'' |
| Q44 | varchar |  |  | SI | Item 17: Tracing path |
| Q45 | varchar |  |  | SI | ''Use your pencil to complete the path in one smoo... |
| Q46 | varchar |  |  | SI | Item 18: Push on light |
| Q47 | varchar |  |  | SI | ''Push on the light with the fingers of one hand'' |
| Q48 | varchar |  |  | SI | Item 19: Supination |
| Q49 | varchar |  |  | SI | ''Pick up the light and turn your hand over'' |
| Q50 | varchar |  |  | SI | Item 20: Picking up coins |
| Q51 | varchar |  |  | SI | ''Using one hand, Pick up 6 coins, one at a time'' |
| Q52 | varchar |  |  | SI | Item 21:  Placing finger on number diagram (precis... |
| Q53 | varchar |  |  | SI | ''Using one finger to touch each number on the dia... |
| Q54 | varchar |  |  | SI | Item 22:  Pick up 10g weight finger pinch |
| Q55 | varchar |  |  | SI | ''Pick up this small weight like this (by body of ... |
| Q56 | varchar |  |  | SI | Additional Material Item 17: Tracing a path |
| Q57 | varchar |  |  | SI | Additional Material Item 21: Placing finger on num... |
| Q58 | varchar |  |  | SI | Starting on the yellow number 1 point to the numbe... |
| Q59 | varchar |  |  | SI | Score |
| Q60 | varchar |  |  | SI | Classification |
| Q61 | varchar |  |  | SI | The Performance of the Upper Limb (PUL) assessment... |
| Q62 | varchar |  |  | SI | 0 - 42 |
| Q63 | varchar |  |  | SI | Lower scores correspond to higher level of disabil... |
| Q64 | varchar |  |  | SI | 0 - 42: Lower scores correspond to higher level of... |
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