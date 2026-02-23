# SQLUser.NR_CarePlanIssues

**Schema:** SQLUser
**Columnas:** 181
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ISS_ParRef | bigint | PK |  | NO | NR_CarePlan Parent Reference |
| ChildQ18DR | - |  |  | SI | Child Reference: CTG |
| ISS_Actions | varchar |  |  | SI | Actions |
| ISS_Aims | varchar |  |  | SI | Aims |
| ISS_CarePlanGoal_DR | bigint |  | FK | SI | Goal |
| ISS_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| ISS_CareProviderType_DR | bigint |  | FK | SI | Care Provider Type of Adding User |
| ISS_Childsub | double |  |  | NO | Childsub |
| ISS_ClinPathOutcome_DR | bigint |  | FK | SI | Des Ref to MRCClinPathOutcome |
| ISS_CreateDate | date |  |  | SI | Creation Date |
| ISS_CreateTime | time |  |  | SI | Creation Time |
| ISS_CreateUser_DR | bigint |  | FK | SI | Creation User |
| ISS_EndDate | date |  |  | SI | End Date |
| ISS_Issues_DR | bigint |  | FK | SI | Des Ref NRCIssues |
| ISS_OtherProviders | varchar |  |  | SI | OtherProviders |
| ISS_Outcome | varchar |  |  | SI | Outcome |
| ISS_ReviewDate | date |  |  | SI | ReviewDate |
| ISS_ReviewProgress | varchar |  |  | SI | ReviewProgress |
| ISS_RowId | varchar |  |  | NO | - |
| ISS_StartDate | date |  |  | SI | Start Date |
| Q01 | - |  |  | SI | Explanation given |
| Q01ObsDR | - |  |  | SI | Explanation given DR |
| Q02 | - |  |  | SI | Decision to induce |
| Q03 | - |  |  | SI | Any uterine activity |
| Q04 | - |  |  | SI | Lie |
| Q04ObsDR | - |  |  | SI | Lie DR |
| Q05 | - |  |  | SI | Presentation |
| Q05ObsDR | - |  |  | SI | Presentation DR |
| Q06 | - |  |  | SI | Position |
| Q06ObsDR | - |  |  | SI | Position DR |
| Q07 | - |  |  | SI | Presention / 5ths palpable |
| Q07ObsDR | - |  |  | SI | Presention / 5ths palpable DR |
| Q08 | - |  |  | SI | PV loss |
| Q08ObsDR | - |  |  | SI | PV loss DR |
| Q09 | - |  |  | SI | Vaginal gel given |
| Q09ObsDR | - |  |  | SI | Vaginal gel given DR |
| Q10 | - |  |  | SI | Vaginal gel dose |
| Q10ObsDR | - |  |  | SI | Vaginal gel dose DR |
| Q11 | - |  |  | SI | Membranes ruptured |
| Q11ObsDR | - |  |  | SI | Membranes ruptured DR |
| Q12 | - |  |  | SI | Liqour clear |
| Q12ObsDR | - |  |  | SI | Liqour clear DR |
| Q13 | - |  |  | SI | Liqour blood stained |
| Q13ObsDR | - |  |  | SI | Liqour blood stained DR |
| Q14 | - |  |  | SI | Liqour meconium stained |
| Q14ObsDR | - |  |  | SI | Liqour meconium stained DR |
| Q15 | - |  |  | SI | Spontaneous rupture of membranes date |
| Q16 | - |  |  | SI | Spontaneous rupture of membranes time |
| Q17 | - |  |  | SI | Comments |
| Q19 | - |  |  | SI | Unreactive |
| Q20 | - |  |  | SI | Dilation |
| Q20ObsDR | - |  |  | SI | Dilation DR |
| Q21 | - |  |  | SI | Cervical length |
| Q21ObsDR | - |  |  | SI | Cervical length DR |
| Q22 | - |  |  | SI | Consistency |
| Q22ObsDR | - |  |  | SI | Consistency DR |
| Q23 | - |  |  | SI | Position |
| Q23ObsDR | - |  |  | SI | Position DR |
| Q24 | - |  |  | SI | Midwife countersigning |
| Q25 | - |  |  | SI | Verbal consent obtained |
| Q25ObsDR | - |  |  | SI | Verbal consent obtained DR |
| Q26 | - |  |  | SI | Gestation: Weeks |
| Q26ObsDR | - |  |  | SI | Gestation: Weeks DR |
| Q27 | - |  |  | SI | Indication for induction |
| Q28 | - |  |  | SI | History of contractions |
| Q28ObsDR | - |  |  | SI | History of contractions DR |
| Q29 | - |  |  | SI | Systolic blood pressure |
| Q29ObsDR | - |  |  | SI | Systolic blood pressure DR |
| Q30 | - |  |  | SI | Diastolic Blood pressure |
| Q30ObsDR | - |  |  | SI | Diastolic Blood pressure DR |
| Q31 | - |  |  | SI | Pulse |
| Q31ObsDR | - |  |  | SI | Pulse DR |
| Q32 | - |  |  | SI | Temperature |
| Q32ObsDR | - |  |  | SI | Temperature DR |
| Q33 | - |  |  | SI | Urinalysis |
| Q33ObsDR | - |  |  | SI | Urinalysis DR |
| Q34 | - |  |  | SI | Urinalysis abnormalities |
| Q34ObsDR | - |  |  | SI | Urinalysis abnormalities DR |
| Q35 | - |  |  | SI | Oedema |
| Q35ObsDR | - |  |  | SI | Oedema DR |
| Q36 | - |  |  | SI | Fetal movements felt |
| Q36ObsDR | - |  |  | SI | Fetal movements felt DR |
| Q37 | - |  |  | SI | Fundal height |
| Q37ObsDR | - |  |  | SI | Fundal height DR |
| Q38 | - |  |  | SI | Induction methods |
| Q39 | - |  |  | SI | Assessment number |
| Q39ObsDR | - |  |  | SI | Assessment number DR |
| Q40 | - |  |  | SI | Parity |
| Q40ObsDR | - |  |  | SI | Parity DR |
| Q41 | - |  |  | SI | Propess removed |
| Q41ObsDR | - |  |  | SI | Propess removed DR |
| Q42 | - |  |  | SI | Suitable for OP Propess |
| Q42ObsDR | - |  |  | SI | Suitable for OP Propess DR |
| Q43 | - |  |  | SI | Inpatient induction with Propess |
| Q43ObsDR | - |  |  | SI | Inpatient induction with Propess DR |
| Q44 | - |  |  | SI | IP induction with other |
| Q44ObsDR | - |  |  | SI | IP induction with other DR |
| Q45 | - |  |  | SI | Outpatient information leaflet given |
| Q45ObsDR | - |  |  | SI | Outpatient information leaflet given DR |
| Q46 | - |  |  | SI | Membrane sweep offered and accepted |
| Q46ObsDR | - |  |  | SI | Membrane sweep offered and accepted DR |
| Q47 | - |  |  | SI | Reasons if not accepted |
| Q48 | - |  |  | SI | Is current care low risk |
| Q48ObsDR | - |  |  | SI | Is current care low risk DR |
| Q49 | - |  |  | SI | Is maternal age <40 |
| Q49ObsDR | - |  |  | SI | Is maternal age <40 DR |
| Q50 | - |  |  | SI | Para 3 or less |
| Q50ObsDR | - |  |  | SI | Para 3 or less DR |
| Q51 | - |  |  | SI | is the head engaged |
| Q51ObsDR | - |  |  | SI | is the head engaged DR |
| Q52 | - |  |  | SI | Is this woman postdates |
| Q52ObsDR | - |  |  | SI | Is this woman postdates DR |
| Q53 | - |  |  | SI | Discussed with consultant |
| Q53ObsDR | - |  |  | SI | Discussed with consultant DR |
| Q54 | - |  |  | SI | Discussion details |
| Q55 | - |  |  | SI | Requested review by medical staff |
| Q55ObsDR | - |  |  | SI | Requested review by medical staff DR |
| Q56 | - |  |  | SI | Person booking induction |
| Q57 | - |  |  | SI | Propess removed date |
| Q58 | - |  |  | SI | Midwife countersigning |
| Q59 | - |  |  | SI | Position |
| Q60 | - |  |  | SI | Consistency |
| Q61 | - |  |  | SI | Effacement |
| Q62 | - |  |  | SI | Dilation |
| Q63 | - |  |  | SI | Station |
| Q64 | - |  |  | SI | Score |
| Q65 | - |  |  | SI | Cervical length |
| Q66 | - |  |  | SI | Fetal heart rate |
| Q66ObsDR | - |  |  | SI | Fetal heart rate DR |
| Q67 | - |  |  | SI | Notes |
| Q68 | - |  |  | SI | Contractions |
| Q68A | - |  |  | SI | Strength |
| Q68AObsDR | - |  |  | SI | Strength DR |
| Q68B | - |  |  | SI | Regularity |
| Q68BObsDR | - |  |  | SI | Regularity DR |
| Q68C | - |  |  | SI | No/10 min |
| Q68CObsDR | - |  |  | SI | No/10 min DR |
| Q72 | - |  |  | SI | Gestation: Days |
| Q72ObsDR | - |  |  | SI | Gestation: Days DR |
| Q73 | - |  |  | SI | Date |
| Q74 | - |  |  | SI | Time |
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