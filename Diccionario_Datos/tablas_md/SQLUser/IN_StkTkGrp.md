# SQLUser.IN_StkTkGrp

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TG_ParRef | bigint | PK |  | NO | IN_StkTk Parent Reference |
| Q01 | - |  |  | SI | Current Sport(s) - Type |
| Q02 | - |  |  | SI | Current Sport - Level of participation |
| Q03 | - |  |  | SI | Years of experience at this level |
| Q04 | - |  |  | SI | Years of education completed |
| Q05 | - |  |  | SI | Repeated any school years |
| Q06 | - |  |  | SI | School History (tick all that apply) |
| Q07 | - |  |  | SI | Sports and school history comments |
| Q08 | - |  |  | SI | Impact Testing History |
| Q09 | - |  |  | SI | Baseline testing Date |
| Q10 | - |  |  | SI | Baseline testing place |
| Q11 | - |  |  | SI | Post Injury testing Date |
| Q12 | - |  |  | SI | Post Injury testing place |
| Q13 | - |  |  | SI | Memory Questions |
| Q14 | - |  |  | SI | Remember things that people just told you |
| Q15 | - |  |  | SI | Remember things that happened in the past |
| Q16 | - |  |  | SI | Remember to do things (keep appointments / take me... |
| Q17 | - |  |  | SI | Remember the day of the week	 |
| Q18 | - |  |  | SI | Concentrate |
| Q19 | - |  |  | SI | Think quickly |
| Q20 | - |  |  | SI | Solve everyday problems |
| Q21 | - |  |  | SI | Say the name of someone in front of you	 |
| Q22 | - |  |  | SI | Understand what is being said in a conversation wi... |
| Q23 | - |  |  | SI | Reply to questions	 |
| Q24 | - |  |  | SI | Correctly name objects	 |
| Q25 | - |  |  | SI | Participate in a conversation with a group of peop... |
| Q26 | - |  |  | SI | Call a person on the telephone, including selectin... |
| Q27 | - |  |  | SI | Have you receive any treatment for symptoms since ... |
| Q28 | - |  |  | SI | Treatment details	 |
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
| TG_Childsub | double |  |  | NO | Childsub |
| TG_RowId | varchar |  |  | NO | - |
| TG_StkGroup_DR | bigint |  | FK | SI | Des Ref StkGroup |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*