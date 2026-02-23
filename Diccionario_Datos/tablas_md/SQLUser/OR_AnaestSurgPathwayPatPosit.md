# SQLUser.OR_AnaestSurgPathwayPatPosit

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATPOS_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| PATPOS_Childsub | numeric |  |  | NO | Childsub |
| PATPOS_OperPosit_DR | bigint |  | FK | NO |  Des Ref ORC_OperPosition |
| PATPOS_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Indication |
| Q04 | - |  |  | SI | Other indication |
| Q05 | - |  |  | SI | Known cirrhosis |
| Q06 | - |  |  | SI | Ascites |
| Q07 | - |  |  | SI | Currently pregnant |
| Q08 | - |  |  | SI | Mass liver lesion |
| Q09 | - |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q10 | - |  |  | SI | Previous fibroscan |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Previous liver biopsy |
| Q13 | - |  |  | SI | Date |
| Q14 | - |  |  | SI | Recent liver ultrasound |
| Q15 | - |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q16 | - |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q17 | - |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q18 | - |  |  | SI | Exclusion Criteria - Do not proceed with the Fibro... |
| Q19 | - |  |  | SI | Exclusion Criteria |
| Q20 | - |  |  | SI | Meets exclusion criteria - Do not proceed with fib... |
| Q21 | - |  |  | SI | Has 'Yes' been selected as an answer, to any of th... |
| Q22 | - |  |  | SI | Meets exclusion criteria - Do not proceed with fib... |
| Q23 | - |  |  | SI | Other tests |
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