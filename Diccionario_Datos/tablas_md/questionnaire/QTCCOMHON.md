# questionnaire.QTCCOMHON

> COMHON Index V2.1 (2021)

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* COMHON Index V2.1 (2021)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Level of conciousness |
| Q04 | varchar |  |  | SI | Mobility |
| Q05 | varchar |  |  | SI | Haemodynamic |
| Q06 | varchar |  |  | SI | Oxygenation |
| Q07 | varchar |  |  | SI | Nutrition |
| Q08 | varchar |  |  | SI | Level of consciousness |
| Q09 | varchar |  |  | SI | 1. Awake and alert: RASS 0 to + 1. The patient is ... |
| Q10 | varchar |  |  | SI | 2. Agitated / restless / confused: RASS > 1. The p... |
| Q11 | varchar |  |  | SI | 3. Sedated but responsive: RASS -1 to -3. The pati... |
| Q12 | varchar |  |  | SI | 4. Coma, sedated and unresponsive: RASS -4 to -5. ... |
| Q13 | varchar |  |  | SI | Mobility |
| Q14 | varchar |  |  | SI | 1. Independent / walking with help. The patient wa... |
| Q15 | varchar |  |  | SI | 2. Limited / bed-armchair activity. The patient is... |
| Q16 | varchar |  |  | SI | 3. Very limited but tolerates change in position. ... |
| Q17 | varchar |  |  | SI | 4. Unable to change position or lying prone. The p... |
| Q18 | varchar |  |  | SI | Haemodynamic |
| Q19 | varchar |  |  | SI | 1. No haemodynamic support. The patient does not r... |
| Q20 | varchar |  |  | SI | 2. Volume expanders. The patient requires use of b... |
| Q21 | varchar |  |  | SI | 3. Dopamine or norepinephrine or adrenaline or car... |
| Q22 | varchar |  |  | SI | 4. Needing two of the above. The patient requires ... |
| Q23 | varchar |  |  | SI | Oxygenation |
| Q24 | varchar |  |  | SI | 1. Spontaneous breathing and low FiO2 (< 0.4). The... |
| Q25 | varchar |  |  | SI | 2. Spontaneous breathing and high FiO2 (>= 0.4). T... |
| Q26 | varchar |  |  | SI | 3. Non-invasive mechanical ventilation. The patien... |
| Q27 | varchar |  |  | SI | 4. Invasive mechanical ventilation. The patient re... |
| Q28 | varchar |  |  | SI | Nutrition |
| Q29 | varchar |  |  | SI | 1. Full oral diet. The patient tolerates liquids a... |
| Q30 | varchar |  |  | SI | 2. Enteral nutrition / parenteral feeding. The pat... |
| Q31 | varchar |  |  | SI | 3. Oral fluids. Incomplete oral feeding. The patie... |
| Q32 | varchar |  |  | SI | 4. No feeding. The patient is not being fed at all... |
| Q33 | varchar |  |  | SI | The COMHON index assesses a patient's risk of deve... |
| Q34 | varchar |  |  | SI | RASS = Richmond Agitation Sedation Scale |
| Q35 | varchar |  |  | SI | World Federation of Critical Care Nurses. COHMON I... |
| Q36 | varchar |  |  | SI | https://wfccn.org/wp-content/uploads/2022/03/COMHO... |
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