# questionnaire.QTCDEATHINF

> Deceased patient information

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Deceased patient information

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Deceased Patient Information |
| Q10 | varchar |  |  | SI | Place of origin of the deceased body |
| Q11 | numeric |  |  | SI | Observation time (h) |
| Q12 | varchar |  |  | SI | Reason for a shorter observation period |
| Q13 | varchar |  |  | SI | Annotation |
| Q14 | varchar |  |  | SI | Clothes and medical devices removal |
| Q15 | varchar |  |  | SI | Pacemaker removed |
| Q16 | varchar |  |  | SI | Other medical devices removed |
| Q17 | date |  |  | SI | Clothes removal date / time |
| Q18 | time |  |  | SI | Clothes removal time |
| Q19 | varchar |  |  | SI | Removed clothes in charge to |
| Q2 | varchar |  |  | SI | Referral person to contact |
| Q20 | varchar |  |  | SI | Information provided and activities performed by t... |
| Q21 | varchar |  |  | SI | Funeral home name |
| Q22 | varchar |  |  | SI | Material of the coffin |
| Q23 | date |  |  | SI | Dressing date / time |
| Q24 | time |  |  | SI | Dressing time |
| Q25 | varchar |  |  | SI | Dressing in charge to |
| Q26 | date |  |  | SI | Assembly date / time |
| Q27 | time |  |  | SI | Assembly time |
| Q28 | varchar |  |  | SI | Assembly in charge to |
| Q29 | date |  |  | SI | Viewing date / time |
| Q3 | numeric |  |  | SI | Phone contact |
| Q30 | time |  |  | SI | Viewing time |
| Q31 | varchar |  |  | SI | Conservation treatments used |
| Q32 | varchar |  |  | SI | Judicial Authority |
| Q33 | varchar |  |  | SI | Available to judicial authority |
| Q34 | date |  |  | SI | Available to judicial authority on |
| Q35 | time |  |  | SI | Available to judicial authority at |
| Q36 | date |  |  | SI | Authorized on the day |
| Q37 | varchar |  |  | SI | Autopsy |
| Q38 | varchar |  |  | SI | Specify |
| Q39 | varchar |  |  | SI | Annotation |
| Q4 | varchar |  |  | SI | Death Information |
| Q40 | varchar |  |  | SI | Specify |
| Q41 | date |  |  | SI | Date / Time of device removal |
| Q42 | time |  |  | SI | Time of device removal |
| Q43 | varchar |  |  | SI | In charge to |
| Q44 | varchar |  |  | SI | Type of the removed device |
| Q45 | date |  |  | SI | Date / Time of device removal |
| Q46 | time |  |  | SI | Time of device removal |
| Q47 | varchar |  |  | SI | In charge to |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
| Q5 | varchar |  |  | SI | Place of death |
| Q50 | time |  |  | SI | Observation time (hh:mm) |
| Q6 | varchar |  |  | SI | Cause of death |
| Q7 | varchar |  |  | SI | Infection is out of death reason |
| Q8 | varchar |  |  | SI | Management of Deceased Body |
| Q9 | varchar |  |  | SI | Eligible to donate tissues |
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