# questionnaire.QTCCVCCB

> Periodic Care And Flushing Of The Central Venous Catheter (CVC) Bundle Score

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Periodic Care And Flushing Of The Central Venous Catheter (CVC) Bundle Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bundle compliance percentage |
| Q04 | varchar |  |  | SI | Has the patient been identified? |
| Q05 | varchar |  |  | SI | Has the correct indication of central venous acces... |
| Q06 | varchar |  |  | SI | Has the patient been informed about the indication... |
| Q07 | varchar |  |  | SI | Was hand hygiene performed according to protocol? |
| Q08 | varchar |  |  | SI | Have clean, non-sterile gloves been used? |
| Q09 | varchar |  |  | SI | Has the insertion site been examined for tendernes... |
| Q10 | varchar |  |  | SI | Has the old central venous catheter line dressing ... |
| Q11 | varchar |  |  | SI | Has the insertion site been visually inspected? |
| Q12 | varchar |  |  | SI | Has the sutureless securement device been removed ... |
| Q13 | varchar |  |  | SI | Has skin antisepsis been performed with 2% chlorhe... |
| Q14 | varchar |  |  | SI | Has the material needed for the new dressing been ... |
| Q15 | varchar |  |  | SI | Have sterile gloves been used, after hand hygiene ... |
| Q16 | varchar |  |  | SI | Has the new dressing: chlorexidine antiseptic pad ... |
| Q17 | varchar |  |  | SI | Has the sterile field being maintained for the dur... |
| Q18 | varchar |  |  | SI | Notes |
| Q19 | varchar |  |  | SI | 0 - 100 |
| Q20 | varchar |  |  | SI | Higher percentages represent higher compliance to ... |
| Q21 | varchar |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q22 | varchar |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q23 | varchar |  |  | SI | The aim of the Central venous catheter (CVC) care ... |
| Q24 | varchar |  |  | SI | Score |
| Q25 | varchar |  |  | SI | Classification |
| Q26 | varchar |  |  | SI | % |
| Q27 | varchar |  |  | SI | Has all the necessary material for the procedure b... |
| Q28 | varchar |  |  | SI | Has the correct indication of central venous acces... |
| Q29 | varchar |  |  | SI | Care Procedure |
| Q30 | varchar |  |  | SI | Flushing Procedure |
| Q31 | varchar |  |  | SI | Were clean non-sterile gloves used? |
| Q32 | varchar |  |  | SI | Has the infusion line been clamped and the needle-... |
| Q33 | varchar |  |  | SI | Has the connection cone been disinfected? |
| Q34 | varchar |  |  | SI | Has a new needle-free connector been applied and t... |
| Q35 | varchar |  |  | SI | Was the pulsatile flush performed with 10ml of sal... |
| Q36 | varchar |  |  | SI | Has the port protector been applied? |
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