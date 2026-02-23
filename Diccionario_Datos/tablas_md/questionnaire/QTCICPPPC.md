# questionnaire.QTCICPPPC

> Invasive Cardiac Procedure - Post Procedure Checklist

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Invasive Cardiac Procedure - Post Procedure Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Variance |
| Q04 | varchar |  |  | SI | Observations stable and within acceptable limits |
| Q05 | varchar |  |  | SI | Variance |
| Q06 | varchar |  |  | SI | 12 lead electrocardiogram performed post procedure... |
| Q07 | varchar |  |  | SI | Variance |
| Q08 | varchar |  |  | SI | Cardiac rhythmn monitored and all arrhythmias repo... |
| Q09 | varchar |  |  | SI | Variance |
| Q10 | varchar |  |  | SI | Neurovascular observations within normal parameter... |
| Q11 | varchar |  |  | SI | Variance |
| Q12 | varchar |  |  | SI | Medications administered as prescribed |
| Q13 | varchar |  |  | SI | Variance |
| Q14 | varchar |  |  | SI | Insertion site checked and free of haematoma and o... |
| Q15 | varchar |  |  | SI | Variance |
| Q16 | varchar |  |  | SI | Intravascular fluid therapy administered as prescr... |
| Q17 | varchar |  |  | SI | Variance |
| Q18 | varchar |  |  | SI | Patient has voided post procedure |
| Q19 | varchar |  |  | SI | Variance |
| Q20 | varchar |  |  | SI | Patient tolerated oral diet as appropriate |
| Q21 | varchar |  |  | SI | Variance |
| Q22 | varchar |  |  | SI | Post-procedure positioning as per guidelines |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | Dummy1 |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | Explained sheath removal to patient (if sheath pre... |
| Q27 | varchar |  |  | SI | Variance |
| Q28 | varchar |  |  | SI | Completed cardiac education |
| Q29 | varchar |  |  | SI | Variance |
| Q30 | varchar |  |  | SI | Post-Procedure Positioning |
| Q31 | varchar |  |  | SI | Femoral approach: lay flat for first hour then rai... |
| Q32 | varchar |  |  | SI | Radial approach: patient can sit upon return |
| Q33 | varchar |  |  | SI | Variance |
| Q34 | varchar |  |  | SI | Variance |
| Q35 | varchar |  |  | SI | Variance |
| Q36 | varchar |  |  | SI | Variance |
| Q37 | varchar |  |  | SI | Variance |
| Q38 | varchar |  |  | SI | Variance |
| Q39 | varchar |  |  | SI | Variance |
| Q40 | varchar |  |  | SI | Variance |
| Q41 | varchar |  |  | SI | Variance |
| Q42 | varchar |  |  | SI | Variance |
| Q43 | varchar |  |  | SI | Variance |
| Q44 | varchar |  |  | SI | Variance |
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