# SQLUser.OR_An_Oper_SecSurgItmCnt

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSIC_ParRef | varchar | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Guidelines |
| Q11 | - |  |  | SI | Description of tasks: |
| Q12 | - |  |  | SI | Patients sit comfortably at a table with hands on ... |
| Q13 | - |  |  | SI | - Stabilize a ruler, while drawing a line with a p... |
| Q14 | - |  |  | SI | - Grasp a cylinder (12 mm diameter, 5 cm long), se... |
| Q15 | - |  |  | SI | - Pick up a glass, half full of water positioned a... |
| Q16 | - |  |  | SI | - Remove and replace a sprung clothes peg from a 1... |
| Q17 | - |  |  | SI | - Comb hair (or imitate) |
| Q18 | - |  |  | SI | What to consider before beginning: |
| Q19 | - |  |  | SI | Before administering the fat, the clinician should... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Scoring and score interpretation: |
| Q21 | - |  |  | SI | Each item is scored as either pass (=1) or fail (=... |
| Q22 | - |  |  | SI | Time: |
| Q23 | - |  |  | SI | The fat takes approximately 3 minutes to administe... |
| Q24 | - |  |  | SI | Equipment: |
| Q25 | - |  |  | SI | - Ruler |
| Q26 | - |  |  | SI | - Pencil |
| Q27 | - |  |  | SI | - Paper |
| Q28 | - |  |  | SI | - Cylinder (12 mm diameter, 5 cm long) |
| Q29 | - |  |  | SI | - Glass (half filled with water) |
| Q3 | - |  |  | SI | Score |
| Q30 | - |  |  | SI | - Clothes peg |
| Q31 | - |  |  | SI | - Dowel (15 mm) |
| Q32 | - |  |  | SI | - Hair comb |
| Q33 | - |  |  | SI | Reference |
| Q34 | - |  |  | SI | Heller A, Wade DT, Wood VA, Sunderland A, Hewer RL... |
| Q35 | - |  |  | SI | The Frenchay Arm Test assesses function in a singl... |
| Q4 | - |  |  | SI | The Frenchay Arm Test assesses function in a singl... |
| Q5 | - |  |  | SI | Stabilize a ruler, while drawing a line with a pen... |
| Q6 | - |  |  | SI | Grasp a cylinder (12 mm diameter, 5 cm long), set ... |
| Q7 | - |  |  | SI | Pick up a glass, half full of water positioned abo... |
| Q8 | - |  |  | SI | Remove and replace a sprung clothes peg from a 10 ... |
| Q9 | - |  |  | SI | Comb hair (or imitate) |
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
| SSCI_ItemsCntByRole_DR | bigint |  | FK | SI | Des Ref CTCareProv Items Counted by Role |
| SSCI_ItemsCntDate | date |  |  | SI | Des Ref CTCareProv Items Counted by Role Date |
| SSIC_Childsub | double |  |  | NO | OR_Anaest_Operation Parent Reference
Childsub |
| SSIC_Count | varchar |  |  | SI | Des Ref InitialFinal Standard type Count |
| SSIC_CountCorrect | varchar |  |  | SI | Des Ref YESNO Standard type Count Correct |
| SSIC_CreatedDate | date |  |  | SI | Created Date |
| SSIC_CreatedTime | time |  |  | SI | Created Time |
| SSIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSIC_InstrCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Instrument Count St... |
| SSIC_ItemsCntTime | time |  |  | SI | Des Ref CTCareProv Items Counted by Role Time |
| SSIC_ItemsCountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Items Counted By |
| SSIC_ItemsRecntByRole_DR | bigint |  | FK | SI | Des Ref CTCareProv Items Recounted by Role |
| SSIC_ItemsRecntBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Items Recounted By |
| SSIC_ItemsRecntDate | date |  |  | SI | Des Ref CTCareProv Items Recounted by Date |
| SSIC_ItemsRecntTime | time |  |  | SI | Des Ref CTCareProv Items Recounted by Time |
| SSIC_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| SSIC_Procedure_DR | bigint |  | FK | SI | Des Ref PACStatePPP |
| SSIC_RowId | varchar |  |  | NO | - |
| SSIC_SharpsCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Sharps Count Status |
| SSIC_SurgeonNotified | varchar |  |  | SI | Surgeon Notified |
| SSIC_SwabCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Swab Count Status |
| SSIC_UpdatedDate | date |  |  | SI | Updated Date |
| SSIC_UpdatedTime | time |  |  | SI | Updated Time |
| SSIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SSIC_XRayTaken | varchar |  |  | SI | X-Ray Taken |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*