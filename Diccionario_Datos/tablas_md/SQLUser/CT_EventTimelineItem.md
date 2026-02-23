# SQLUser.CT_EventTimelineItem

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVTI_ParRef | bigint | PK |  | NO | Parent table |
| EVTI_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| EVTI_CreatedDate | date |  |  | SI | Created Date |
| EVTI_CreatedTime | time |  |  | SI | Created Time |
| EVTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVTI_DateFrom | date |  |  | NO | Date From |
| EVTI_DateTo | date |  |  | SI | Date To |
| EVTI_RowID | varchar |  |  | NO | - |
| EVTI_Sequence | integer |  |  | NO | Sequence |
| EVTI_TimelineEvent_DR | bigint |  | FK | NO | Timeline Event |
| EVTI_UpdatedDate | date |  |  | SI | Updated Date |
| EVTI_UpdatedTime | time |  |  | SI | Updated Time |
| EVTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Possible causes of hearing impairment	 |
| Q02 | - |  |  | SI | Deformation of the ear	 |
| Q03 | - |  |  | SI | Atresia / Microtia of external canal	 |
| Q04 | - |  |  | SI | Middle ear anomalies	 |
| Q05 | - |  |  | SI | Infections |
| Q06 | - |  |  | SI | Acute and chronic suppurative otitis media	 |
| Q07 | - |  |  | SI | Chronic purulent otitis media with ossicular destr... |
| Q08 | - |  |  | SI | Severe General Intelligibility (GI) with dehydrati... |
| Q09 | - |  |  | SI | Meningitis |
| Q10 | - |  |  | SI | Typhoid fever	 |
| Q11 | - |  |  | SI | Rubella |
| Q12 | - |  |  | SI | Rheumatic fever	 |
| Q13 | - |  |  | SI | Toxic intake during pregnancy	 |
| Q14 | - |  |  | SI | Gentamycin	 |
| Q15 | - |  |  | SI | Kanamycin |
| Q16 | - |  |  | SI | Neomycin |
| Q17 | - |  |  | SI | Garamycin |
| Q18 | - |  |  | SI | Tobramycin	 |
| Q19 | - |  |  | SI | Streptomycin |
| Q20 | - |  |  | SI | Aspirin	 |
| Q21 | - |  |  | SI | Others (specify)	 |
| Q22 | - |  |  | SI | Oxygen deprivation	 |
| Q23 | - |  |  | SI | Anoxia at birth	 |
| Q24 | - |  |  | SI | Long / Obstructed labor	 |
| Q25 | - |  |  | SI | Heavy material sedation	 |
| Q26 | - |  |  | SI | Obstruction of the respiratory passage with mucus	 |
| Q27 | - |  |  | SI | Trauma |
| Q28 | - |  |  | SI | Indirect trauma of the head	 |
| Q29 | - |  |  | SI | Direct trauma of the cochlea	 |
| Q30 | - |  |  | SI | Intra-cranial hemorrhage due to maternal pelvic ab... |
| Q31 | - |  |  | SI | Mal-presentation at birth	 |
| Q32 | - |  |  | SI | Rh and other incompatibilities	 |
| Q33 | - |  |  | SI | Means of communication	 |
| Q34 | - |  |  | SI | Past history of hearing aid use	 |
| Q35 | - |  |  | SI | Age |
| Q36 | - |  |  | SI | Duration	 |
| Q37 | - |  |  | SI | Type	 |
| Q38 | - |  |  | SI | How long / days	 |
| Q39 | - |  |  | SI | Any noticeable response to sound after aid	 |
| Q40 | - |  |  | SI | Previous intervention	 |
| Q41 | - |  |  | SI | Place	 |
| Q42 | - |  |  | SI | At age of	 |
| Q43 | - |  |  | SI | Duration	 |
| Q44 | - |  |  | SI | Frequency	 |
| Q45 | - |  |  | SI | Compliance	 |
| Q46 | - |  |  | SI | Effect |
| Q47 | - |  |  | SI | Examination	 |
| Q48 | - |  |  | SI | Speech |
| Q49 | - |  |  | SI | Prosody, Rate	 |
| Q50 | - |  |  | SI | Prosody, Stress	 |
| Q51 | - |  |  | SI | Prosody, Tonality	 |
| Q52 | - |  |  | SI | Articulation, Consonance	 |
| Q53 | - |  |  | SI | Resonance	 |
| Q54 | - |  |  | SI | General Intelligibility (GI) |
| Q55 | - |  |  | SI | Voice |
| Q56 | - |  |  | SI | Grade of dysphonia |
| Q57 | - |  |  | SI | Quality	 |
| Q58 | - |  |  | SI | Pitch |
| Q59 | - |  |  | SI | Loudness	 |
| Q60 | - |  |  | SI | Lip reading ability	 |
| Q61 | - |  |  | SI | Ability to imitate	 |
| Q62 | - |  |  | SI | Oral motor examination	 |
| Q63 | - |  |  | SI | Language assessment	 |
| Q64 | - |  |  | SI | Diagnosis |
| Q65 | - |  |  | SI | Recommendation	 |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*