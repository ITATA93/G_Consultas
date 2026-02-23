# SQLUser.LBC_CodedResult

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCR_RowID | bigint | PK |  | NO | - |
| LBCCR_ClinicalReviewFlag | varchar |  |  | SI | Flag for clinical review |
| LBCCR_Code | varchar |  |  | NO | Code
Note that the UI restricts this to be non-nu... |
| LBCCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCR_CodeTranslated | varchar |  |  | SI | - |
| LBCCR_CreatedDate | date |  |  | SI | Created Date |
| LBCCR_CreatedTime | time |  |  | SI | Created Time |
| LBCCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCR_DateFrom | date |  |  | NO | Effective date for the record |
| LBCCR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCR_Desc | varchar |  |  | SI | Description
Note that the UI restricts this to be... |
| LBCCR_DescTranslated | varchar |  |  | SI | - |
| LBCCR_NotPerformed | varchar |  |  | SI | Not Performed Flag. |
| LBCCR_Owner | varchar |  |  | SI | Owner |
| LBCCR_RangeFlag | varchar |  |  | SI | Flag to indicate if range is normal, abnormal or b... |
| LBCCR_SuppressBilling | varchar |  |  | SI | Suppress Billing Flag. |
| LBCCR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Facial expression |
| Q02 | - |  |  | SI | Body movements |
| Q03 | - |  |  | SI | Compliance with the ventilator (intubated patient)... |
| Q04 | - |  |  | SI | Muscle tension |
| Q05 | - |  |  | SI | Date |
| Q06 | - |  |  | SI | Time |
| Q07 | - |  |  | SI | Pain |
| Q08 | - |  |  | SI | Localisation |
| Q09 | - |  |  | SI | Body map |
| Q10 | - |  |  | SI | of 8 |
| Q11 | - |  |  | SI | 0: No muscle tension observed |
| Q12 | - |  |  | SI | 1: Presence of frowning, brow lowering, orbital ti... |
| Q13 | - |  |  | SI | 2: All previous facial movements, plus eyelids tig... |
| Q14 | - |  |  | SI | 0: Does not move at all (doesn’t necessarily mean ... |
| Q15 | - |  |  | SI | 1: Slow, cautious movements, touching or rubbing t... |
| Q16 | - |  |  | SI | 2: Pulling tube, attempting to sit up, moving limb... |
| Q17 | - |  |  | SI | 0: Alarms not activated, easy ventilation |
| Q18 | - |  |  | SI | 1: Coughing, alarms may be activated but stop spon... |
| Q19 | - |  |  | SI | 2: Asynchrony: blocking ventilation, alarms freque... |
| Q20 | - |  |  | SI | 0: Talking in normal tone or no sound |
| Q21 | - |  |  | SI | 1: Sighing, moaning |
| Q22 | - |  |  | SI | 2: Crying out, sobbing |
| Q23 | - |  |  | SI | 0: No resistance to passive movements |
| Q24 | - |  |  | SI | 1: Resistance to passive movements |
| Q25 | - |  |  | SI | 2: Strong resistance to passive movements or incap... |
| Q26 | - |  |  | SI | Directives of use of the CPOT |
| Q27 | - |  |  | SI | 1. The patient must be observed at rest for one mi... |
| Q28 | - |  |  | SI | 2. Then, the patient should be observed during noc... |
| Q29 | - |  |  | SI | 3. The patient should be evaluated before and at t... |
| Q30 | - |  |  | SI | 4. For the rating of the CPOT, the patient should ... |
| Q31 | - |  |  | SI | 5. The patient should be attributed a score for ea... |
| Q32 | - |  |  | SI | performing passive flexion and extension of the ar... |
| Q33 | - |  |  | SI | CPOT score of ≤ 2: |
| Q34 | - |  |  | SI | There is likely minimal to no pain present. Consid... |
| Q35 | - |  |  | SI | CPOT score of >2: |
| Q36 | - |  |  | SI | There is an unacceptable level of pain. Consider f... |
| Q37 | - |  |  | SI | The Critical Care Pain Observation Tool (CPOT) inc... |
| Q38 | - |  |  | SI | Facial expression |
| Q39 | - |  |  | SI | Body movements |
| Q40 | - |  |  | SI | Compliance with the ventilator (intubated patient) |
| Q41 | - |  |  | SI | Or vocalization (extubated patients) |
| Q42 | - |  |  | SI | Muscle tension |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time |
| Q45 | - |  |  | SI | Score |
| Q46 | - |  |  | SI | Classification |
| Q47 | - |  |  | SI | > 2 |
| Q48 | - |  |  | SI | There is an unacceptable level of pain. Consider f... |
| Q49 | - |  |  | SI | ≤ 2 |
| Q50 | - |  |  | SI | There is likely minimal to no pain present. Consid... |
| Q51 | - |  |  | SI | Is the patient intubated? |
| Q52 | - |  |  | SI | Compliance with the ventilator |
| Q53 | - |  |  | SI | Vocalisation |
| Q54 | - |  |  | SI | Legend |
| Q55 | - |  |  | SI | The 'Critical Care Pain Observation Tool' (CCPOT) ... |
| Q56 | - |  |  | SI | The threshold for determining the presence of pain... |
| Q57 | - |  |  | SI | References |
| Q58 | - |  |  | SI | 1. Gélinas C, Fillion L, Puntillo KA, Viens C, Fo... |
| Q59 | - |  |  | SI | 2. Gélinas C, Harel F, Fillion L, Puntillo KA, Joh... |
| Q60 | - |  |  | SI | J Pain Symptom Manag 2009 |
| Q61 | - |  |  | SI | 3.Gélinas C, Arbour C, Michaud C, Vaillant F, Desj... |
| Q62 | - |  |  | SI | with nonverbal critically ill adults: a before and... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*