# questionnaire.QTCBRADENQ

> Braden (Neonatal/Infant) Q Scale

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Braden (Neonatal/Infant) Q Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | INTENSITY AND DURATION OF PRESSURE |
| Q02 | varchar |  |  | SI | General Physical Condition |
| Q03 | varchar |  |  | SI | MOBILITY - The Ability to Change and Control Body ... |
| Q04 | varchar |  |  | SI | ACTIVITY - The degree of physical activity |
| Q05 | varchar |  |  | SI | SENSORY PERCEPTION - Ability to respond in a devel... |
| Q06 | varchar |  |  | SI | TOLERANCE OF THE SKIN AND SUPPORTING STRUCTURE |
| Q07 | varchar |  |  | SI | MOISTURE - Degree to which skin is exposed to mois... |
| Q08 | varchar |  |  | SI | FRICTION AND SHEAR - Friction: occurs when skin mo... |
| Q09 | varchar |  |  | SI | NUTRITION - Usual food intake pattern |
| Q10 | varchar |  |  | SI | Tissue perfusion and oxygenation |
| Q11 | varchar |  |  | SI | Remarks |
| Q12 | varchar |  |  | SI | < 20 |
| Q13 | varchar |  |  | SI | At Risk |
| Q14 | varchar |  |  | SI | ≥ 20 |
| Q15 | varchar |  |  | SI | Low Risk |
| Q16 | varchar |  |  | SI | The Braden scale assesses a patient's risk of deve... |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | ≥ 20 : Low Risk |
| Q20 | varchar |  |  | SI | < 20 : At Risk |
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