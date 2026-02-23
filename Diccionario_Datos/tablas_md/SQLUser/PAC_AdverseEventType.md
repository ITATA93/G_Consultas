# SQLUser.PAC_AdverseEventType

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADVEVT_RowId | bigint | PK |  | NO | - |
| ADVEVT_Code | varchar |  |  | NO | Code |
| ADVEVT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADVEVT_CodeTranslated | varchar |  |  | SI | - |
| ADVEVT_CreatedDate | date |  |  | SI | Created Date |
| ADVEVT_CreatedTime | time |  |  | SI | Created Time |
| ADVEVT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADVEVT_DateFrom | date |  |  | SI | Date From |
| ADVEVT_DateTo | date |  |  | SI | Date To |
| ADVEVT_Desc | varchar |  |  | NO | Description |
| ADVEVT_DescTranslated | varchar |  |  | SI | - |
| ADVEVT_DisplayOEWarning | varchar |  |  | SI | Display order entry warning |
| ADVEVT_Owner | varchar |  |  | SI | Owner |
| ADVEVT_UpdatedDate | date |  |  | SI | Updated Date |
| ADVEVT_UpdatedTime | time |  |  | SI | Updated Time |
| ADVEVT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Assessment of |
| Q04 | - |  |  | SI | Carer(s) name, if applicable |
| Q05 | - |  |  | SI | Dialysis access |
| Q06 | - |  |  | SI | Assessment notes |
| Q07 | - |  |  | SI | Able to complete math calculations |
| Q08 | - |  |  | SI | Able to read alarms on the dialysis machine |
| Q09 | - |  |  | SI | Able to read reverse osmosis unit screens |
| Q10 | - |  |  | SI | Literacy / Numeracy notes |
| Q11 | - |  |  | SI | Able to read weigh scales |
| Q12 | - |  |  | SI | Able to read dialysate concentrate label |
| Q13 | - |  |  | SI | Able to read expiry date on dialysis consumables |
| Q14 | - |  |  | SI | Able to read the blood pressure monitor |
| Q15 | - |  |  | SI | Vision test required |
| Q16 | - |  |  | SI | Vision notes |
| Q17 | - |  |  | SI | Able to open dialysate concentrate |
| Q18 | - |  |  | SI | Able to open / close large clamps on dialysis line... |
| Q19 | - |  |  | SI | Able to open / close small clamps on dialysis line... |
| Q20 | - |  |  | SI | Able to use roller ball on saline line |
| Q21 | - |  |  | SI | Able to open saline / heparin vials |
| Q22 | - |  |  | SI | Dexterity notes |
| Q23 | - |  |  | SI | Able to clean equipment |
| Q24 | - |  |  | SI | Able to manage stores and stock |
| Q25 | - |  |  | SI | Able to reach areas of machine and equipment whils... |
| Q26 | - |  |  | SI | Mobility notes |
| Q27 | - |  |  | SI | Anticipated location to complete dialysis |
| Q28 | - |  |  | SI | Home / Residence |
| Q29 | - |  |  | SI | Dummy1 |
| Q30 | - |  |  | SI | Dummy2 |
| Q31 | - |  |  | SI | Home suitability assessment completed |
| Q32 | - |  |  | SI | Location notes |
| Q33 | - |  |  | SI | Outcome of patient assessment for home haemodialys... |
| Q34 | - |  |  | SI | Suitability for home haemodialysis |
| Q35 | - |  |  | SI | Outcome |
| Q36 | - |  |  | SI | Plan |
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