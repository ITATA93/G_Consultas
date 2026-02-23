# SQLUser.INC_SterilePriority

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPRI_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Cry |
| Q04 | - |  |  | SI | Facial |
| Q05 | - |  |  | SI | Child verbal |
| Q06 | - |  |  | SI | Torso |
| Q07 | - |  |  | SI | Touch |
| Q08 | - |  |  | SI | Legs |
| Q10 | - |  |  | SI | Guidelines |
| Q11 | - |  |  | SI | Patients: |
| Q12 | - |  |  | SI | • The initial study was done on children 1 to 5 ye... |
| Q13 | - |  |  | SI | • It has been used in studies with adolescents but... |
| Q14 | - |  |  | SI | • According to Mitchell (1999) it is intended for ... |
| Q15 | - |  |  | SI | Where: |
| Q16 | - |  |  | SI | • No cry: Child is not crying. |
| Q17 | - |  |  | SI | • Moaning: Child is moaning or quietly vocalizing ... |
| Q18 | - |  |  | SI | • Crying: Child is crying but the cry is gentle or... |
| Q19 | - |  |  | SI | • Screaming: Child is in a full-lunged cry |
| Q20 | - |  |  | SI | • Smiling: Score only if definite positive facial ... |
| Q21 | - |  |  | SI | • Composed: Neutral facial expression. |
| Q22 | - |  |  | SI | • Grimace: Score only if definite negative facial ... |
| Q23 | - |  |  | SI | • Positive (Verbal): Child makes any positive stat... |
| Q24 | - |  |  | SI | • None (Verbal): Child not talking. |
| Q25 | - |  |  | SI | • Complaints other than pain: Child complains but ... |
| Q26 | - |  |  | SI | • Pain complaints: Child complains about pain. |
| Q27 | - |  |  | SI | • Both pain and non-pain complaints: Child complai... |
| Q28 | - |  |  | SI | • Neutral (Torso): Body (Not limbs) is at rest |
| Q29 | - |  |  | SI | • Shifting: Body is in motion in a shifting or ser... |
| Q30 | - |  |  | SI | • Tense: Body is arched or rigid. |
| Q31 | - |  |  | SI | • Shivering: Body is shuddering or shaking involun... |
| Q32 | - |  |  | SI | • Upright: Child is in a vertical or upright posit... |
| Q33 | - |  |  | SI | • Restrained: Body is restrained. |
| Q34 | - |  |  | SI | • Not touching: Child is not touching or grabbing ... |
| Q35 | - |  |  | SI | • Reach: Child is reaching for but not touching wo... |
| Q36 | - |  |  | SI | • Touch: Child is gently touching wound or wound a... |
| Q37 | - |  |  | SI | • Grab: Child is grabbing vigorously at wound. |
| Q38 | - |  |  | SI | • Restrained: Child's arms are restrained. |
| Q39 | - |  |  | SI | • Neutral (Legs): Legs may be in any position but ... |
| Q40 | - |  |  | SI | • Squirming kicking: Definitive uneasy or restless... |
| Q41 | - |  |  | SI | • Drawn up tensed: Legs tensed and/or pulled up ti... |
| Q42 | - |  |  | SI | • Standing: Standing crouching or kneeling. |
| Q43 | - |  |  | SI | • Restrained: Child's legs are being held down. |
| Q44 | - |  |  | SI | Scoring and analgesic administration: |
| Q45 | - |  |  | SI | • Score ≥ 5 should be considered for the administr... |
| Q46 | - |  |  | SI | Greater the score, greater the pain. |
| Q47 | - |  |  | SI | The CHEOPS (Children's Hospital of Eastern Ontario... |
| Q48 | - |  |  | SI | It can be used to monitor the effectiveness of int... |
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
| SPRI_Code | varchar |  |  | NO | Code |
| SPRI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPRI_CreatedDate | date |  |  | SI | Created Date |
| SPRI_CreatedTime | time |  |  | SI | Created Time |
| SPRI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPRI_Desc | varchar |  |  | NO | Description |
| SPRI_Owner | varchar |  |  | SI | Owner |
| SPRI_UpdatedDate | date |  |  | SI | Updated Date |
| SPRI_UpdatedTime | time |  |  | SI | Updated Time |
| SPRI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*