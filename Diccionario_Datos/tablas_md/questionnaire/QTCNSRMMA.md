# questionnaire.QTCNSRMMA

> Rivermead Motor Assessment

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Rivermead Motor Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | General instructions: |
| Q02 | varchar |  |  | SI | Go through the items in order of difficulty. Score... |
| Q03 | varchar |  |  | SI |  3 consecutive '0' scores for 3 consecutive items. |
| Q04 | varchar |  |  | SI | In the 'Leg and Trunk' section all items should be... |
| Q05 | varchar |  |  | SI | Repeat instructions and demonstrate them to the pa... |
| Q06 | varchar |  |  | SI |  'Gross function' section can be assessed simply b... |
| Q07 | varchar |  |  | SI | Gross function |
| Q08 | varchar |  |  | SI | 1- Sit unsupported: Without holding on, on edge of... |
| Q09 | varchar |  |  | SI | 2- Lying to sitting on side of bed: Using any meth... |
| Q10 | varchar |  |  | SI | 3- Sitting to standing: May use hands to push up: ... |
| Q11 | varchar |  |  | SI | 4- Transfer from weelchair to chair towards unaffe... |
| Q12 | varchar |  |  | SI | 5- Transfer from weelchair to chair towards affect... |
| Q13 | varchar |  |  | SI | 6- Walk 10 m indoors with an aid: Any walking aid.... |
| Q14 | varchar |  |  | SI | 7- Climb stairs independently: Any method. May use... |
| Q15 | varchar |  |  | SI | 8- Walk 10 m indoors without an aid: No stand-by h... |
| Q16 | varchar |  |  | SI | 9- Walk 10m , pick up bean bag from floor, turn an... |
| Q17 | varchar |  |  | SI | 10-  Walk outside 40 m: May use walking aid, calip... |
| Q18 | varchar |  |  | SI | 11- Walk up and down four steps: Patient may use a... |
| Q19 | varchar |  |  | SI | 12- Run 10 m: Must be symmetrical. |
| Q20 | varchar |  |  | SI | 13- Hop on affected leg five times on the spot: Mu... |
| Q21 | varchar |  |  | SI | Gross function Total:  |
| Q22 | varchar |  |  | SI | Arm |
| Q23 | varchar |  |  | SI | 1- Lying, protract shoulder girdle with arm in ele... |
| Q24 | varchar |  |  | SI | 2- Lying, hold extended arm in elevation (some ext... |
| Q25 | varchar |  |  | SI | Elbow must be held within 30 degrees of full exten... |
| Q26 | varchar |  |  | SI | 3-  Flexion and extension of elbow, with arm as in... |
| Q27 | varchar |  |  | SI | 4- Sitting, elbow into side, pronation and supinat... |
| Q28 | varchar |  |  | SI | 5- Reach forward, pick up large ball with both han... |
| Q29 | varchar |  |  | SI |  wrist neutral or extended, and fingers extended t... |
| Q30 | varchar |  |  | SI | 6- Stretch arm forward, pick up tennis ball from t... |
| Q31 | varchar |  |  | SI | extended during each phase. |
| Q32 | varchar |  |  | SI | 7-  Same exercise as in 6 above with pencil Patien... |
| Q33 | varchar |  |  | SI | 8- Pick up a piece of paper from table in front an... |
| Q34 | varchar |  |  | SI | 9- Cut putty with a knife and fork on plate with n... |
| Q35 | varchar |  |  | SI | 10- Stand on spot, maintain upright position, pat ... |
| Q36 | varchar |  |  | SI | 11-  Continuous opposition of thumb and each finge... |
| Q37 | varchar |  |  | SI | 12- Supination and pronation on to palm of unaffec... |
| Q38 | varchar |  |  | SI | but introduces speed. |
| Q39 | varchar |  |  | SI | 13- Standing, with affected arm abducted to 90 deg... |
| Q40 | varchar |  |  | SI | Do not allow flexion at elbow, and wrist must be e... |
| Q41 | varchar |  |  | SI | 14- Place string around head and tie bow at back: ... |
| Q42 | varchar |  |  | SI | 15- 'Pat- a-cake' seven times in 15 sec: Mark cros... |
| Q43 | varchar |  |  | SI | which involves co-ordination, speed, and memory, a... |
| Q44 | varchar |  |  | SI | Arm function total: |
| Q45 | varchar |  |  | SI | Leg and trunk |
| Q46 | varchar |  |  | SI | 1- Roll to affected side: Starting position should... |
| Q47 | varchar |  |  | SI | 2-  Roll to unaffected side: Starting position sho... |
| Q48 | varchar |  |  | SI | 3-  Half-bridging: Starting position -- half-crook... |
| Q49 | varchar |  |  | SI | is completed |
| Q50 | varchar |  |  | SI | 4- Sitting to standing:  May not use arms-- feet m... |
| Q51 | varchar |  |  | SI | 5- Half-crook lying: lift affected leg over side o... |
| Q52 | varchar |  |  | SI |  and knee at 90 degrees while resting on support. ... |
| Q53 | varchar |  |  | SI | 6- Standing, step unaffected leg on and off block:... |
| Q54 | varchar |  |  | SI | 7- Standing, tap ground lightly five times with un... |
| Q55 | varchar |  |  | SI |  affected leg but is more difficult than in 6. |
| Q56 | varchar |  |  | SI | 8- Lying, dorsiflex affected ankle with leg flexed... |
| Q57 | varchar |  |  | SI | 9-  Lying, dorsiflex affected ankle with leg exten... |
| Q58 | varchar |  |  | SI | 10- Stand with affected hip in neutral position, f... |
| Q59 | varchar |  |  | SI | Leg and trunk function total |
| Q60 | varchar |  |  | SI | Gross function: 0-13 |
| Q61 | varchar |  |  | SI | Arm function: 0-15 |
| Q62 | varchar |  |  | SI | Leg and trunk function: 0-10 |
| Q63 | varchar |  |  | SI | The higher the score the less the disability. |
| Q64 | varchar |  |  | SI | Rivermead Motor Assessment is an instrument used t... |
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