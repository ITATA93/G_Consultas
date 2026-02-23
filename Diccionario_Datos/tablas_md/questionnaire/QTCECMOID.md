# questionnaire.QTCECMOID

> ECMO Initial Documentation

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ECMO Initial Documentation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Activity |
| Q02 | varchar |  |  | SI | Mechanical circulatory support type |
| Q03 | varchar |  |  | SI | Cannulation type |
| Q04 | varchar |  |  | SI | Arterial Site |
| Q05 | varchar |  |  | SI | Arterial cannula size |
| Q06 | varchar |  |  | SI | Venous site |
| Q07 | varchar |  |  | SI | Others |
| Q08 | varchar |  |  | SI | Venous cannula size |
| Q09 | varchar |  |  | SI | Veno-venous in venous site |
| Q10 | varchar |  |  | SI | Veno-venous in venous cannula size |
| Q11 | varchar |  |  | SI | Veno-venous out venous site |
| Q12 | varchar |  |  | SI | Veno-venous out venous cannula size |
| Q13 | varchar |  |  | SI | Oxygenator type |
| Q14 | date |  |  | SI | ECMO insertion date |
| Q15 | time |  |  | SI | ECMO insertion time |
| Q16 | date |  |  | SI | ECMO discontinuation date |
| Q17 | time |  |  | SI | ECMO discontinuation time |
| Q18 | varchar |  |  | SI | ECMO know, insertion date |
| Q19 | varchar |  |  | SI | RVAD, inflow cannula site |
| Q20 | varchar |  |  | SI | RVAD, inflow cannula size |
| Q21 | varchar |  |  | SI | RVAD, outflow cannula site |
| Q22 | varchar |  |  | SI | RVAD, outflow cannula size |
| Q23 | varchar |  |  | SI | LVAD, inflow cannula site |
| Q24 | varchar |  |  | SI | LVAD, inflow cannula size |
| Q25 | varchar |  |  | SI | LVAD, outflow cannula site |
| Q26 | varchar |  |  | SI | LVAD, outflow cannula size |
| Q27 | date |  |  | SI | ECMO known, date of insertion |
| Q28 | varchar |  |  | SI | Procedure preparation |
| Q29 | varchar |  |  | SI | Sterile field |
| Q30 | varchar |  |  | SI | MBP compliance |
| Q31 | varchar |  |  | SI | Non compliant MBP |
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