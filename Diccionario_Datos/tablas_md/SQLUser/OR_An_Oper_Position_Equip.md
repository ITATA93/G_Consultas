# SQLUser.OR_An_Oper_Position_Equip

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POSEQ_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| POSEQ_Childsub | double |  |  | NO | Childsub |
| POSEQ_RowId | varchar |  |  | NO | - |
| POSEQ_Type_DR | bigint |  | FK | SI | Des Ref PACAnalgetics |
| Q01 | - |  |  | SI | Grading Scale |
| Q02 | - |  |  | SI | Skin Colour |
| Q03 | - |  |  | SI | Skin Temperature |
| Q04 | - |  |  | SI | Skin Integrity |
| Q05 | - |  |  | SI | Absent |
| Q06 | - |  |  | SI | Normal |
| Q07 | - |  |  | SI | Normal |
| Q08 | - |  |  | SI | Unbroken |
| Q09 | - |  |  | SI | Oedema |
| Q10 | - |  |  | SI | Pink |
| Q11 | - |  |  | SI | Warm |
| Q12 | - |  |  | SI | Blistered |
| Q13 | - |  |  | SI | Non-pitting |
| Q14 | - |  |  | SI | Red |
| Q15 | - |  |  | SI | Hot |
| Q16 | - |  |  | SI | Superficial skin loss |
| Q17 | - |  |  | SI | Pitting |
| Q18 | - |  |  | SI | Blanched centre |
| Q19 | - |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q20 | - |  |  | SI | Blackened |
| Q21 | - |  |  | SI | Tissue loss muscle / bone / exposure, deep crater ... |
| Q22 | - |  |  | SI | Mobility |
| Q23 | - |  |  | SI | Pain |
| Q24 | - |  |  | SI | Fever |
| Q25 | - |  |  | SI | Grading Scale |
| Q26 | - |  |  | SI | 0 |
| Q27 | - |  |  | SI | 1 |
| Q28 | - |  |  | SI | 2 |
| Q29 | - |  |  | SI | 3 |
| Q30 | - |  |  | SI | 4 |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
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