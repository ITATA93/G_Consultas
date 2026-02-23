# questionnaire.QTCFAT

> Frenchay Arm Test (FAT)

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Frenchay Arm Test (FAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Guidelines |
| Q11 | varchar |  |  | SI | Description of tasks: |
| Q12 | varchar |  |  | SI | Patients sit comfortably at a table with hands on ... |
| Q13 | varchar |  |  | SI | - Stabilize a ruler, while drawing a line with a p... |
| Q14 | varchar |  |  | SI | - Grasp a cylinder (12 mm diameter, 5 cm long), se... |
| Q15 | varchar |  |  | SI | - Pick up a glass, half full of water positioned a... |
| Q16 | varchar |  |  | SI | - Remove and replace a sprung clothes peg from a 1... |
| Q17 | varchar |  |  | SI | - Comb hair (or imitate); must comb across top, do... |
| Q18 | varchar |  |  | SI | What to consider before beginning: |
| Q19 | varchar |  |  | SI | Before administering the fat, the clinician should... |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Scoring and score interpretation: |
| Q21 | varchar |  |  | SI | Each item is scored as either pass (=1) or fail (=... |
| Q22 | varchar |  |  | SI | Time: |
| Q23 | varchar |  |  | SI | The fat takes approximately 3 minutes to administe... |
| Q24 | varchar |  |  | SI | Equipment: |
| Q25 | varchar |  |  | SI | - Ruler |
| Q26 | varchar |  |  | SI | - Pencil |
| Q27 | varchar |  |  | SI | - Paper |
| Q28 | varchar |  |  | SI | - Cylinder (12 mm diameter, 5 cm long) |
| Q29 | varchar |  |  | SI | - Glass (half filled with water) |
| Q3 | varchar |  |  | SI | Score |
| Q30 | varchar |  |  | SI | - Clothes peg |
| Q31 | varchar |  |  | SI | - Dowel (15 mm) |
| Q32 | varchar |  |  | SI | - Hair comb |
| Q33 | varchar |  |  | SI | Reference |
| Q34 | varchar |  |  | SI | Heller A, Wade DT, Wood VA, Sunderland A, Hewer RL... |
| Q35 | varchar |  |  | SI | The Frenchay Arm Test assesses function in a singl... |
| Q4 | varchar |  |  | SI | The Frenchay Arm Test assesses function in a singl... |
| Q5 | varchar |  |  | SI | Stabilize a ruler, while drawing a line with a pen... |
| Q6 | varchar |  |  | SI | Grasp a cylinder (12 mm diameter, 5 cm long), set ... |
| Q7 | varchar |  |  | SI | Pick up a glass, half full of water positioned abo... |
| Q8 | varchar |  |  | SI | Remove and replace a sprung clothes peg from a 10 ... |
| Q9 | varchar |  |  | SI | Comb hair (or imitate); must comb across top, down... |
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