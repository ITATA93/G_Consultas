# SQLUser.OE_OrdResolveDose

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RD_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| Q01 | - |  |  | SI | Level of consciousness |
| Q02 | - |  |  | SI | Observation |
| Q03 | - |  |  | SI | Muscle tone |
| Q04 | - |  |  | SI | Muscle length |
| Q05 | - |  |  | SI | Sensation |
| Q06 | - |  |  | SI | Muscle strength |
| Q07 | - |  |  | SI | Functional Testing |
| Q08 | - |  |  | SI | Rolling |
| Q09 | - |  |  | SI | Come to sit |
| Q10 | - |  |  | SI | Come to stand |
| Q11 | - |  |  | SI | Balance Testing |
| Q12 | - |  |  | SI | Sitting position Static |
| Q13 | - |  |  | SI | Sitting position Dynamic |
| Q14 | - |  |  | SI | Standing position Static |
| Q15 | - |  |  | SI | Standing position Dynamic |
| Q16 | - |  |  | SI | Gait analysis |
| Q17 | - |  |  | SI | Physical Therapy diagnosis / impression |
| Q18 | - |  |  | SI | Goal of treatment |
| Q19 | - |  |  | SI | Long term goal |
| Q20 | - |  |  | SI | Short term goal |
| Q21 | - |  |  | SI | Re-assessment date |
| Q22 | - |  |  | SI | Plan of treatment and procedure |
| Q23 | - |  |  | SI | Intervention for High risk of fall due to location... |
| Q24 | - |  |  | SI | information for fall prevention and safety devices... |
| Q25 | - |  |  | SI | Post treatment |
| Q26 | - |  |  | SI | Instruction |
| Q27 | - |  |  | SI | Patient and/or family was given and understood abo... |
| Q28 | - |  |  | SI | Need reviewed |
| Q29 | - |  |  | SI | Others |
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
| RD_Childsub | double |  |  | NO | Childsub |
| RD_Dose | double |  |  | SI | - |
| RD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*