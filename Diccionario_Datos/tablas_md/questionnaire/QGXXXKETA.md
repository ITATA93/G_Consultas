# questionnaire.QGXXXKETA

> Ketamine Assessment

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ketamine Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Comment |
| Q02 | varchar |  |  | SI | Pump Check |
| Q03 | varchar |  |  | SI | RN 1 (Pump Check) |
| Q04 | varchar |  |  | SI | RN 2 (Pump Check) |
| Q05 | varchar |  |  | SI | Rate of Infusion |
| Q06 | varchar |  |  | SI | Amount in Syringe |
| Q07 | varchar |  |  | SI | Syringe Change |
| Q08 | varchar |  |  | SI | Syringe Change |
| Q09 | varchar |  |  | SI | RN 1 (Syringe Change) |
| Q10 | varchar |  |  | SI | RN 2 (Syringe Change) |
| Q11 | varchar |  |  | SI | Programme Change |
| Q12 | varchar |  |  | SI | RN 1 (Programme Change) |
| Q13 | varchar |  |  | SI | RN 2 (Programme Change) |
| Q14 | varchar |  |  | SI | Rate Change |
| Q15 | varchar |  |  | SI | Rate Increase / Decrease |
| Q16 | varchar |  |  | SI | RN 1 (Rate Change) |
| Q17 | varchar |  |  | SI | RN 2 (Rate Change) |
| Q18 | bit |  |  | SI | Entered Discarded Amount in S8 Book |
| Q19 | varchar |  |  | SI | KETAMINE DOSE INFORMATION |
| Q20 | varchar |  |  | SI | KETAMINE INFUSION CHECKS |
| Q21 | varchar |  |  | SI | Comment Display |
| Q22 | varchar |  |  | SI | mgs |
| Q23 | varchar |  |  | SI | mls |
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