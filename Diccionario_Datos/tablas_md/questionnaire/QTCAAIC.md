# questionnaire.QTCAAIC

> Artificial Airway Insertion and Care

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Artificial Airway Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient consented |
| Q04 | varchar |  |  | SI | Barrier precautions used |
| Q05 | varchar |  |  | SI | Artificial airway prior to procedure |
| Q06 | varchar |  |  | SI | History relevant to intubation |
| Q07 | varchar |  |  | SI | Other history relevant to intubation |
| Q08 | varchar |  |  | SI | Pre-oxygenation |
| Q09 | varchar |  |  | SI | Bag mask ventilation |
| Q10 | varchar |  |  | SI | Two handed technique |
| Q11 | date |  |  | SI | Insertion date |
| Q12 | time |  |  | SI | Insertion time |
| Q13 | varchar |  |  | SI | Final airway type |
| Q14 | varchar |  |  | SI | Insertion reason |
| Q15 | varchar |  |  | SI | Other insertion reason |
| Q16 | varchar |  |  | SI | Laryngoscope |
| Q17 | varchar |  |  | SI | Grade of view - direct |
| Q18 | varchar |  |  | SI | Percentage of Glottic Opening (POGO) |
| Q19 | varchar |  |  | SI | Laryngoscope blade |
| Q20 | varchar |  |  | SI | Laryngoscope video blade |
| Q21 | varchar |  |  | SI | Airway adjuncts |
| Q22 | varchar |  |  | SI | ETT location |
| Q23 | varchar |  |  | SI | ETT type |
| Q24 | numeric |  |  | SI | ETT size (mm) |
| Q25 | varchar |  |  | SI | LMA type |
| Q26 | numeric |  |  | SI | LMA size (mm) |
| Q27 | varchar |  |  | SI | Tube passage |
| Q28 | varchar |  |  | SI | Double - lumen tube type |
| Q29 | numeric |  |  | SI | Double - lumen tube size (Fr) |
| Q30 | varchar |  |  | SI | Bronchial blocker type |
| Q31 | varchar |  |  | SI | Number of attempts |
| Q33 | varchar |  |  | SI | Post Procedure |
| Q34 | varchar |  |  | SI | Post-procedure checks |
| Q35 | varchar |  |  | SI | Airway device position checks |
| Q36 | varchar |  |  | SI | Airway device re-positioned |
| Q37 | varchar |  |  | SI | Post-procedure notes |
| Q38 | varchar |  |  | SI | Inserted by |
| Q39 | varchar |  |  | SI | Designation |
| Q40 | varchar |  |  | SI | Specialist present |
| Q41 | varchar |  |  | SI | Designation |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time |
| Q45 | varchar |  |  | SI | Removal reason |
| Q46 | varchar |  |  | SI | Other removal reason |
| Q47 | varchar |  |  | SI | Removed by |
| Q48 | varchar |  |  | SI | Removal notes |
| Q49 | varchar |  |  | SI | Complications |
| Q50 | varchar |  |  | SI | Other complications |
| Q51 | varchar |  |  | SI | Complication notes |
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