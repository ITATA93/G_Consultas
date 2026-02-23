# questionnaire.QTCMMAS

> Modified Motor Assessment Scale (MMAS) (Loewen and Anderson)

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Motor Assessment Scale (MMAS) (Loewen and Anderson)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Stage of assessment |
| Q04 | varchar |  |  | SI | Side of assessment	 |
| Q05 | varchar |  |  | SI | Supine to side-lying (onto intact side) |
| Q06 | varchar |  |  | SI | Supine to sitting over side of bed |
| Q07 | varchar |  |  | SI | Balance sitting	 |
| Q08 | varchar |  |  | SI | Sitting to standing |
| Q09 | varchar |  |  | SI | Walking |
| Q10 | varchar |  |  | SI | Upper arm function |
| Q11 | varchar |  |  | SI | Hand movements |
| Q12 | varchar |  |  | SI | Advanced hand activities |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | Physical therapist |
| Q15 | date |  |  | SI | Date and time of assessment |
| Q16 | varchar |  |  | SI | Occupational therapist |
| Q17 | date |  |  | SI | Date and time of assessment |
| Q18 | time |  |  | SI | Time |
| Q19 | varchar |  |  | SI | • The test should preferably be carried out in a q... |
| Q20 | varchar |  |  | SI | • The test should be carried out when patient is m... |
| Q21 | varchar |  |  | SI | Record should be made if patient is under the infl... |
| Q22 | varchar |  |  | SI | • Patient should be dressed in suitable street clo... |
| Q23 | varchar |  |  | SI | • Each item is recorded on a scale of 0 to 6. |
| Q24 | varchar |  |  | SI | • All items are to be performed independently by t... |
| Q25 | varchar |  |  | SI | • Patient should be scored on their best performan... |
| Q26 | varchar |  |  | SI | Because the scale is designed to score patient's b... |
| Q27 | varchar |  |  | SI | • Sensitivity to the patient is necessary to enabl... |
| Q28 | varchar |  |  | SI | • Instructions should be repeated and demonstratio... |
| Q29 | varchar |  |  | SI | • The order of administration of items can be vari... |
| Q30 | varchar |  |  | SI | • If patient becomes emotionally labile at any sta... |
| Q31 | varchar |  |  | SI | The examiner should cease testing, and rescore thi... |
| Q32 | varchar |  |  | SI | • If performance is scored differently on left and... |
| Q33 | varchar |  |  | SI | The patient should be informed when being timed. |
| Q34 | varchar |  |  | SI | Equipment required |
| Q35 | varchar |  |  | SI | • Low wide plinth |
| Q36 | varchar |  |  | SI | • Stopwatch |
| Q37 | varchar |  |  | SI | • Polystyrene cup |
| Q38 | varchar |  |  | SI | • Eight jellybeans |
| Q39 | varchar |  |  | SI | • Two teacups |
| Q40 | varchar |  |  | SI | • Rubber ball approximately 14 - cm (5 - in) diame... |
| Q41 | varchar |  |  | SI | • Stool |
| Q42 | varchar |  |  | SI | • Comb |
| Q43 | varchar |  |  | SI | • Top of a pen |
| Q44 | varchar |  |  | SI | • Table |
| Q45 | varchar |  |  | SI | • Dessert spoon and water |
| Q46 | varchar |  |  | SI | • Pen |
| Q47 | varchar |  |  | SI | • Prepared sheet for drawing lines |
| Q48 | varchar |  |  | SI | • Cylindrical object such as a jar |
| Q49 | varchar |  |  | SI | 0 - 40 |
| Q50 | varchar |  |  | SI | The higher the score – the higher functioning the ... |
| Q51 | time |  |  | SI | Time |
| Q52 | varchar |  |  | SI | The Motor Assessment Scale (MAS) is a performance ... |
| Q53 | varchar |  |  | SI | (1988) modified item descriptions and deleted the ... |
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