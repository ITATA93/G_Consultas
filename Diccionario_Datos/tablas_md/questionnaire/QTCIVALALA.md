# questionnaire.QTCIVALALA

> Arterial Line Assessment

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Arterial Line Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Activity |
| Q04 | varchar |  |  | SI | Arterial line present |
| Q06 | time |  |  | SI | Insertion time |
| Q07 | varchar |  |  | SI | Total days of insertion |
| Q08 | varchar |  |  | SI | Procedure type |
| Q09 | varchar |  |  | SI | Catheter type |
| Q10 | varchar |  |  | SI | Laterality |
| Q11 | varchar |  |  | SI | Site |
| Q12 | varchar |  |  | SI | Size |
| Q13 | numeric |  |  | SI | Length |
| Q14 | varchar |  |  | SI | Reason for insertion |
| Q15 | varchar |  |  | SI | Patient identified |
| Q16 | varchar |  |  | SI | Insertion unit |
| Q17 | varchar |  |  | SI | Performing provider |
| Q18 | varchar |  |  | SI | Assisting in insertion |
| Q19 | varchar |  |  | SI | Procedure preparation |
| Q20 | varchar |  |  | SI | Sterile field maintained |
| Q21 | varchar |  |  | SI | Maximal sterile barrier precautions compliance |
| Q22 | varchar |  |  | SI | Non - compliant maximal sterile barrier precaution... |
| Q23 | varchar |  |  | SI | Procedure result |
| Q24 | numeric |  |  | SI | Number of attempts |
| Q25 | varchar |  |  | SI | Comment |
| Q28 | varchar |  |  | SI | Collateral flow assured |
| Q29 | varchar |  |  | SI | Allen test |
| Q30 | date |  |  | SI | Discontinue date and time |
| Q31 | time |  |  | SI | Discontinue time |
| Q32 | varchar |  |  | SI | Care provider discontinued the line |
| Q33 | varchar |  |  | SI | Removal reason |
| Q34 | varchar |  |  | SI | Unexpected events |
| Q35 | varchar |  |  | SI | Removal result |
| Q36 | varchar |  |  | SI | Removal result |
| Q37 | numeric |  |  | SI | Direct pressure duration (Minutes) |
| Q38 | date |  |  | SI | Insertion date and time |
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