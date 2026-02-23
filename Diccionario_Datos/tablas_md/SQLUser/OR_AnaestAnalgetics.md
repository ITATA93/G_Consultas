# SQLUser.OR_AnaestAnalgetics

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAAN_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANAAN_Childsub | double |  |  | NO | Childsub |
| ANAAN_RowId | varchar |  |  | NO | - |
| ANAAN_Type_DR | bigint |  | FK | SI | Des Ref PACAnalgetics |
| ChildQ18DR | - |  |  | SI | Child Reference: Faecal containment device assessm... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient consented |
| Q04 | - |  |  | SI | Barrier precautions used |
| Q05 | - |  |  | SI | Confirmed no impaction in the rectum |
| Q06 | - |  |  | SI | Confirmed no previous rectal surgery within last 1... |
| Q07 | - |  |  | SI | Confirmed no significant haemorrhoids |
| Q08 | - |  |  | SI | Confirmed no rectal / anal stricture stenosis or t... |
| Q09 | - |  |  | SI | Confirmed no history of inflammatory bowel disease... |
| Q10 | - |  |  | SI | Pre - procedure notes |
| Q11 | - |  |  | SI | Insertion date |
| Q12 | - |  |  | SI | Insertion time |
| Q13 | - |  |  | SI | Reason for insertion |
| Q14 | - |  |  | SI | Other insertion reason |
| Q15 | - |  |  | SI | Balloon inflation (mls) |
| Q16 | - |  |  | SI | Inserted by |
| Q17 | - |  |  | SI | Insertion notes |
| Q19 | - |  |  | SI | Removal date |
| Q20 | - |  |  | SI | Removal time |
| Q21 | - |  |  | SI | Removal reason |
| Q22 | - |  |  | SI | Other removal reason |
| Q23 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | Complications |
| Q25 | - |  |  | SI | Other complications |
| Q26 | - |  |  | SI | Complication notes |
| Q27 | - |  |  | SI | Removed by |
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