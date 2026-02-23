# questionnaire.QGXXXMIA

> Induction Assessment

**Schema:** questionnaire
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Induction Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Explanation given |
| Q01ObsDR | varchar |  | FK | SI | Explanation given DR |
| Q02 | varchar |  |  | SI | Decision to induce |
| Q03 | varchar |  |  | SI | Any uterine activity |
| Q04 | varchar |  |  | SI | Lie |
| Q04ObsDR | varchar |  | FK | SI | Lie DR |
| Q05 | varchar |  |  | SI | Presentation |
| Q05ObsDR | varchar |  | FK | SI | Presentation DR |
| Q06 | varchar |  |  | SI | Position |
| Q06ObsDR | varchar |  | FK | SI | Position DR |
| Q07 | varchar |  |  | SI | Presention / 5ths palpable |
| Q07ObsDR | varchar |  | FK | SI | Presention / 5ths palpable DR |
| Q08 | varchar |  |  | SI | PV loss |
| Q08ObsDR | varchar |  | FK | SI | PV loss DR |
| Q09 | varchar |  |  | SI | Vaginal gel given |
| Q09ObsDR | varchar |  | FK | SI | Vaginal gel given DR |
| Q10 | varchar |  |  | SI | Vaginal gel dose |
| Q10ObsDR | varchar |  | FK | SI | Vaginal gel dose DR |
| Q11 | varchar |  |  | SI | Membranes ruptured |
| Q11ObsDR | varchar |  | FK | SI | Membranes ruptured DR |
| Q12 | varchar |  |  | SI | Liqour clear |
| Q12ObsDR | varchar |  | FK | SI | Liqour clear DR |
| Q13 | varchar |  |  | SI | Liqour blood stained |
| Q13ObsDR | varchar |  | FK | SI | Liqour blood stained DR |
| Q14 | varchar |  |  | SI | Liqour meconium stained |
| Q14ObsDR | varchar |  | FK | SI | Liqour meconium stained DR |
| Q15 | date |  |  | SI | Spontaneous rupture of membranes date |
| Q16 | time |  |  | SI | Spontaneous rupture of membranes time |
| Q17 | varchar |  |  | SI | Comments |
| Q19 | varchar |  |  | SI | Unreactive |
| Q20 | varchar |  |  | SI | Dilation |
| Q20ObsDR | varchar |  | FK | SI | Dilation DR |
| Q21 | varchar |  |  | SI | Cervical length |
| Q21ObsDR | varchar |  | FK | SI | Cervical length DR |
| Q22 | varchar |  |  | SI | Consistency |
| Q22ObsDR | varchar |  | FK | SI | Consistency DR |
| Q23 | varchar |  |  | SI | Position |
| Q23ObsDR | varchar |  | FK | SI | Position DR |
| Q24 | varchar |  |  | SI | Midwife countersigning |
| Q25 | varchar |  |  | SI | Verbal consent obtained |
| Q25ObsDR | varchar |  | FK | SI | Verbal consent obtained DR |
| Q26 | varchar |  |  | SI | Gestation: Weeks |
| Q26ObsDR | varchar |  | FK | SI | Gestation: Weeks DR |
| Q27 | varchar |  |  | SI | Indication for induction |
| Q28 | varchar |  |  | SI | History of contractions |
| Q28ObsDR | varchar |  | FK | SI | History of contractions DR |
| Q29 | varchar |  |  | SI | Systolic blood pressure |
| Q29ObsDR | varchar |  | FK | SI | Systolic blood pressure DR |
| Q30 | varchar |  |  | SI | Diastolic Blood pressure |
| Q30ObsDR | varchar |  | FK | SI | Diastolic Blood pressure DR |
| Q31 | varchar |  |  | SI | Pulse |
| Q31ObsDR | varchar |  | FK | SI | Pulse DR |
| Q32 | varchar |  |  | SI | Temperature |
| Q32ObsDR | varchar |  | FK | SI | Temperature DR |
| Q33 | varchar |  |  | SI | Urinalysis |
| Q33ObsDR | varchar |  | FK | SI | Urinalysis DR |
| Q34 | varchar |  |  | SI | Urinalysis abnormalities |
| Q34ObsDR | varchar |  | FK | SI | Urinalysis abnormalities DR |
| Q35 | varchar |  |  | SI | Oedema |
| Q35ObsDR | varchar |  | FK | SI | Oedema DR |
| Q36 | varchar |  |  | SI | Fetal movements felt |
| Q36ObsDR | varchar |  | FK | SI | Fetal movements felt DR |
| Q37 | varchar |  |  | SI | Fundal height |
| Q37ObsDR | varchar |  | FK | SI | Fundal height DR |
| Q38 | varchar |  |  | SI | Induction methods |
| Q39 | varchar |  |  | SI | Assessment number |
| Q39ObsDR | varchar |  | FK | SI | Assessment number DR |
| Q40 | varchar |  |  | SI | Parity |
| Q40ObsDR | varchar |  | FK | SI | Parity DR |
| Q41 | varchar |  |  | SI | Propess removed |
| Q41ObsDR | varchar |  | FK | SI | Propess removed DR |
| Q42 | varchar |  |  | SI | Suitable for OP Propess |
| Q42ObsDR | varchar |  | FK | SI | Suitable for OP Propess DR |
| Q43 | varchar |  |  | SI | Inpatient induction with Propess |
| Q43ObsDR | varchar |  | FK | SI | Inpatient induction with Propess DR |
| Q44 | varchar |  |  | SI | IP induction with other |
| Q44ObsDR | varchar |  | FK | SI | IP induction with other DR |
| Q45 | varchar |  |  | SI | Outpatient information leaflet given |
| Q45ObsDR | varchar |  | FK | SI | Outpatient information leaflet given DR |
| Q46 | varchar |  |  | SI | Membrane sweep offered and accepted |
| Q46ObsDR | varchar |  | FK | SI | Membrane sweep offered and accepted DR |
| Q47 | varchar |  |  | SI | Reasons if not accepted |
| Q48 | varchar |  |  | SI | Is current care low risk |
| Q48ObsDR | varchar |  | FK | SI | Is current care low risk DR |
| Q49 | varchar |  |  | SI | Is maternal age <40 |
| Q49ObsDR | varchar |  | FK | SI | Is maternal age <40 DR |
| Q50 | varchar |  |  | SI | Para 3 or less |
| Q50ObsDR | varchar |  | FK | SI | Para 3 or less DR |
| Q51 | varchar |  |  | SI | is the head engaged |
| Q51ObsDR | varchar |  | FK | SI | is the head engaged DR |
| Q52 | varchar |  |  | SI | Is this woman postdates |
| Q52ObsDR | varchar |  | FK | SI | Is this woman postdates DR |
| Q53 | varchar |  |  | SI | Discussed with consultant |
| Q53ObsDR | varchar |  | FK | SI | Discussed with consultant DR |
| Q54 | varchar |  |  | SI | Discussion details |
| Q55 | varchar |  |  | SI | Requested review by medical staff |
| Q55ObsDR | varchar |  | FK | SI | Requested review by medical staff DR |
| Q56 | varchar |  |  | SI | Person booking induction |
| Q57 | date |  |  | SI | Propess removed date |
| Q58 | varchar |  |  | SI | Midwife countersigning |
| Q59 | varchar |  |  | SI | Position |
| Q60 | varchar |  |  | SI | Consistency |
| Q61 | varchar |  |  | SI | Effacement |
| Q62 | varchar |  |  | SI | Dilation |
| Q63 | varchar |  |  | SI | Station |
| Q64 | varchar |  |  | SI | Score |
| Q65 | varchar |  |  | SI | Cervical length |
| Q66 | varchar |  |  | SI | Fetal heart rate |
| Q66ObsDR | varchar |  | FK | SI | Fetal heart rate DR |
| Q67 | varchar |  |  | SI | Notes |
| Q68 | varchar |  |  | SI | Contractions |
| Q68A | varchar |  |  | SI | Strength |
| Q68AObsDR | varchar |  | FK | SI | Strength DR |
| Q68B | varchar |  |  | SI | Regularity |
| Q68BObsDR | varchar |  | FK | SI | Regularity DR |
| Q68C | varchar |  |  | SI | No/10 min |
| Q68CObsDR | varchar |  | FK | SI | No/10 min DR |
| Q72 | varchar |  |  | SI | Gestation: Days |
| Q72ObsDR | varchar |  | FK | SI | Gestation: Days DR |
| Q73 | date |  |  | SI | Date |
| Q74 | time |  |  | SI | Time |
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