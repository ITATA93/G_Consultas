# questionnaire.QTCFICP

> Food Intake Chart - Paediatric

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Food Intake Chart - Paediatric

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Breakfast - Requires food / eating behaviour monit... |
| Q04 | varchar |  |  | SI | Breakfast - Type of food offered |
| Q05 | varchar |  |  | SI | Breakfast - Amount of food offered |
| Q06 | varchar |  |  | SI | Breakfast - Amount eaten |
| Q07 | numeric |  |  | SI | Breakfast - Oral intake (ml) |
| Q08 | varchar |  |  | SI | Breakfast notes |
| Q09 | varchar |  |  | SI | Mid-morning - Requires food / eating behaviour mon... |
| Q10 | varchar |  |  | SI | Mid-morning - Type of food offered |
| Q11 | varchar |  |  | SI | Mid-morning - Amount of food offered |
| Q12 | varchar |  |  | SI | Mid-morning - Amount eaten |
| Q13 | numeric |  |  | SI | Mid-morning - Oral intake (ml) |
| Q14 | varchar |  |  | SI | Mid-morning notes |
| Q15 | varchar |  |  | SI | Lunch - Requires food / eating behaviour monitorin... |
| Q16 | varchar |  |  | SI | Lunch - Type of food offered |
| Q17 | varchar |  |  | SI | Lunch - Amount of food offered |
| Q18 | varchar |  |  | SI | Lunch - Amount eaten |
| Q19 | numeric |  |  | SI | Lunch - Oral intake (ml) |
| Q20 | varchar |  |  | SI | Lunch notes |
| Q21 | varchar |  |  | SI | Mid-afternoon - Requires food / eating behaviour m... |
| Q22 | varchar |  |  | SI | Mid-afternoon - Type of food offered |
| Q23 | varchar |  |  | SI | Mid-afternoon - Amount of food offered |
| Q24 | varchar |  |  | SI | Mid-afternoon - Amount eaten |
| Q25 | numeric |  |  | SI | Mid-afternoon - Oral intake (ml) |
| Q26 | varchar |  |  | SI | Mid-afternoon notes |
| Q27 | varchar |  |  | SI | Evening meal - Requires food / eating behaviour mo... |
| Q28 | varchar |  |  | SI | Evening meal - Type of food offered |
| Q29 | varchar |  |  | SI | Evening meal - Amount of food offered |
| Q30 | varchar |  |  | SI | Evening meal - Amount eaten |
| Q31 | numeric |  |  | SI | Evening meal - Oral intake (ml) |
| Q32 | varchar |  |  | SI | Evening meal notes |
| Q33 | varchar |  |  | SI | Supper - Requires food / eating behaviour monitori... |
| Q34 | varchar |  |  | SI | Supper - Type of food offered |
| Q35 | varchar |  |  | SI | Supper - Amount of food offered |
| Q36 | varchar |  |  | SI | Supper - Amount eaten |
| Q37 | numeric |  |  | SI | Supper - Oral intake (ml) |
| Q38 | varchar |  |  | SI | Supper notes |
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