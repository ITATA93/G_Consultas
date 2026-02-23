# SQLUser.OE_FilmExecuteItems

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_FilmExecute Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_OEFilmRejected_DR | varchar |  | FK | SI | Des Ref OEFilmRejected |
| ITM_OEFilmUse_DR | varchar |  | FK | SI | Des Ref OEFilmUse |
| ITM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| ITM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date of Home Assessment |
| Q02 | - |  |  | SI | Time of Home Assessment |
| Q03 | - |  |  | SI | Reason for Home Assessment |
| Q04 | - |  |  | SI | People Present on The Home Assessment |
| Q05 | - |  |  | SI | Type of Dwelling |
| Q06 | - |  |  | SI | For the following section please note whether the ... |
| Q07 | - |  |  | SI | Functional Mobility |
| Q08 | - |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q09 | - |  |  | SI | RECOMMENDATIONS |
| Q10 | - |  |  | SI | Moving Inside / Outside The Home |
| Q11 | - |  |  | SI | Moving Inside / Outside The Home (Context) |
| Q12 | - |  |  | SI | Moving Inside / Outside The Home (Recommendations) |
| Q13 | - |  |  | SI | Accessing The Home |
| Q14 | - |  |  | SI | Access 1 |
| Q15 | - |  |  | SI | Access 1 (Context) |
| Q16 | - |  |  | SI | Access 1 (Recommendations) |
| Q17 | - |  |  | SI | Access 2 |
| Q18 | - |  |  | SI | Access 2 (Context) |
| Q19 | - |  |  | SI | Access 2 (Recommendations) |
| Q20 | - |  |  | SI | Seating and Transfers |
| Q21 | - |  |  | SI | Seating and Transfers (Context) |
| Q22 | - |  |  | SI | Seating and Transfers (Recommendations) |
| Q23 | - |  |  | SI | Bed Mobility and Transfers |
| Q24 | - |  |  | SI | Bed Mobility and Transfers (Context) |
| Q25 | - |  |  | SI | Bed Mobility and Transfers (Recommendations) |
| Q26 | - |  |  | SI | Self Care Occupations |
| Q27 | - |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q28 | - |  |  | SI | RECOMMENDATIONS |
| Q29 | - |  |  | SI | Washing, Drying and Grooming |
| Q30 | - |  |  | SI | Washing, Drying and Grooming (Context) |
| Q31 | - |  |  | SI | Washing, Drying and Grooming (Recommendations) |
| Q32 | - |  |  | SI | Dressing and Undressing |
| Q33 | - |  |  | SI | Dressing and Undressing (Context) |
| Q34 | - |  |  | SI | Dressing and Undressing (Recommendations) |
| Q35 | - |  |  | SI | Toileting |
| Q36 | - |  |  | SI | Toileting (Context) |
| Q37 | - |  |  | SI | Toileting (Recommendations) |
| Q38 | - |  |  | SI | Domestic Occupations |
| Q39 | - |  |  | SI | OCCUPATIONAL PERFORMANCE CONTEXT |
| Q40 | - |  |  | SI | RECOMMENDATIONS |
| Q41 | - |  |  | SI | Cleaning and Laundry |
| Q42 | - |  |  | SI | Cleaning and Laundry (Context) |
| Q43 | - |  |  | SI | Cleaning and Laundry (Recommendations) |
| Q44 | - |  |  | SI | Preparing Meals and Eating |
| Q45 | - |  |  | SI | Preparing Meals and Eating (Context) |
| Q46 | - |  |  | SI | Preparing Meals and Eating (Recommendations) |
| Q47 | - |  |  | SI | Maintaining the Home |
| Q48 | - |  |  | SI | Maintaining the Home (Context) |
| Q49 | - |  |  | SI | Maintaining the Home (Recommendations) |
| Q50 | - |  |  | SI | Other |
| Q51 | - |  |  | SI | e.g. pet care, communication, leisure, study, |
| Q52 | - |  |  | SI | vocational occupations, pet care etc. |
| Q53 | - |  |  | SI | Occupational Therapist Name |
| Q54 | - |  |  | SI | Date |
| Q55 | - |  |  | SI | Signature |
| Q55UDt | - |  |  | SI | Signature Last Updated Date |
| Q55UTm | - |  |  | SI | Signature Last Updated Time |
| Q56 | - |  |  | SI | Access 1 |
| Q57 | - |  |  | SI | Access 2 |
| Q58 | - |  |  | SI | e.g. pet care, communication, leisure, study, voca... |
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