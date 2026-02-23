# questionnaire.QTCPEF

> Peritonitis Episode Form

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritonitis Episode Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of infection |
| Q04 | varchar |  |  | SI | This episode a relapse or recurrence |
| Q05 | varchar |  |  | SI | Relapse = Peritonitis within 4 weeks of completion... |
| Q06 | varchar |  |  | SI | Recurrence = Peritonitis within 4 weeks of complet... |
| Q07 | varchar |  |  | SI | Organism information |
| Q08 | varchar |  |  | SI | Organism |
| Q09 | varchar |  |  | SI | Other organism notes |
| Q10 | varchar |  |  | SI | Drug treatments |
| Q11 | varchar |  |  | SI | Antifungal therapy |
| Q12 | varchar |  |  | SI | Antibiotics |
| Q13 | varchar |  |  | SI | Initial antibiotic regimen |
| Q14 | varchar |  |  | SI | Final antibiotic regimen |
| Q15 | varchar |  |  | SI | First treatment |
| Q16 | varchar |  |  | SI | Other first treatment antibiotic |
| Q17 | varchar |  |  | SI | Second treatment |
| Q18 | varchar |  |  | SI | Other second treatment antibiotic |
| Q19 | varchar |  |  | SI | Third treatment |
| Q20 | varchar |  |  | SI | Other third treatment antibiotic |
| Q21 | varchar |  |  | SI | Date of last dose |
| Q22 | varchar |  |  | SI | Treatment notes |
| Q23 | varchar |  |  | SI | First treatment - Initial regimen |
| Q24 | varchar |  |  | SI | Other second treatment antibiotic - Initial regime... |
| Q25 | varchar |  |  | SI | Second treatment - Initial regimen |
| Q26 | varchar |  |  | SI | Other second treatment antibiotic - Initial regime... |
| Q27 | varchar |  |  | SI | Third treatment - Initial regimen |
| Q28 | varchar |  |  | SI | Other third treatment antibiotic - Initial regimen |
| Q29 | date |  |  | SI | Date of last dose |
| Q30 | varchar |  |  | SI | Initial treatment notes |
| Q31 | varchar |  |  | SI | First treatment - Final antibiotic regimen |
| Q32 | varchar |  |  | SI | Other first treatment antibiotic - final antibioti... |
| Q33 | varchar |  |  | SI | Second treatment - final antibiotic regimen |
| Q34 | varchar |  |  | SI | Other second treatment antibiotic - final antibiot... |
| Q35 | varchar |  |  | SI | Third treatment - Final antibiotic regimen |
| Q36 | varchar |  |  | SI | Other third treatment antibiotic - Final antibioti... |
| Q37 | date |  |  | SI | Date of last dose - final antibiotic regimen |
| Q38 | varchar |  |  | SI | Final treatment notes |
| Q39 | varchar |  |  | SI | Peritoneal dialysis solutions at time of infection |
| Q40 | varchar |  |  | SI | Glucose |
| Q41 | varchar |  |  | SI | Icodextrin |
| Q42 | varchar |  |  | SI | Low glucose degradation product (GDP) |
| Q43 | varchar |  |  | SI | Other (please specify) |
| Q44 | varchar |  |  | SI | Outcome |
| Q45 | varchar |  |  | SI | Overnight hospitalisation |
| Q46 | numeric |  |  | SI | Number of nights, if applicable |
| Q47 | varchar |  |  | SI | Catheter removed |
| Q48 | date |  |  | SI | Date catheter removed, if applicable |
| Q49 | varchar |  |  | SI | Interim haemodialysis |
| Q50 | date |  |  | SI | First dialysis date, if applicable |
| Q51 | date |  |  | SI | Last dialysis date, if applicable |
| Q52 | varchar |  |  | SI | Permanent haemodialysis (HD) |
| Q53 | date |  |  | SI | Date of permanent HD, if applicable |
| Q54 | varchar |  |  | SI | Treatment and outcome notes |
| Q55 | varchar |  |  | SI | Dummy1 |
| Q56 | varchar |  |  | SI | Initial antibiotic regimen |
| Q57 | varchar |  |  | SI | Initial antibiotic regimen |
| Q58 | varchar |  |  | SI | Initial antibiotic regimen |
| Q59 | varchar |  |  | SI | Initial antibiotic regimen |
| Q60 | varchar |  |  | SI | Initial antibiotic regimen |
| Q61 | varchar |  |  | SI | Initial antibiotic regimen |
| Q62 | varchar |  |  | SI | Initial antibiotic regimen |
| Q63 | varchar |  |  | SI | Initial antibiotic regimen |
| Q64 | varchar |  |  | SI | Final antibiotic regimen |
| Q65 | varchar |  |  | SI | Final antibiotic regimen |
| Q66 | varchar |  |  | SI | Final antibiotic regimen |
| Q67 | varchar |  |  | SI | Final antibiotic regimen |
| Q68 | varchar |  |  | SI | Final antibiotic regimen |
| Q69 | varchar |  |  | SI | Final antibiotic regimen |
| Q70 | varchar |  |  | SI | Final antibiotic regimen |
| Q71 | varchar |  |  | SI | Final antibiotic regimen |
| Q72 | varchar |  |  | SI | First treatment - Initial regimen |
| Q73 | varchar |  |  | SI | Second treatment - Initial regimen |
| Q74 | varchar |  |  | SI | Third treatment - Initial regimen |
| Q75 | varchar |  |  | SI | First treatment - Final antibiotic regimen |
| Q76 | varchar |  |  | SI | Second treatment - final antibiotic regimen |
| Q77 | varchar |  |  | SI | Third treatment - Final antibiotic regimen |
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