# SQLUser.OE_OrdCateg

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAT_ParRef | numeric | PK |  | NO | OE_Order Parent Reference |
| CAT_Categ_DR | bigint |  | FK | NO | Des Ref Categ |
| CAT_Qty | double |  |  | SI | Qty |
| CAT_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Level of consciousness |
| Q02 | - |  |  | SI | Observation |
| Q03 | - |  |  | SI | Palpation / Percussion |
| Q04 | - |  |  | SI | Auscultation location |
| Q05 | - |  |  | SI | Adventitious sound |
| Q06 | - |  |  | SI | Breath sound |
| Q07 | - |  |  | SI | Location |
| Q08 | - |  |  | SI | Muscle strength |
| Q09 | - |  |  | SI | Functional Testing |
| Q10 | - |  |  | SI | Rolling |
| Q11 | - |  |  | SI | Come to sit |
| Q12 | - |  |  | SI | Come to stand |
| Q13 | - |  |  | SI | Transferring |
| Q14 | - |  |  | SI | Ambulation status |
| Q15 | - |  |  | SI | Others |
| Q16 | - |  |  | SI | Physical Therapy diagnosis / impression |
| Q17 | - |  |  | SI | Goal of treatment |
| Q18 | - |  |  | SI | Long term goal |
| Q19 | - |  |  | SI | Short term goal |
| Q20 | - |  |  | SI | Re-assessment date |
| Q21 | - |  |  | SI | Plan of treatment and procedure |
| Q22 | - |  |  | SI | Intervention for High risk of fall due to location... |
| Q23 | - |  |  | SI | Post treatment |
| Q24 | - |  |  | SI | Instruction |
| Q25 | - |  |  | SI | Patient and/or family was given and understood abo... |
| Q26 | - |  |  | SI | Need reviewed |
| Q27 | - |  |  | SI | information for fall prevention and safety devices... |
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