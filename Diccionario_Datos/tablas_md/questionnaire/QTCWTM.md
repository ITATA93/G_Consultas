# questionnaire.QTCWTM

> Warfarin Therapy Management

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Warfarin Therapy Management

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | International Normalised Ratio (INR) Guidelines fo... |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Indication and recommended INR range |
| Q05 | varchar |  |  | SI | Other indication, including INR range |
| Q06 | varchar |  |  | SI | INR range (If different to recommendation) |
| Q07 | varchar |  |  | SI | Rationale for different INR range |
| Q08 | varchar |  |  | SI | For All Patients Initiated on Warfarin |
| Q09 | varchar |  |  | SI | Warfarin education provided |
| Q10 | varchar |  |  | SI | Anticoagulation education record completed |
| Q11 | varchar |  |  | SI | Reason for no education |
| Q12 | numeric |  |  | SI | Usual dose, if taken previously (mg) |
| Q13 | varchar |  |  | SI | General practitioner details confirmed and updated |
| Q14 | varchar |  |  | SI | Requires bridging anticoagulation e.g. enoxaparin ... |
| Q15 | varchar |  |  | SI | Ensure patient has an inpatient order for bridging... |
| Q16 | varchar |  |  | SI | Ensure patient has: |
| Q17 | varchar |  |  | SI | 1. A discharge or outpatient prescription for brid... |
| Q18 | varchar |  |  | SI | 2. Equipment (e.g. sharps kit) required for self-a... |
| Q19 | varchar |  |  | SI | For Outpatients |
| Q20 | varchar |  |  | SI | Patient location |
| Q21 | varchar |  |  | SI | Other patient location |
| Q22 | varchar |  |  | SI | Warfarin administration |
| Q23 | varchar |  |  | SI | Ensure patient has an inpatient order for warfarin... |
| Q24 | varchar |  |  | SI | Ensure patient has a discharge or outpatient presc... |
| Q25 | varchar |  |  | SI | Guidelines |
| Q26 | varchar |  |  | SI | Use in conjunction with local warfarin management ... |
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