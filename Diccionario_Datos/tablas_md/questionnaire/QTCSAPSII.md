# questionnaire.QTCSAPSII

> SAPS II

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(SAPS II)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of Admission |
| Q02 | varchar |  |  | SI | Chronic Disease |
| Q03 | varchar |  |  | SI | Glasgow Coma Scale |
| Q04 | varchar |  |  | SI | Age, years |
| Q05 | varchar |  |  | SI | Systolic Blood Pressure, mmHg |
| Q06 | varchar |  |  | SI | White Blood Cells, 10E9/L |
| Q07 | varchar |  |  | SI | Heart Rate, bpm |
| Q08 | varchar |  |  | SI | Temperature, °C |
| Q09a | varchar |  |  | SI | Mechanical Ventilation or CPAP |
| Q09b | varchar |  |  | SI | PaO2/FiO2, mmHg (kPa) |
| Q10 | varchar |  |  | SI | Urine Output, L/d |
| Q11 | varchar |  |  | SI | Potassium, mmol/L |
| Q12 | varchar |  |  | SI | Sodium, mmol/L |
| Q13 | varchar |  |  | SI | Bicarbonate, mEq/L |
| Q14 | varchar |  |  | SI | Bilirubin, micromol/L (mg/dL) |
| Q15 | varchar |  |  | SI | Serum urea concentration, mmol/L (mg/dL) |
| Q17 | varchar |  |  | SI | Use the worst value for each physiological variabl... |
| Q18 | varchar |  |  | SI | SAPS II is a severity of disease classification sy... |
| Q19 | varchar |  |  | SI | 163 - High severity / 0 - Low severity |
| Q20 | varchar |  |  | SI | A higher number is associated with a greater sever... |
| Q21 | varchar |  |  | SI | Primary Source |
| Q22 | varchar |  |  | SI | Le Gall J, Lemeshow S, Saulnier F. A New Simplifie... |
| Q23 | varchar |  |  | SI | Validation |
| Q24 | varchar |  |  | SI | Beck DH, Smith GB, Pappachan JV, Millar B. Externa... |
| Q25 | varchar |  |  | SI | Capuzzo M, Valpondi V, Sgarbi A, Bortolazzi S, Pav... |
| Q26 | date |  |  | SI | Date |
| Q27 | time |  |  | SI | Time |
| Q28 | varchar |  |  | SI | SAPS 2 Score |
| Q29 | varchar |  |  | SI | Estimated hospital mortality |
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