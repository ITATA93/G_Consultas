# questionnaire.QTCOTRRD

> Recovery Room Discharge

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Recovery Room Discharge

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure |
| Q02 | varchar |  |  | SI | Conscious & orientated |
| Q03 | varchar |  |  | SI | Comments |
| Q04 | varchar |  |  | SI | Maintaining the airway & having protective reflexe... |
| Q05 | varchar |  |  | SI | Comments |
| Q06 | varchar |  |  | SI | Stable cardiovascular function |
| Q07 | varchar |  |  | SI | Comments |
| Q08 | varchar |  |  | SI | Stable respiratory function |
| Q09 | varchar |  |  | SI | Comments |
| Q10 | varchar |  |  | SI | Body Temp >35.9°C |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | NEWS Score |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | Surgical site satisfactory |
| Q15 | varchar |  |  | SI | Comments |
| Q16 | varchar |  |  | SI | Is patient nauseous &/or vomiting |
| Q17 | varchar |  |  | SI | Comments |
| Q18 | varchar |  |  | SI | Is pain score 0 or 1 |
| Q19 | varchar |  |  | SI | Comments |
| Q20 | varchar |  |  | SI | Oxygenation |
| Q21 | varchar |  |  | SI | Comments |
| Q22 | varchar |  |  | SI | IV access / fluid replacement |
| Q23 | varchar |  |  | SI | Comments |
| Q24 | varchar |  |  | SI | Drugs given in recovery |
| Q25 | varchar |  |  | SI | Comments |
| Q26 | varchar |  |  | SI | PCA/IV site checked |
| Q27 | varchar |  |  | SI | Comments |
| Q28 | varchar |  |  | SI | Epidural site checked |
| Q29 | varchar |  |  | SI | Comments |
| Q30 | varchar |  |  | SI | Surgical site / wound checked |
| Q31 | varchar |  |  | SI | Comments |
| Q32 | varchar |  |  | SI | Dressing & drains |
| Q33 | varchar |  |  | SI | Comments |
| Q34 | varchar |  |  | SI | Skin condition assessed |
| Q35 | varchar |  |  | SI | Comments |
| Q36 | varchar |  |  | SI | Pressure areas intact |
| Q37 | varchar |  |  | SI | Comments |
| Q38 | varchar |  |  | SI | Patient passed urine |
| Q39 | varchar |  |  | SI | Comments |
| Q40 | varchar |  |  | SI | Fluid balanced chart commenced? |
| Q41 | varchar |  |  | SI | Comments |
| Q42 | varchar |  |  | SI | Pressure areas checked on handover to ward |
| Q43 | varchar |  |  | SI | Comments |
| Q44 | varchar |  |  | SI | Patient property checked |
| Q45 | varchar |  |  | SI | Comments |
| Q46 | varchar |  |  | SI | X-rays / Scans |
| Q47 | varchar |  |  | SI | Comments |
| Q48 | varchar |  |  | SI | Recovery staff name |
| Q49 | varchar |  |  | SI | Ward staff |
| Q50 | varchar |  |  | SI | Temperature ( ℃) |
| Q50ObsDR | varchar |  | FK | SI | Temperature ( ℃) DR |
| Q51 | varchar |  |  | SI | Blood glucose (mmol/l) |
| Q51ObsDR | varchar |  | FK | SI | Blood glucose (mmol/l) DR |
| Q52 | varchar |  |  | SI | Comments |
| Q53 | varchar |  |  | SI | Is the patient nauseous? |
| Q54 | varchar |  |  | SI | Is the patient vomiting? |
| Q55 | varchar |  |  | SI | Comments |
| Q56 | varchar |  |  | SI | Pain Score (0-10) |
| Q56ObsDR | varchar |  | FK | SI | Pain Score (0-10) DR |
| Q57 | varchar |  |  | SI | Is the patient diabetic? |
| Q58 | varchar |  |  | SI | Comments |
| Q59 | date |  |  | SI | Date |
| Q60 | time |  |  | SI | Time |
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