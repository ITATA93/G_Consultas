# questionnaire.QTCAHOCCHA

> Occupational Therapy Home Assessment

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Occupational Therapy Home Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of Home Assessment |
| Q02 | time |  |  | SI | Time of Home Assessment |
| Q03 | varchar |  |  | SI | Reason for Home Assessment |
| Q04 | varchar |  |  | SI | People Present on The Home Assessment |
| Q05 | varchar |  |  | SI | Type of Dwelling |
| Q06 | varchar |  |  | SI | For the following section please note whether the ... |
| Q07 | varchar |  |  | SI | Functional Mobility |
| Q08 | varchar |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q09 | varchar |  |  | SI | RECOMMENDATIONS |
| Q10 | varchar |  |  | SI | Moving Inside / Outside The Home |
| Q11 | varchar |  |  | SI | Moving Inside / Outside The Home (Context) |
| Q12 | varchar |  |  | SI | Moving Inside / Outside The Home (Recommendations) |
| Q13 | varchar |  |  | SI | Accessing The Home |
| Q14 | varchar |  |  | SI | Access 1 |
| Q15 | varchar |  |  | SI | Access 1 (Context) |
| Q16 | varchar |  |  | SI | Access 1 (Recommendations) |
| Q17 | varchar |  |  | SI | Access 2 |
| Q18 | varchar |  |  | SI | Access 2 (Context) |
| Q19 | varchar |  |  | SI | Access 2 (Recommendations) |
| Q20 | varchar |  |  | SI | Seating and Transfers |
| Q21 | varchar |  |  | SI | Seating and Transfers (Context) |
| Q22 | varchar |  |  | SI | Seating and Transfers (Recommendations) |
| Q23 | varchar |  |  | SI | Bed Mobility and Transfers |
| Q24 | varchar |  |  | SI | Bed Mobility and Transfers (Context) |
| Q25 | varchar |  |  | SI | Bed Mobility and Transfers (Recommendations) |
| Q26 | varchar |  |  | SI | Self Care Occupations |
| Q27 | varchar |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q28 | varchar |  |  | SI | RECOMMENDATIONS |
| Q29 | varchar |  |  | SI | Washing, Drying and Grooming |
| Q30 | varchar |  |  | SI | Washing, Drying and Grooming (Context) |
| Q31 | varchar |  |  | SI | Washing, Drying and Grooming (Recommendations) |
| Q32 | varchar |  |  | SI | Dressing and Undressing |
| Q33 | varchar |  |  | SI | Dressing and Undressing (Context) |
| Q34 | varchar |  |  | SI | Dressing and Undressing (Recommendations) |
| Q35 | varchar |  |  | SI | Toileting |
| Q36 | varchar |  |  | SI | Toileting (Context) |
| Q37 | varchar |  |  | SI | Toileting (Recommendations) |
| Q38 | varchar |  |  | SI | Domestic Occupations |
| Q39 | varchar |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q40 | varchar |  |  | SI | RECOMMENDATIONS |
| Q41 | varchar |  |  | SI | Cleaning and Laundry |
| Q42 | varchar |  |  | SI | Cleaning and Laundry (Context) |
| Q43 | varchar |  |  | SI | Cleaning and Laundry (Recommendations) |
| Q44 | varchar |  |  | SI | Preparing Meals and Eating |
| Q45 | varchar |  |  | SI | Preparing Meals and Eating (Context) |
| Q46 | varchar |  |  | SI | Preparing Meals and Eating (Recommendations) |
| Q47 | varchar |  |  | SI | Maintaining the Home |
| Q48 | varchar |  |  | SI | Maintaining the Home (Context) |
| Q49 | varchar |  |  | SI | Maintaining the Home (Recommendations) |
| Q50 | varchar |  |  | SI | Other |
| Q51 | varchar |  |  | SI | e.g. pet care, communication, leisure, study, |
| Q52 | varchar |  |  | SI | vocational occupations, pet care etc. |
| Q53 | varchar |  |  | SI | Occupational Therapist Name |
| Q54 | date |  |  | SI | Date |
| Q55 | longvarbinary |  |  | SI | Signature |
| Q55UDt | date |  |  | SI | Signature Last Updated Date |
| Q55UTm | time |  |  | SI | Signature Last Updated Time |
| Q56 | varchar |  |  | SI | Access 1 |
| Q57 | varchar |  |  | SI | Access 2 |
| Q58 | varchar |  |  | SI | e.g. pet care, communication, leisure, study, voca... |
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