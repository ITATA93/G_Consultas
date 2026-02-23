# questionnaire.QTCCDIC

> Chest Drain Insertion and Care

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chest Drain Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Pre-Procedure Checklist |
| Q04 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q05 | varchar |  |  | SI | Aseptic technique used |
| Q06 | varchar |  |  | SI | Skin disinfected with |
| Q07 | varchar |  |  | SI | Other skin disinfection |
| Q08 | varchar |  |  | SI | Local anaesthetic used |
| Q09 | varchar |  |  | SI | Pre-procedure notes |
| Q10 | varchar |  |  | SI | Insertion Details |
| Q11 | varchar |  |  | SI | Insertion reason |
| Q12 | varchar |  |  | SI | Other insertion reason |
| Q13 | date |  |  | SI | Insertion date |
| Q14 | time |  |  | SI | Insertion time |
| Q15 | varchar |  |  | SI | Drain identifier |
| Q16 | varchar |  |  | SI | Catheter type |
| Q17 | numeric |  |  | SI | Size of catheter (French) |
| Q18 | varchar |  |  | SI | Insertion site laterality |
| Q19 | varchar |  |  | SI | Insertion site |
| Q20 | varchar |  |  | SI | Other insertion site |
| Q21 | varchar |  |  | SI | Drainage unit type |
| Q22 | varchar |  |  | SI | Post-insertion checklist |
| Q23 | varchar |  |  | SI | Insertion notes |
| Q24 | varchar |  |  | SI | Inserted by |
| Q25 | varchar |  |  | SI | Assistant |
| Q26 | varchar |  |  | SI | Assessment |
| Q28 | varchar |  |  | SI | Removal Details |
| Q29 | date |  |  | SI | Removal date |
| Q30 | time |  |  | SI | Removal time |
| Q31 | varchar |  |  | SI | Removal reason |
| Q32 | varchar |  |  | SI | Other removal reason |
| Q33 | varchar |  |  | SI | Catheter tip sent for microbiology culture and sen... |
| Q34 | varchar |  |  | SI | Removal notes |
| Q35 | varchar |  |  | SI | Removed by 1 |
| Q36 | varchar |  |  | SI | Removed by 2 |
| Q37 | varchar |  |  | SI | Complications |
| Q38 | varchar |  |  | SI | Complications |
| Q39 | varchar |  |  | SI | Other complications |
| Q40 | varchar |  |  | SI | Complication notes |
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