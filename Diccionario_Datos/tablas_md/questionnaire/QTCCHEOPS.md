# questionnaire.QTCCHEOPS

> Children's Hospital of Eastern Ontario Pain Scale (CHEOPS)

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Children's Hospital of Eastern Ontario Pain Scale (CHEOPS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Cry |
| Q04 | varchar |  |  | SI | Facial |
| Q05 | varchar |  |  | SI | Child verbal  |
| Q06 | varchar |  |  | SI | Torso |
| Q07 | varchar |  |  | SI | Touch |
| Q08 | varchar |  |  | SI | Legs |
| Q10 | varchar |  |  | SI | Guidelines |
| Q11 | varchar |  |  | SI | Patients:  |
| Q12 | varchar |  |  | SI | • The initial study was done on children 1 to 5 ye... |
| Q13 | varchar |  |  | SI | • It has been used in studies with adolescents but... |
| Q14 | varchar |  |  | SI | • According to Mitchell (1999) it is intended for ... |
| Q15 | varchar |  |  | SI | Where: |
| Q16 | varchar |  |  | SI | • No cry: Child is not crying. |
| Q17 | varchar |  |  | SI | • Moaning: Child is moaning or quietly vocalizing ... |
| Q18 | varchar |  |  | SI | • Crying: Child is crying but the cry is gentle or... |
| Q19 | varchar |  |  | SI | • Screaming: Child is in a full-lunged cry; sobbin... |
| Q20 | varchar |  |  | SI | • Smiling: Score only if definite positive facial ... |
| Q21 | varchar |  |  | SI | • Composed: Neutral facial expression. |
| Q22 | varchar |  |  | SI | • Grimace: Score only if definite negative facial ... |
| Q23 | varchar |  |  | SI | • Positive (Verbal): Child makes any positive stat... |
| Q24 | varchar |  |  | SI | • None (Verbal): Child not talking. |
| Q25 | varchar |  |  | SI | • Complaints other than pain: Child complains but ... |
| Q26 | varchar |  |  | SI | • Pain complaints: Child complains about pain. |
| Q27 | varchar |  |  | SI | • Both pain and non-pain complaints: Child complai... |
| Q28 | varchar |  |  | SI | • Neutral (Torso): Body (Not limbs) is at rest; To... |
| Q29 | varchar |  |  | SI | • Shifting: Body is in motion in a shifting or ser... |
| Q30 | varchar |  |  | SI | • Tense: Body is arched or rigid. |
| Q31 | varchar |  |  | SI | • Shivering: Body is shuddering or shaking involun... |
| Q32 | varchar |  |  | SI | • Upright: Child is in a vertical or upright posit... |
| Q33 | varchar |  |  | SI | • Restrained: Body is restrained. |
| Q34 | varchar |  |  | SI | • Not touching: Child is not touching or grabbing ... |
| Q35 | varchar |  |  | SI | • Reach: Child is reaching for but not touching wo... |
| Q36 | varchar |  |  | SI | • Touch: Child is gently touching wound or wound a... |
| Q37 | varchar |  |  | SI | • Grab: Child is grabbing vigorously at wound. |
| Q38 | varchar |  |  | SI | • Restrained: Child's arms are restrained. |
| Q39 | varchar |  |  | SI | • Neutral (Legs): Legs may be in any position but ... |
| Q40 | varchar |  |  | SI | • Squirming kicking: Definitive uneasy or restless... |
| Q41 | varchar |  |  | SI | • Drawn up tensed: Legs tensed and/or pulled up ti... |
| Q42 | varchar |  |  | SI | • Standing: Standing crouching or kneeling. |
| Q43 | varchar |  |  | SI | • Restrained: Child's legs are being held down. |
| Q44 | varchar |  |  | SI | Scoring and analgesic administration: |
| Q45 | varchar |  |  | SI | • Score ≥ 5 should be considered for the administr... |
| Q46 | varchar |  |  | SI | Greater the score, greater the pain. |
| Q47 | varchar |  |  | SI | The CHEOPS (Children's Hospital of Eastern Ontario... |
| Q48 | varchar |  |  | SI | It can be used to monitor the effectiveness of int... |
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