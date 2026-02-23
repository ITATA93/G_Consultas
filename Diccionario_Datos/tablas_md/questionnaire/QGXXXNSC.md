# questionnaire.QGXXXNSC

> Nursing Safety Checks

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nursing Safety Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Safety checks |
| Q02 | varchar |  |  | SI | Invasive lines |
| Q03 | varchar |  |  | SI | Patient ID |
| Q04 | varchar |  |  | SI | Allergies reviewed |
| Q05 | varchar |  |  | SI | Clinical handover received from |
| Q06 | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI |  ETT length at lip |
| Q07ObsDR | varchar |  | FK | SI |  ETT length at lip DR |
| Q08 | varchar |  |  | SI | PA catheter length |
| Q08ObsDR | varchar |  | FK | SI | PA catheter length DR |
| Q09 | varchar |  |  | SI | Does the Patient have 2 ID bands? |
| Q10 | varchar |  |  | SI | Yankauer sucker changed |
| Q11 | varchar |  |  | SI | Heat and moisture exchange filter changed |
| Q12 | varchar |  |  | SI | In-Line circuit |
| Q13 | varchar |  |  | SI | Humidified circuit |
| Q14 | varchar |  |  | SI | Arterial line |
| Q15 | varchar |  |  | SI | Central line |
| Q16 | varchar |  |  | SI | ICP catheter |
| Q17 | varchar |  |  | SI | PA catheter |
| Q18 | date |  |  | SI | Due date |
| Q19 | date |  |  | SI | Due date |
| Q20 | date |  |  | SI | Due date |
| Q21 | date |  |  | SI | Due date |
| Q22 | varchar |  |  | SI | Pacemaker |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Time |
| Q25 | varchar |  |  | SI | Invasive devices reviewed and documented |
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