# questionnaire.QTCRESPNA

> Respiratory Nurse Assessment

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Nurse Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Attended since last visit	 |
| Q02 | varchar |  |  | SI | Outcome |
| Q03 | varchar |  |  | SI | Medication or device change |
| Q04 | date |  |  | SI | Date of Medication or Device change	 |
| Q05 | varchar |  |  | SI | Medication or Device change by	 |
| Q06 | varchar |  |  | SI | Other |
| Q07 | varchar |  |  | SI | Nebuliser |
| Q08 | varchar |  |  | SI | Other |
| Q09 | varchar |  |  | SI | Ever ventilated	 |
| Q10 | varchar |  |  | SI | Ventilated year	 |
| Q11 | varchar |  |  | SI | Ventilated information	 |
| Q12 | varchar |  |  | SI | Triggers |
| Q13 | varchar |  |  | SI |  Other	 |
| Q14 | varchar |  |  | SI | Nocturnal symptoms	 |
| Q15 | varchar |  |  | SI | Nocturnal symptom notes	 |
| Q16 | varchar |  |  | SI | Daytime symptoms	 |
| Q17 | varchar |  |  | SI | Daytime symptom notes	 |
| Q18 | varchar |  |  | SI | Affected daily activities	 |
| Q19 | varchar |  |  | SI | Affected daily activities notes	 |
| Q20 | varchar |  |  | SI | Emergency advice given	 |
| Q21 | varchar |  |  | SI | Previous Self Management Plan	 |
| Q22 | varchar |  |  | SI | Was the Self Management Plan reviewed today	 |
| Q23 | varchar |  |  | SI | Inhaler technique	 |
| Q24 | varchar |  |  | SI | Oxygen |
| Q25 | varchar |  |  | SI | Oxygen type	 |
| Q26 | varchar |  |  | SI | Walking |
| Q27 | varchar |  |  | SI | Climbing stairs	 |
| Q28 | varchar |  |  | SI | Social circumstances	 |
| Q29 | varchar |  |  | SI | Other social circumstances	 |
| Q30 | varchar |  |  | SI | Notes |
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