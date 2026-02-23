# questionnaire.QTCFCTIC

> Faecal Containment Tube Insertion and Care

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Faecal Containment Tube Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient consented |
| Q04 | varchar |  |  | SI | Barrier precautions used |
| Q05 | varchar |  |  | SI | Confirmed no impaction in the rectum |
| Q06 | varchar |  |  | SI | Confirmed no previous rectal surgery within last 1... |
| Q07 | varchar |  |  | SI | Confirmed no significant haemorrhoids |
| Q08 | varchar |  |  | SI | Confirmed no rectal / anal stricture stenosis or t... |
| Q09 | varchar |  |  | SI | Confirmed no history of inflammatory bowel disease... |
| Q10 | varchar |  |  | SI | Pre - procedure notes |
| Q11 | date |  |  | SI | Insertion date |
| Q12 | time |  |  | SI | Insertion time |
| Q13 | varchar |  |  | SI | Reason for insertion |
| Q14 | varchar |  |  | SI | Other insertion reason |
| Q15 | numeric |  |  | SI | Balloon inflation (mls) |
| Q16 | varchar |  |  | SI | Inserted by |
| Q17 | varchar |  |  | SI | Insertion notes |
| Q19 | date |  |  | SI | Removal date |
| Q20 | time |  |  | SI | Removal time |
| Q21 | varchar |  |  | SI | Removal reason |
| Q22 | varchar |  |  | SI | Other removal reason |
| Q23 | varchar |  |  | SI | Comments |
| Q24 | varchar |  |  | SI | Complications |
| Q25 | varchar |  |  | SI | Other complications |
| Q26 | varchar |  |  | SI | Complication notes |
| Q27 | varchar |  |  | SI | Removed by |
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