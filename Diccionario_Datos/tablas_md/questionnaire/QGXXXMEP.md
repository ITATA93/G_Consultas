# questionnaire.QGXXXMEP

> Ectopic Pregnancy

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ectopic Pregnancy

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Consultant who decided to give Methotrexate |
| Q02 | varchar |  |  | SI | Methotrexate given |
| Q02ObsDR | varchar |  | FK | SI | Methotrexate given DR |
| Q03 | varchar |  |  | SI | Methotrexate cycle - Follow - up |
| Q04 | numeric |  |  | SI | Days post Methotrexate |
| Q05 | varchar |  |  | SI | Pain since Methotrexate |
| Q05ObsDR | varchar |  | FK | SI | Pain since Methotrexate DR |
| Q06 | varchar |  |  | SI | Bleeding since Methotrexate |
| Q06ObsDR | varchar |  | FK | SI | Bleeding since Methotrexate DR |
| Q07 | varchar |  |  | SI | Second dose of Methotrexate required |
| Q07ObsDR | varchar |  | FK | SI | Second dose of Methotrexate required DR |
| Q08 | varchar |  |  | SI | Consultant who decided 2nd dose Methotrexate |
| Q09 | varchar |  |  | SI | HCG done |
| Q09ObsDR | varchar |  | FK | SI | HCG done DR |
| Q10 | varchar |  |  | SI | HCG level within protocol |
| Q10ObsDR | varchar |  | FK | SI | HCG level within protocol DR |
| Q11 | varchar |  |  | SI | US findings within protocol |
| Q11ObsDR | varchar |  | FK | SI | US findings within protocol DR |
| Q12 | varchar |  |  | SI | Medical history within protocol |
| Q12ObsDR | varchar |  | FK | SI | Medical history within protocol DR |
| Q13 | varchar |  |  | SI | Follow - up |
| Q13ObsDR | varchar |  | FK | SI | Follow - up DR |
| Q14 | varchar |  |  | SI | Surgery required |
| Q14ObsDR | varchar |  | FK | SI | Surgery required DR |
| Q15 | varchar |  |  | SI | Hospital consent form signed |
| Q15ObsDR | varchar |  | FK | SI | Hospital consent form signed DR |
| Q16 | varchar |  |  | SI | Patient information consent signed |
| Q16ObsDR | varchar |  | FK | SI | Patient information consent signed DR |
| Q17 | date |  |  | SI | Group and save date |
| Q18 | varchar |  |  | SI | Group and save done |
| Q18ObsDR | varchar |  | FK | SI | Group and save done DR |
| Q19 | varchar |  |  | SI | Anti D required |
| Q19ObsDR | varchar |  | FK | SI | Anti D required DR |
| Q20 | varchar |  |  | SI | Consultant who decided conservative management |
| Q21 | varchar |  |  | SI | Registrar reviewing patient |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | Consultant who decided surgery |
| Q24 | varchar |  |  | SI | Follow - up location |
| Q25 | varchar |  |  | SI | Methotrexate dose |
| Q25ObsDR | varchar |  | FK | SI | Methotrexate dose DR |
| Q26 | time |  |  | SI | Methotrexate administration time |
| Q27 | varchar |  |  | SI | Methotrexate cycle |
| Q28 | date |  |  | SI | Anti D given |
| Q29 | varchar |  |  | SI | Anti D dose |
| Q29ObsDR | varchar |  | FK | SI | Anti D dose DR |
| Q30 | varchar |  |  | SI | Anti D batch number |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
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