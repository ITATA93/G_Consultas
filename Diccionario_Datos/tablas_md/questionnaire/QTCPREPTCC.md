# questionnaire.QTCPREPTCC

> Pre-Procedure Travel Checklist - Cardiac

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre-Procedure Travel Checklist - Cardiac

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Cardiac procedure |
| Q04 | varchar |  |  | SI | Other procedure |
| Q05 | date |  |  | SI | Date accepted |
| Q06 | date |  |  | SI | Date of procedure |
| Q07 | varchar |  |  | SI | Current admission status |
| Q08 | varchar |  |  | SI | Community |
| Q09 | varchar |  |  | SI | Primary health care provider |
| Q10 | varchar |  |  | SI | Referral to receiving hospital sent |
| Q11 | varchar |  |  | SI | Referral to receiving hospital received |
| Q12 | varchar |  |  | SI | Receiving hospital |
| Q13 | varchar |  |  | SI | Receiving doctor |
| Q14 | varchar |  |  | SI | Receiving hospital notified |
| Q15 | varchar |  |  | SI | Primary health care provider notified |
| Q16 | varchar |  |  | SI | Primary health care provider notified of travel da... |
| Q17 | varchar |  |  | SI | Rheumatic heart disease register notified |
| Q18 | varchar |  |  | SI | Receiving hospital aboriginal liaison officer noti... |
| Q19 | varchar |  |  | SI | Patient aware |
| Q20 | varchar |  |  | SI | Renal patient |
| Q21 | varchar |  |  | SI | On dialysis |
| Q22 | varchar |  |  | SI | Current renal services notified |
| Q23 | varchar |  |  | SI | Receiving renal services notified |
| Q24 | varchar |  |  | SI | Notification notes |
| Q25 | varchar |  |  | SI | Screening tool sent to primary health care provide... |
| Q26 | varchar |  |  | SI | Dental clearance complete |
| Q27 | varchar |  |  | SI | Screening completed / forwarded to receiving hospi... |
| Q28 | varchar |  |  | SI | Screening notes |
| Q29 | date |  |  | SI | Date of travel |
| Q30 | varchar |  |  | SI | Escort name |
| Q31 | date |  |  | SI | Escort date of birth |
| Q32 | varchar |  |  | SI | Travel booking complete |
| Q33 | varchar |  |  | SI | Travel notes |
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