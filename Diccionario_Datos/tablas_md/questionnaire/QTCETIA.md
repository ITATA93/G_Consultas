# questionnaire.QTCETIA

> Endotracheal Intubation Assessment

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endotracheal Intubation Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Insertion details |
| Q10 | varchar |  |  | SI | Was the rapid sequence intubation technique used? |
| Q11 | varchar |  |  | SI | Pretreatment medications |
| Q12 | varchar |  |  | SI | Induction medications |
| Q13 | varchar |  |  | SI | Neuromuscular blockers medications |
| Q14 | varchar |  |  | SI | Cricoid pressure applied |
| Q15 | varchar |  |  | SI | Visualization / Guidance |
| Q16 | numeric |  |  | SI | Number of attempts |
| Q17 | varchar |  |  | SI | Tube type size and type |
| Q18 | varchar |  |  | SI | Pre-procedural checklist completed? |
| Q19 | varchar |  |  | SI | Cricothyrotomy procedure notes |
| Q2 | varchar |  |  | SI | Activity |
| Q20 | varchar |  |  | SI | Tracheostomy procedure notes |
| Q21 | varchar |  |  | SI | Was the intubation successful? |
| Q22 | varchar |  |  | SI | Placement confirmed by |
| Q23 | varchar |  |  | SI | Status of the patient |
| Q24 | varchar |  |  | SI | Additional procedure notes |
| Q25 | varchar |  |  | SI | Assessment |
| Q28 | varchar |  |  | SI | Discontinuation details |
| Q29 | date |  |  | SI | Discontinue date and time |
| Q3 | date |  |  | SI | Insertion date and time |
| Q30 | time |  |  | SI | Discontinue time |
| Q31 | varchar |  |  | SI | Removal type |
| Q32 | varchar |  |  | SI | Complications |
| Q33 | varchar |  |  | SI | Care provider performing insertion |
| Q34 | varchar |  |  | SI | Care provider removing tube |
| Q35 | varchar |  |  | SI | Content Copyright / Licensing Not Required |
| Q36 | date |  |  | SI | Date |
| Q37 | time |  |  | SI | Time |
| Q38 | varchar |  |  | SI | Total days of insertion |
| Q39 | varchar |  |  | SI | Ventilator Associated Pneumonia Infection Type |
| Q4 | time |  |  | SI | Insertion time |
| Q5 | varchar |  |  | SI | Total days of insertion |
| Q6 | varchar |  |  | SI | Procedure type |
| Q7 | varchar |  |  | SI | Procedure indication |
| Q8 | varchar |  |  | SI | Intubation type |
| Q9 | varchar |  |  | SI | Airway and oxygen management during procedure |
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