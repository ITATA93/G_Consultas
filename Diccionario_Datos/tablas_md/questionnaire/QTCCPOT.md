# questionnaire.QTCCPOT

> Critical Care Pain Observation Tool

**Schema:** questionnaire
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Critical Care Pain Observation Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Facial expression |
| Q02 | varchar |  |  | SI | Body movements |
| Q03 | varchar |  |  | SI | Compliance with the ventilator (intubated patient)... |
| Q04 | varchar |  |  | SI | Muscle tension |
| Q05 | date |  |  | SI | Date |
| Q06 | time |  |  | SI | Time |
| Q07 | varchar |  |  | SI | Pain |
| Q08 | varchar |  |  | SI | Localisation |
| Q09 | varchar |  |  | SI | Body map |
| Q10 | varchar |  |  | SI |  of 8  |
| Q11 | varchar |  |  | SI | 0: No muscle tension observed |
| Q12 | varchar |  |  | SI | 1: Presence of frowning, brow lowering, orbital ti... |
| Q13 | varchar |  |  | SI | 2: All previous facial movements, plus eyelids tig... |
| Q14 | varchar |  |  | SI | 0: Does not move at all (doesn’t necessarily mean ... |
| Q15 | varchar |  |  | SI | 1: Slow, cautious movements, touching or rubbing t... |
| Q16 | varchar |  |  | SI | 2: Pulling tube, attempting to sit up, moving limb... |
| Q17 | varchar |  |  | SI | 0: Alarms not activated, easy ventilation |
| Q18 | varchar |  |  | SI | 1: Coughing, alarms may be activated but stop spon... |
| Q19 | varchar |  |  | SI | 2: Asynchrony: blocking ventilation, alarms freque... |
| Q20 | varchar |  |  | SI | 0: Talking in normal tone or no sound  |
| Q21 | varchar |  |  | SI | 1: Sighing, moaning |
| Q22 | varchar |  |  | SI | 2: Crying out, sobbing |
| Q23 | varchar |  |  | SI | 0: No resistance to passive movements  |
| Q24 | varchar |  |  | SI | 1: Resistance to passive movements |
| Q25 | varchar |  |  | SI | 2: Strong resistance to passive movements or incap... |
| Q26 | varchar |  |  | SI | Directives of use of the CPOT |
| Q27 | varchar |  |  | SI | 1. The patient must be observed at rest for one mi... |
| Q28 | varchar |  |  | SI | 2. Then, the patient should be observed during noc... |
| Q29 | varchar |  |  | SI | 3. The patient should be evaluated before and at t... |
| Q30 | varchar |  |  | SI | 4. For the rating of the CPOT, the patient should ... |
| Q31 | varchar |  |  | SI | 5. The patient should be attributed a score for ea... |
| Q32 | varchar |  |  | SI | performing passive flexion and extension of the ar... |
| Q33 | varchar |  |  | SI | CPOT score of ≤ 2: |
| Q34 | varchar |  |  | SI | There is likely minimal to no pain present. Consid... |
| Q35 | varchar |  |  | SI | CPOT score of >2: |
| Q36 | varchar |  |  | SI | There is an unacceptable level of pain. Consider f... |
| Q37 | varchar |  |  | SI | The Critical Care Pain Observation Tool (CPOT) inc... |
| Q38 | varchar |  |  | SI | Facial expression |
| Q39 | varchar |  |  | SI | Body movements |
| Q40 | varchar |  |  | SI | Compliance with the ventilator (intubated patient) |
| Q41 | varchar |  |  | SI | Or vocalization (extubated patients) |
| Q42 | varchar |  |  | SI | Muscle tension |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time |
| Q45 | varchar |  |  | SI | Score |
| Q46 | varchar |  |  | SI | Classification |
| Q47 | varchar |  |  | SI | > 2 |
| Q48 | varchar |  |  | SI | There is an unacceptable level of pain. Consider f... |
| Q49 | varchar |  |  | SI | ≤ 2 |
| Q50 | varchar |  |  | SI | There is likely minimal to no pain present. Consid... |
| Q51 | varchar |  |  | SI | Is the patient intubated? |
| Q52 | varchar |  |  | SI | Compliance with the ventilator |
| Q53 | varchar |  |  | SI | Vocalisation |
| Q54 | varchar |  |  | SI | Legend |
| Q55 | varchar |  |  | SI | The 'Critical Care Pain Observation Tool' (CCPOT) ... |
| Q56 | varchar |  |  | SI | The threshold for determining the presence of pain... |
| Q57 | varchar |  |  | SI | References |
| Q58 | varchar |  |  | SI | 1. Gélinas C, Fillion L, Puntillo KA, Viens C, Fo... |
| Q59 | varchar |  |  | SI | 2. Gélinas C, Harel F, Fillion L, Puntillo KA, Joh... |
| Q60 | varchar |  |  | SI | J Pain Symptom Manag 2009;37:58–67. |
| Q61 | varchar |  |  | SI | 3.Gélinas C, Arbour C, Michaud C, Vaillant F, Desj... |
| Q62 | varchar |  |  | SI | with nonverbal critically ill adults: a before and... |
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