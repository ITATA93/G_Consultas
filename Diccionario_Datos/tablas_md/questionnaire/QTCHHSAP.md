# questionnaire.QTCHHSAP

> Home Haemodialysis Suitability Assessment - Patient

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home Haemodialysis Suitability Assessment - Patient

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Assessment of |
| Q04 | varchar |  |  | SI | Carer(s) name, if applicable |
| Q05 | varchar |  |  | SI | Dialysis access |
| Q06 | varchar |  |  | SI | Assessment notes |
| Q07 | varchar |  |  | SI | Able to complete math calculations |
| Q08 | varchar |  |  | SI | Able to read alarms on the dialysis machine |
| Q09 | varchar |  |  | SI | Able to read reverse osmosis unit screens |
| Q10 | varchar |  |  | SI | Literacy / Numeracy notes |
| Q11 | varchar |  |  | SI | Able to read weigh scales |
| Q12 | varchar |  |  | SI | Able to read dialysate concentrate label |
| Q13 | varchar |  |  | SI | Able to read expiry date on dialysis consumables |
| Q14 | varchar |  |  | SI | Able to read the blood pressure monitor |
| Q15 | varchar |  |  | SI | Vision test required |
| Q16 | varchar |  |  | SI | Vision notes |
| Q17 | varchar |  |  | SI | Able to open dialysate concentrate |
| Q18 | varchar |  |  | SI | Able to open / close large clamps on dialysis line... |
| Q19 | varchar |  |  | SI | Able to open / close small clamps on dialysis line... |
| Q20 | varchar |  |  | SI | Able to use roller ball on saline line |
| Q21 | varchar |  |  | SI | Able to open saline / heparin vials |
| Q22 | varchar |  |  | SI | Dexterity notes |
| Q23 | varchar |  |  | SI | Able to clean equipment |
| Q24 | varchar |  |  | SI | Able to manage stores and stock |
| Q25 | varchar |  |  | SI | Able to reach areas of machine and equipment whils... |
| Q26 | varchar |  |  | SI | Mobility notes |
| Q27 | varchar |  |  | SI | Anticipated location to complete dialysis |
| Q28 | varchar |  |  | SI | Home / Residence |
| Q29 | varchar |  |  | SI | Dummy1 |
| Q30 | varchar |  |  | SI | Dummy2 |
| Q31 | varchar |  |  | SI | Home suitability assessment completed |
| Q32 | varchar |  |  | SI | Location notes |
| Q33 | varchar |  |  | SI | Outcome of patient assessment for home haemodialys... |
| Q34 | varchar |  |  | SI | Suitability for home haemodialysis |
| Q35 | varchar |  |  | SI | Outcome |
| Q36 | varchar |  |  | SI | Plan |
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