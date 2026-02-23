# questionnaire.QTCDISFA

> Disfluency Assessment

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Disfluency Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Personal Data |
| Q02 | varchar |  |  | SI | Residence	 |
| Q03 | varchar |  |  | SI | Handedness	 |
| Q04 | varchar |  |  | SI | Bilingualism |
| Q05 | varchar |  |  | SI | Education	 |
| Q06 | varchar |  |  | SI | Occupation |
| Q07 | varchar |  |  | SI | Parent consanguinity	 |
| Q08 | varchar |  |  | SI | Mother's job	 |
| Q09 | varchar |  |  | SI | Father's job	 |
| Q10 | varchar |  |  | SI | Similar condition in the family	 |
| Q11 | varchar |  |  | SI | 2. Impact of Complaint on the Patient |
| Q12 | varchar |  |  | SI | Patient's rating of severity	 |
| Q13 | varchar |  |  | SI | Effect on daily life	 |
| Q14 | varchar |  |  | SI | Effect on social relationships	 |
| Q15 | varchar |  |  | SI | Effect on success in school / vacation	 |
| Q16 | varchar |  |  | SI | Listener's reaction (familiar / unfamiliar)	 |
| Q17 | varchar |  |  | SI | 3. Development History |
| Q18 | varchar |  |  | SI | Prenatal |
| Q19 | varchar |  |  | SI | Perinatal |
| Q20 | varchar |  |  | SI | Postnatal	 |
| Q21 | varchar |  |  | SI | 4. Developmental Milestones |
| Q22 | varchar |  |  | SI | Parent recognition |
| Q23 | varchar |  |  | SI | Walking |
| Q24 | varchar |  |  | SI | Sitting |
| Q25 | varchar |  |  | SI | Toilet training	 |
| Q26 | varchar |  |  | SI | 5. Language Development |
| Q27 | varchar |  |  | SI | First word	 |
| Q28 | varchar |  |  | SI | First sentence	 |
| Q29 | varchar |  |  | SI | 6. Stuttering History |
| Q30 | varchar |  |  | SI | Possible cause	 |
| Q31 | varchar |  |  | SI | Awareness |
| Q32 | varchar |  |  | SI | Difficult words	 |
| Q33 | varchar |  |  | SI | Avoidance	 |
| Q34 | varchar |  |  | SI | Worsening (person / situation)	 |
| Q35 | varchar |  |  | SI | Improving (person / situation)	 |
| Q36 | varchar |  |  | SI | 7. Behaviour |
| Q37 | varchar |  |  | SI | Behaviour	 |
| Q38 | varchar |  |  | SI | 8. Rehabilitation History / Previous Therapy |
| Q39 | varchar |  |  | SI | Place |
| Q40 | varchar |  |  | SI | At age of (years) |
| Q41 | varchar |  |  | SI | Number of sessions	 |
| Q42 | varchar |  |  | SI | Compliance	 |
| Q43 | varchar |  |  | SI | Effect |
| Q44 | varchar |  |  | SI | Disfluency pattern |
| Q45 | varchar |  |  | SI | Secondary behaviours	 |
| Q46 | varchar |  |  | SI | If Others, please specify	 |
| Q47 | varchar |  |  | SI | Breathing patterns	 |
| Q48 | varchar |  |  | SI | Stuttering Severity Instrument (SSI)	 |
| Q49 | varchar |  |  | SI | Frequency |
| Q50 | varchar |  |  | SI | Duration |
| Q51 | varchar |  |  | SI | Physical concomitants	 |
| Q52 | varchar |  |  | SI | Total	 |
| Q53 | varchar |  |  | SI | Oral motor examination	 |
| Q54 | varchar |  |  | SI | Any additional information	 |
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