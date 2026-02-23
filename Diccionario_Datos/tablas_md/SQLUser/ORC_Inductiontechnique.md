# SQLUser.ORC_Inductiontechnique

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDTEC_RowId | bigint | PK |  | NO | - |
| INDTEC_Code | varchar |  |  | NO | Code |
| INDTEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INDTEC_CreatedDate | date |  |  | SI | Created Date |
| INDTEC_CreatedTime | time |  |  | SI | Created Time |
| INDTEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INDTEC_DateFrom | date |  |  | SI | Date From |
| INDTEC_DateTo | date |  |  | SI | Date To |
| INDTEC_Desc | varchar |  |  | NO | Description |
| INDTEC_Owner | varchar |  |  | SI | Owner |
| INDTEC_UpdatedDate | date |  |  | SI | Updated Date |
| INDTEC_UpdatedTime | time |  |  | SI | Updated Time |
| INDTEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Personal Data |
| Q02 | - |  |  | SI | Residence	 |
| Q03 | - |  |  | SI | Handedness	 |
| Q04 | - |  |  | SI | Bilingualism |
| Q05 | - |  |  | SI | Education	 |
| Q06 | - |  |  | SI | Occupation |
| Q07 | - |  |  | SI | Parent consanguinity	 |
| Q08 | - |  |  | SI | Mother's job	 |
| Q09 | - |  |  | SI | Father's job	 |
| Q10 | - |  |  | SI | Similar condition in the family	 |
| Q11 | - |  |  | SI | 2. Impact of Complaint on the Patient |
| Q12 | - |  |  | SI | Patient's rating of severity	 |
| Q13 | - |  |  | SI | Effect on daily life	 |
| Q14 | - |  |  | SI | Effect on social relationships	 |
| Q15 | - |  |  | SI | Effect on success in school / vacation	 |
| Q16 | - |  |  | SI | Listener's reaction (familiar / unfamiliar)	 |
| Q17 | - |  |  | SI | 3. Development History |
| Q18 | - |  |  | SI | Prenatal |
| Q19 | - |  |  | SI | Perinatal |
| Q20 | - |  |  | SI | Postnatal	 |
| Q21 | - |  |  | SI | 4. Developmental Milestones |
| Q22 | - |  |  | SI | Parent recognition |
| Q23 | - |  |  | SI | Walking |
| Q24 | - |  |  | SI | Sitting |
| Q25 | - |  |  | SI | Toilet training	 |
| Q26 | - |  |  | SI | 5. Language Development |
| Q27 | - |  |  | SI | First word	 |
| Q28 | - |  |  | SI | First sentence	 |
| Q29 | - |  |  | SI | 6. Stuttering History |
| Q30 | - |  |  | SI | Possible cause	 |
| Q31 | - |  |  | SI | Awareness |
| Q32 | - |  |  | SI | Difficult words	 |
| Q33 | - |  |  | SI | Avoidance	 |
| Q34 | - |  |  | SI | Worsening (person / situation)	 |
| Q35 | - |  |  | SI | Improving (person / situation)	 |
| Q36 | - |  |  | SI | 7. Behaviour |
| Q37 | - |  |  | SI | Behaviour	 |
| Q38 | - |  |  | SI | 8. Rehabilitation History / Previous Therapy |
| Q39 | - |  |  | SI | Place |
| Q40 | - |  |  | SI | At age of (years) |
| Q41 | - |  |  | SI | Number of sessions	 |
| Q42 | - |  |  | SI | Compliance	 |
| Q43 | - |  |  | SI | Effect |
| Q44 | - |  |  | SI | Disfluency pattern |
| Q45 | - |  |  | SI | Secondary behaviours	 |
| Q46 | - |  |  | SI | If Others, please specify	 |
| Q47 | - |  |  | SI | Breathing patterns	 |
| Q48 | - |  |  | SI | Stuttering Severity Instrument (SSI)	 |
| Q49 | - |  |  | SI | Frequency |
| Q50 | - |  |  | SI | Duration |
| Q51 | - |  |  | SI | Physical concomitants	 |
| Q52 | - |  |  | SI | Total	 |
| Q53 | - |  |  | SI | Oral motor examination	 |
| Q54 | - |  |  | SI | Any additional information	 |
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