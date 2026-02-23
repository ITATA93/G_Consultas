# questionnaire.QGXXXMDAU

> Day Assessment Unit

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Day Assessment Unit

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Referred by |
| Q02 | varchar |  |  | SI | Referred by other |
| Q02ObsDR | varchar |  | FK | SI | Referred by other DR |
| Q03 | varchar |  |  | SI | Reason for referral |
| Q03ObsDR | varchar |  | FK | SI | Reason for referral DR |
| Q04 | varchar |  |  | SI | Temperature |
| Q04ObsDR | varchar |  | FK | SI | Temperature DR |
| Q05 | varchar |  |  | SI | Pulse |
| Q05ObsDR | varchar |  | FK | SI | Pulse DR |
| Q06 | varchar |  |  | SI | Systolic blood pressure |
| Q06ObsDR | varchar |  | FK | SI | Systolic blood pressure DR |
| Q07 | varchar |  |  | SI | Diastolic blood pressure |
| Q07ObsDR | varchar |  | FK | SI | Diastolic blood pressure DR |
| Q08 | varchar |  |  | SI | Visual disturbance |
| Q08ObsDR | varchar |  | FK | SI | Visual disturbance DR |
| Q09 | varchar |  |  | SI | Headaches |
| Q09ObsDR | varchar |  | FK | SI | Headaches DR |
| Q10 | varchar |  |  | SI | Epigastric pain |
| Q10ObsDR | varchar |  | FK | SI | Epigastric pain DR |
| Q11 | varchar |  |  | SI | How are you feeling |
| Q11ObsDR | varchar |  | FK | SI | How are you feeling DR |
| Q12 | varchar |  |  | SI | Urinalysis |
| Q12ObsDR | varchar |  | FK | SI | Urinalysis DR |
| Q13 | varchar |  |  | SI | Oedema |
| Q13ObsDR | varchar |  | FK | SI | Oedema DR |
| Q14 | varchar |  |  | SI | Blood pressure profile performed |
| Q14ObsDR | varchar |  | FK | SI | Blood pressure profile performed DR |
| Q15 | varchar |  |  | SI | Fundal height |
| Q15ObsDR | varchar |  | FK | SI | Fundal height DR |
| Q16 | varchar |  |  | SI | Lie |
| Q16ObsDR | varchar |  | FK | SI | Lie DR |
| Q17 | varchar |  |  | SI | Presentation |
| Q17ObsDR | varchar |  | FK | SI | Presentation DR |
| Q18 | varchar |  |  | SI | Fetal Position |
| Q18ObsDR | varchar |  | FK | SI | Fetal Position DR |
| Q19 | varchar |  |  | SI | Presentation / 5ths palpable |
| Q19ObsDR | varchar |  | FK | SI | Presentation / 5ths palpable DR |
| Q20 | varchar |  |  | SI | Membranes |
| Q20ObsDR | varchar |  | FK | SI | Membranes DR |
| Q21 | varchar |  |  | SI | Fetal heart |
| Q21ObsDR | varchar |  | FK | SI | Fetal heart DR |
| Q23 | varchar |  |  | SI | CTG required |
| Q23ObsDR | varchar |  | FK | SI | CTG required DR |
| Q25 | numeric |  |  | SI | Number of contractions in 10mins |
| Q27 | varchar |  |  | SI | Fetal tone score |
| Q28 | varchar |  |  | SI | Fetal movement score |
| Q29 | varchar |  |  | SI | Amniotic fluid score |
| Q30 | varchar |  |  | SI | Fetal breathing score |
| Q31 | varchar |  |  | SI | Biophysical score |
| Q32 | varchar |  |  | SI | Vacuum Extraction Indication |
| Q32ObsDR | varchar |  | FK | SI | Vacuum Extraction Indication DR |
| Q33 | varchar |  |  | SI | Consent obtained |
| Q33ObsDR | varchar |  | FK | SI | Consent obtained DR |
| Q34 | varchar |  |  | SI | Cervical position |
| Q34ObsDR | varchar |  | FK | SI | Cervical position DR |
| Q35 | varchar |  |  | SI | Cervical consistency |
| Q35ObsDR | varchar |  | FK | SI | Cervical consistency DR |
| Q36 | varchar |  |  | SI | Cervical effacement / length |
| Q36ObsDR | varchar |  | FK | SI | Cervical effacement / length DR |
| Q37 | numeric |  |  | SI | Cervical dilation |
| Q38 | varchar |  |  | SI | Presenting part |
| Q38ObsDR | varchar |  | FK | SI | Presenting part DR |
| Q39 | varchar |  |  | SI | Relation to ischial spines |
| Q39ObsDR | varchar |  | FK | SI | Relation to ischial spines DR |
| Q40 | varchar |  |  | SI | Fetal position |
| Q40ObsDR | varchar |  | FK | SI | Fetal position DR |
| Q41 | varchar |  |  | SI | Caput |
| Q41ObsDR | varchar |  | FK | SI | Caput DR |
| Q42 | varchar |  |  | SI | Moulding |
| Q42ObsDR | varchar |  | FK | SI | Moulding DR |
| Q43 | varchar |  |  | SI | Comments |
| Q44 | varchar |  |  | SI | Follow-up |
| Q44ObsDR | varchar |  | FK | SI | Follow-up DR |
| Q45 | varchar |  |  | SI | Midwife countersigning |
| Q46 | varchar |  |  | SI | Fetal movements felt by mother |
| Q46ObsDR | varchar |  | FK | SI | Fetal movements felt by mother DR |
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