# questionnaire.QTCPFCVCB

> Periodic flushing of the Central Venous Catheter (CVC) bundle

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Periodic flushing of the Central Venous Catheter (CVC) bundle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bundle Compliance Percentage |
| Q04 | varchar |  |  | SI | % |
| Q05 | varchar |  |  | SI | Has the patient been identified? |
| Q06 | varchar |  |  | SI | Has the correct indication for system flushing bee... |
| Q07 | varchar |  |  | SI | Has it been verified that the patient is informed ... |
| Q08 | varchar |  |  | SI | Has all the necessary material for the procedure b... |
| Q09 | varchar |  |  | SI | Was hand hygiene performed according to protocol? |
| Q10 | varchar |  |  | SI | Has the infusion line been clamped and the needlef... |
| Q11 | varchar |  |  | SI | Has the connection cone been disinfected? |
| Q12 | varchar |  |  | SI | Has a new needlefree connector been applied and th... |
| Q13 | varchar |  |  | SI | Was the pulsatile flush performed with 10ml of phy... |
| Q14 | varchar |  |  | SI | Has the port protector been applied? |
| Q15 | varchar |  |  | SI | Notes |
| Q16 | varchar |  |  | SI | Score |
| Q17 | varchar |  |  | SI | Classification |
| Q18 | varchar |  |  | SI | 0 - 100 |
| Q19 | varchar |  |  | SI | Higher percentages represent higher compliance to ... |
| Q20 | varchar |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q21 | varchar |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q22 | varchar |  |  | SI | The aim of th Periodic flushing of the Central Ven... |
| Q23 | varchar |  |  | SI | Were clean non-sterile gloves used? |
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