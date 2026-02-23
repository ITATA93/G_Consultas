# SQLUser.PAC_PalliativeCareState

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCS_RowId | bigint | PK |  | NO | - |
| PCS_Code | varchar |  |  | NO | Code |
| PCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PCS_CreatedDate | date |  |  | SI | Created Date |
| PCS_CreatedTime | time |  |  | SI | Created Time |
| PCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PCS_DateFrom | date |  |  | SI | Date From |
| PCS_DateTo | date |  |  | SI | Date To |
| PCS_Desc | varchar |  |  | NO | Description |
| PCS_NationCode | varchar |  |  | SI | National Code |
| PCS_NumericVal | double |  |  | SI | Numeric Value |
| PCS_Owner | varchar |  |  | SI | Owner |
| PCS_UpdatedDate | date |  |  | SI | Updated Date |
| PCS_UpdatedTime | time |  |  | SI | Updated Time |
| PCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | General instructions: |
| Q02 | - |  |  | SI | Go through the items in order of difficulty. Score... |
| Q03 | - |  |  | SI | 3 consecutive '0' scores for 3 consecutive items. |
| Q04 | - |  |  | SI | In the 'Leg and Trunk' section all items should be... |
| Q05 | - |  |  | SI | Repeat instructions and demonstrate them to the pa... |
| Q06 | - |  |  | SI | Gross function' section can be assessed simply by ... |
| Q07 | - |  |  | SI | Gross function |
| Q08 | - |  |  | SI | 1- Sit unsupported: Without holding on, on edge of... |
| Q09 | - |  |  | SI | 2- Lying to sitting on side of bed: Using any meth... |
| Q10 | - |  |  | SI | 3- Sitting to standing: May use hands to push up: ... |
| Q11 | - |  |  | SI | 4- Transfer from weelchair to chair towards unaffe... |
| Q12 | - |  |  | SI | 5- Transfer from weelchair to chair towards affect... |
| Q13 | - |  |  | SI | 6- Walk 10 m indoors with an aid: Any walking aid.... |
| Q14 | - |  |  | SI | 7- Climb stairs independently: Any method. May use... |
| Q15 | - |  |  | SI | 8- Walk 10 m indoors without an aid: No stand-by h... |
| Q16 | - |  |  | SI | 9- Walk 10m , pick up bean bag from floor, turn an... |
| Q17 | - |  |  | SI | 10-  Walk outside 40 m: May use walking aid, calip... |
| Q18 | - |  |  | SI | 11- Walk up and down four steps: Patient may use a... |
| Q19 | - |  |  | SI | 12- Run 10 m: Must be symmetrical. |
| Q20 | - |  |  | SI | 13- Hop on affected leg five times on the spot: Mu... |
| Q21 | - |  |  | SI | Gross function Total: |
| Q22 | - |  |  | SI | Arm |
| Q23 | - |  |  | SI | 1- Lying, protract shoulder girdle with arm in ele... |
| Q24 | - |  |  | SI | 2- Lying, hold extended arm in elevation (some ext... |
| Q25 | - |  |  | SI | Elbow must be held within 30 degrees of full exten... |
| Q26 | - |  |  | SI | 3-  Flexion and extension of elbow, with arm as in... |
| Q27 | - |  |  | SI | 4- Sitting, elbow into side, pronation and supinat... |
| Q28 | - |  |  | SI | 5- Reach forward, pick up large ball with both han... |
| Q29 | - |  |  | SI | wrist neutral or extended, and fingers extended th... |
| Q30 | - |  |  | SI | 6- Stretch arm forward, pick up tennis ball from t... |
| Q31 | - |  |  | SI | extended during each phase. |
| Q32 | - |  |  | SI | 7-  Same exercise as in 6 above with pencil Patien... |
| Q33 | - |  |  | SI | 8- Pick up a piece of paper from table in front an... |
| Q34 | - |  |  | SI | 9- Cut putty with a knife and fork on plate with n... |
| Q35 | - |  |  | SI | 10- Stand on spot, maintain upright position, pat ... |
| Q36 | - |  |  | SI | 11-  Continuous opposition of thumb and each finge... |
| Q37 | - |  |  | SI | 12- Supination and pronation on to palm of unaffec... |
| Q38 | - |  |  | SI | but introduces speed. |
| Q39 | - |  |  | SI | 13- Standing, with affected arm abducted to 90 deg... |
| Q40 | - |  |  | SI | Do not allow flexion at elbow, and wrist must be e... |
| Q41 | - |  |  | SI | 14- Place string around head and tie bow at back: ... |
| Q42 | - |  |  | SI | 15- 'Pat- a-cake' seven times in 15 sec: Mark cros... |
| Q43 | - |  |  | SI | which involves co-ordination, speed, and memory, a... |
| Q44 | - |  |  | SI | Arm function total: |
| Q45 | - |  |  | SI | Leg and trunk |
| Q46 | - |  |  | SI | 1- Roll to affected side: Starting position should... |
| Q47 | - |  |  | SI | 2-  Roll to unaffected side: Starting position sho... |
| Q48 | - |  |  | SI | 3-  Half-bridging: Starting position -- half-crook... |
| Q49 | - |  |  | SI | is completed |
| Q50 | - |  |  | SI | 4- Sitting to standing:  May not use arms-- feet m... |
| Q51 | - |  |  | SI | 5- Half-crook lying: lift affected leg over side o... |
| Q52 | - |  |  | SI | and knee at 90 degrees while resting on support. M... |
| Q53 | - |  |  | SI | 6- Standing, step unaffected leg on and off block:... |
| Q54 | - |  |  | SI | 7- Standing, tap ground lightly five times with un... |
| Q55 | - |  |  | SI | affected leg but is more difficult than in 6. |
| Q56 | - |  |  | SI | 8- Lying, dorsiflex affected ankle with leg flexed... |
| Q57 | - |  |  | SI | 9-  Lying, dorsiflex affected ankle with leg exten... |
| Q58 | - |  |  | SI | 10- Stand with affected hip in neutral position, f... |
| Q59 | - |  |  | SI | Leg and trunk function total |
| Q60 | - |  |  | SI | Gross function: 0-13 |
| Q61 | - |  |  | SI | Arm function: 0-15 |
| Q62 | - |  |  | SI | Leg and trunk function: 0-10 |
| Q63 | - |  |  | SI | The higher the score the less the disability. |
| Q64 | - |  |  | SI | Rivermead Motor Assessment is an instrument used t... |
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