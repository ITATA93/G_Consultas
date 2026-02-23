# questionnaire.QTCACIPA

> Adult Cochlear Implant Patient Assessment

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Cochlear Implant Patient Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Possible causes of hearing impairment	 |
| Q02 | varchar |  |  | SI | Deformation of the ear	 |
| Q03 | varchar |  |  | SI | Atresia / Microtia of external canal	 |
| Q04 | varchar |  |  | SI | Middle ear anomalies	 |
| Q05 | varchar |  |  | SI | Infections |
| Q06 | varchar |  |  | SI | Acute and chronic suppurative otitis media	 |
| Q07 | varchar |  |  | SI | Chronic purulent otitis media with ossicular destr... |
| Q08 | varchar |  |  | SI | Severe General Intelligibility (GI) with dehydrati... |
| Q09 | varchar |  |  | SI | Meningitis |
| Q10 | varchar |  |  | SI | Typhoid fever	 |
| Q11 | varchar |  |  | SI | Rubella |
| Q12 | varchar |  |  | SI | Rheumatic fever	 |
| Q13 | varchar |  |  | SI | Toxic intake during pregnancy	 |
| Q14 | varchar |  |  | SI | Gentamycin	 |
| Q15 | varchar |  |  | SI | Kanamycin |
| Q16 | varchar |  |  | SI | Neomycin |
| Q17 | varchar |  |  | SI | Garamycin |
| Q18 | varchar |  |  | SI | Tobramycin	 |
| Q19 | varchar |  |  | SI | Streptomycin |
| Q20 | varchar |  |  | SI | Aspirin	 |
| Q21 | varchar |  |  | SI | Others (specify)	 |
| Q22 | varchar |  |  | SI | Oxygen deprivation	 |
| Q23 | varchar |  |  | SI | Anoxia at birth	 |
| Q24 | varchar |  |  | SI | Long / Obstructed labor	 |
| Q25 | varchar |  |  | SI | Heavy material sedation	 |
| Q26 | varchar |  |  | SI | Obstruction of the respiratory passage with mucus	 |
| Q27 | varchar |  |  | SI | Trauma |
| Q28 | varchar |  |  | SI | Indirect trauma of the head	 |
| Q29 | varchar |  |  | SI | Direct trauma of the cochlea	 |
| Q30 | varchar |  |  | SI | Intra-cranial hemorrhage due to maternal pelvic ab... |
| Q31 | varchar |  |  | SI | Mal-presentation at birth	 |
| Q32 | varchar |  |  | SI | Rh and other incompatibilities	 |
| Q33 | varchar |  |  | SI | Means of communication	 |
| Q34 | varchar |  |  | SI | Past history of hearing aid use	 |
| Q35 | varchar |  |  | SI | Age |
| Q36 | varchar |  |  | SI | Duration	 |
| Q37 | varchar |  |  | SI | Type	 |
| Q38 | varchar |  |  | SI | How long / days	 |
| Q39 | varchar |  |  | SI | Any noticeable response to sound after aid	 |
| Q40 | varchar |  |  | SI | Previous intervention	 |
| Q41 | varchar |  |  | SI | Place	 |
| Q42 | varchar |  |  | SI | At age of	 |
| Q43 | varchar |  |  | SI | Duration	 |
| Q44 | varchar |  |  | SI | Frequency	 |
| Q45 | varchar |  |  | SI | Compliance	 |
| Q46 | varchar |  |  | SI | Effect |
| Q47 | varchar |  |  | SI | Examination	 |
| Q48 | varchar |  |  | SI | Speech |
| Q49 | varchar |  |  | SI | Prosody, Rate	 |
| Q50 | varchar |  |  | SI | Prosody, Stress	 |
| Q51 | varchar |  |  | SI | Prosody, Tonality	 |
| Q52 | varchar |  |  | SI | Articulation, Consonance	 |
| Q53 | varchar |  |  | SI | Resonance	 |
| Q54 | varchar |  |  | SI | General Intelligibility (GI) |
| Q55 | varchar |  |  | SI | Voice |
| Q56 | varchar |  |  | SI | Grade of dysphonia  |
| Q57 | varchar |  |  | SI | Quality	 |
| Q58 | varchar |  |  | SI | Pitch |
| Q59 | varchar |  |  | SI | Loudness	 |
| Q60 | varchar |  |  | SI | Lip reading ability	 |
| Q61 | varchar |  |  | SI | Ability to imitate	 |
| Q62 | varchar |  |  | SI | Oral motor examination	 |
| Q63 | varchar |  |  | SI | Language assessment	 |
| Q64 | varchar |  |  | SI | Diagnosis |
| Q65 | varchar |  |  | SI | Recommendation	 |
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