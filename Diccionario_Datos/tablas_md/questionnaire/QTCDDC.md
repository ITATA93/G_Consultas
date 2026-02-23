# questionnaire.QTCDDC

> Day of Discharge Checklist

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Day of Discharge Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Intent to discharge documented in medical record |
| Q04 | varchar |  |  | SI | Relevant Multidisciplinary Teams (MTD) supports pa... |
| Q05 | varchar |  |  | SI | Contact appropriate specialty / clinician |
| Q06 | varchar |  |  | SI | MDT details |
| Q07 | varchar |  |  | SI | Next of kin / Relevant person / Guardianship / Cas... |
| Q08 | varchar |  |  | SI | Transport arranged |
| Q09 | varchar |  |  | SI | Discharge medications explained to patient / famil... |
| Q10 | varchar |  |  | SI | Discharge medications given to patient / family / ... |
| Q11 | varchar |  |  | SI | Patients own medications have been returned to the... |
| Q12 | varchar |  |  | SI | Outpatient prescription given to patient |
| Q13 | varchar |  |  | SI | All personal items returned to the patient |
| Q14 | varchar |  |  | SI | Personal items returned details |
| Q15 | varchar |  |  | SI | Equipment and supplies given to the patient |
| Q16 | varchar |  |  | SI | Reviewed all invasive devices and removed as requi... |
| Q17 | varchar |  |  | SI | Medical certificate provided / received |
| Q18 | varchar |  |  | SI | Medical discharge summary provided / received |
| Q19 | varchar |  |  | SI | Post discharge instructions provided to patient / ... |
| Q20 | varchar |  |  | SI | Patient / carer aware of follow up appointments an... |
| Q21 | varchar |  |  | SI | Patient able to wait in transit lounge |
| Q22 | varchar |  |  | SI | Waiting for |
| Q23 | varchar |  |  | SI | Adapted from the NSW Health Nepean Blue Mountains ... |
| Q24 | varchar |  |  | SI | Have Community Services / Providers / General Prac... |
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