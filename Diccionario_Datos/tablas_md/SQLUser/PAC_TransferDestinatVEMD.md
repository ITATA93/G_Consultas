# SQLUser.PAC_TransferDestinatVEMD

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VEMD_ParRef | bigint | PK |  | NO | PAC_TransferDestination Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Preferred arm (used for all tests) |
| Q04 | - |  |  | SI | Elbow extension ROM: Right |
| Q05 | - |  |  | SI | ° |
| Q06 | - |  |  | SI | Elbow extension ROM: Left |
| Q07 | - |  |  | SI | ° |
| Q08 | - |  |  | SI | Supination ROM: Right |
| Q09 | - |  |  | SI | Supination ROM: Left |
| Q10 | - |  |  | SI | Start with A to identify starting point for subseq... |
| Q11 | - |  |  | SI | A. Entry Item |
| Q12 | - |  |  | SI | Item 1:  Shoulder abduction both arms above head |
| Q13 | - |  |  | SI | Raise your arms out to the side and above your hea... |
| Q14 | - |  |  | SI | Item 2: Raise both arms to shoulder height (elbows... |
| Q15 | - |  |  | SI | Raise your arms to shoulder level |
| Q16 | - |  |  | SI | Item 3: Shoulder flexion to shoulder height (no we... |
| Q17 | - |  |  | SI | Reach out and touch my hand |
| Q18 | - |  |  | SI | Item 4: Shoulder flexion to shoulder height with 5... |
| Q19 | - |  |  | SI | Reach out and touch my hand |
| Q20 | - |  |  | SI | Item 5: Shoulder flexion above  shoulder height wi... |
| Q21 | - |  |  | SI | Hand on lap - ''Give me the weight |
| Q22 | - |  |  | SI | Item 6: Shoulder flexion above shoulder height wit... |
| Q23 | - |  |  | SI | Hand on lap - ''Give me the weight |
| Q24 | - |  |  | SI | Item 7: Hand(s) to mouth |
| Q25 | - |  |  | SI | Bring the cup to your mouth with one hand |
| Q26 | - |  |  | SI | Item 8: Hands to table from lap |
| Q27 | - |  |  | SI | Bring both hands from lap to table |
| Q28 | - |  |  | SI | Item 9: Move weight on table 100g |
| Q29 | - |  |  | SI | “Move the weight from outside circle to centre cir... |
| Q30 | - |  |  | SI | Item 10: Move weight on table 500g |
| Q31 | - |  |  | SI | Move the weight from outside circle to centre circ... |
| Q32 | - |  |  | SI | Item 11: Move weight on table 1kg |
| Q33 | - |  |  | SI | Move the weight from outside circle to centre circ... |
| Q34 | - |  |  | SI | Item 12: Lift heavy can diagonally |
| Q35 | - |  |  | SI | Lift can from this circle nearest your hand to thi... |
| Q36 | - |  |  | SI | Item 13: Stack of three cans |
| Q37 | - |  |  | SI | Stack these two cans, one at a time on the middle ... |
| Q38 | - |  |  | SI | Item 14: Stack of five cans |
| Q39 | - |  |  | SI | Stack these two additional cans, one at a time on ... |
| Q40 | - |  |  | SI | Item 15: Remove lid from container |
| Q41 | - |  |  | SI | Use your hands to open this container |
| Q42 | - |  |  | SI | Item 16: Tearing paper |
| Q43 | - |  |  | SI | Tear the sheet of paper beginning from here |
| Q44 | - |  |  | SI | Item 17: Tracing path |
| Q45 | - |  |  | SI | Use your pencil to complete the path in one smooth... |
| Q46 | - |  |  | SI | Item 18: Push on light |
| Q47 | - |  |  | SI | Push on the light with the fingers of one hand |
| Q48 | - |  |  | SI | Item 19: Supination |
| Q49 | - |  |  | SI | Pick up the light and turn your hand over |
| Q50 | - |  |  | SI | Item 20: Picking up coins |
| Q51 | - |  |  | SI | Using one hand, Pick up 6 coins, one at a time |
| Q52 | - |  |  | SI | Item 21:  Placing finger on number diagram (precis... |
| Q53 | - |  |  | SI | Using one finger to touch each number on the diagr... |
| Q54 | - |  |  | SI | Item 22:  Pick up 10g weight finger pinch |
| Q55 | - |  |  | SI | Pick up this small weight like this (by body of we... |
| Q56 | - |  |  | SI | Additional Material Item 17: Tracing a path |
| Q57 | - |  |  | SI | Additional Material Item 21: Placing finger on num... |
| Q58 | - |  |  | SI | Starting on the yellow number 1 point to the numbe... |
| Q59 | - |  |  | SI | Score |
| Q60 | - |  |  | SI | Classification |
| Q61 | - |  |  | SI | The Performance of the Upper Limb (PUL) assessment... |
| Q62 | - |  |  | SI | 0 - 42 |
| Q63 | - |  |  | SI | Lower scores correspond to higher level of disabil... |
| Q64 | - |  |  | SI | 0 - 42: Lower scores correspond to higher level of... |
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
| VEMD_Childsub | double |  |  | NO | Childsub |
| VEMD_CreatedDate | date |  |  | SI | Created Date |
| VEMD_CreatedTime | time |  |  | SI | Created Time |
| VEMD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VEMD_DateFrom | date |  |  | SI | DateFrom |
| VEMD_DateTo | date |  |  | SI | DateTo |
| VEMD_RowId | varchar |  |  | NO | - |
| VEMD_UpdatedDate | date |  |  | SI | Updated Date |
| VEMD_UpdatedTime | time |  |  | SI | Updated Time |
| VEMD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| VEMD_VEMDCode | varchar |  |  | SI | VEMDCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*