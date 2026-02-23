# SQLUser.OR_An_Oper_Assistant

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPAS_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| ChildQ27DR | - |  |  | SI | Child Reference: Ventilator associated pneumonia  ... |
| OPAS_Assist_DR | varchar |  | FK | NO | Assistant Des Ref to CTCP |
| OPAS_Childsub | numeric |  |  | NO | Childsub |
| OPAS_RowId | varchar |  |  | NO | - |
| Q1 | - |  |  | SI | Insertion details |
| Q10 | - |  |  | SI | Was the rapid sequence intubation technique used? |
| Q11 | - |  |  | SI | Pretreatment medications |
| Q12 | - |  |  | SI | Induction medications |
| Q13 | - |  |  | SI | Neuromuscular blockers medications |
| Q14 | - |  |  | SI | Cricoid pressure applied |
| Q15 | - |  |  | SI | Visualization / Guidance |
| Q16 | - |  |  | SI | Number of attempts |
| Q17 | - |  |  | SI | Tube type size and type |
| Q18 | - |  |  | SI | Pre-procedural checklist completed? |
| Q19 | - |  |  | SI | Cricothyrotomy procedure notes |
| Q2 | - |  |  | SI | Activity |
| Q20 | - |  |  | SI | Tracheostomy procedure notes |
| Q21 | - |  |  | SI | Was the intubation successful? |
| Q22 | - |  |  | SI | Placement confirmed by |
| Q23 | - |  |  | SI | Status of the patient |
| Q24 | - |  |  | SI | Additional procedure notes |
| Q25 | - |  |  | SI | Assessment |
| Q28 | - |  |  | SI | Discontinuation details |
| Q29 | - |  |  | SI | Discontinue date and time |
| Q3 | - |  |  | SI | Insertion date and time |
| Q30 | - |  |  | SI | Discontinue time |
| Q31 | - |  |  | SI | Removal type |
| Q32 | - |  |  | SI | Complications |
| Q33 | - |  |  | SI | Care provider performing insertion |
| Q34 | - |  |  | SI | Care provider removing tube |
| Q35 | - |  |  | SI | Content Copyright / Licensing Not Required |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Time |
| Q38 | - |  |  | SI | Total days of insertion |
| Q39 | - |  |  | SI | Ventilator Associated Pneumonia Infection Type |
| Q4 | - |  |  | SI | Insertion time |
| Q5 | - |  |  | SI | Total days of insertion |
| Q6 | - |  |  | SI | Procedure type |
| Q7 | - |  |  | SI | Procedure indication |
| Q8 | - |  |  | SI | Intubation type |
| Q9 | - |  |  | SI | Airway and oxygen management during procedure |
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