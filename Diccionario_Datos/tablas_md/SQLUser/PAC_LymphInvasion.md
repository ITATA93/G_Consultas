# SQLUser.PAC_LymphInvasion

**Schema:** SQLUser
**Columnas:** 167
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LYMI_RowId | bigint | PK |  | NO | - |
| LYMI_Code | varchar |  |  | NO | Code |
| LYMI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LYMI_CreatedDate | date |  |  | SI | Created Date |
| LYMI_CreatedTime | time |  |  | SI | Created Time |
| LYMI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LYMI_Desc | varchar |  |  | NO | Description |
| LYMI_Owner | varchar |  |  | SI | Owner |
| LYMI_UpdatedDate | date |  |  | SI | Updated Date |
| LYMI_UpdatedTime | time |  |  | SI | Updated Time |
| LYMI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Elementary Diagnostic Procedures:	 |
| Q02 | - |  |  | SI | Interview	 |
| Q03 | - |  |  | SI | Duration |
| Q04 | - |  |  | SI | Onset	 |
| Q05 | - |  |  | SI | Course	 |
| Q06 | - |  |  | SI | Development History: |
| Q07 | - |  |  | SI | Prenatal |
| Q08 | - |  |  | SI | Others |
| Q09 | - |  |  | SI | Age of mother |
| Q10 | - |  |  | SI | Details |
| Q100 | - |  |  | SI | Left lateral	 |
| Q101 | - |  |  | SI | Passavant's ridge	 |
| Q102 | - |  |  | SI | Pharyngeal reflex	 |
| Q103 | - |  |  | SI | Tonsils size	 |
| Q104 | - |  |  | SI | Nose septal deviation	 |
| Q105 | - |  |  | SI | Turbinates, middle	 |
| Q106 | - |  |  | SI | Turbinates, inferior	 |
| Q107 | - |  |  | SI | Formal testing	 |
| Q108 | - |  |  | SI | Anticulation test phoneme	 |
| Q109 | - |  |  | SI | Language summary	 |
| Q11 | - |  |  | SI | Perinatal and neonatal	 |
| Q110 | - |  |  | SI | Psychometry, mental age	 |
| Q111 | - |  |  | SI | Psychometry, test used	 |
| Q112 | - |  |  | SI | Psychometry, social age	 |
| Q113 | - |  |  | SI | Psychometry, perpetual age	 |
| Q114 | - |  |  | SI | First diagnosis	 |
| Q115 | - |  |  | SI | Management plan	 |
| Q12 | - |  |  | SI | Type of labour	 |
| Q13 | - |  |  | SI | Term	 |
| Q14 | - |  |  | SI | Weight of baby	 |
| Q14ObsDR | - |  |  | SI | Weight of baby	 DR |
| Q15 | - |  |  | SI | Baby cry	 |
| Q16 | - |  |  | SI | Cyanosis |
| Q17 | - |  |  | SI | Jaundice |
| Q18 | - |  |  | SI | Resuscitation	 |
| Q19 | - |  |  | SI | Time of discovery of the problem	 |
| Q20 | - |  |  | SI | Other abnormalities	 |
| Q21 | - |  |  | SI | Nasal regurge of milk |
| Q22 | - |  |  | SI | Milestones:	 |
| Q23 | - |  |  | SI | Sitting |
| Q24 | - |  |  | SI | Walking	 |
| Q25 | - |  |  | SI | Teething |
| Q26 | - |  |  | SI | Toilet training	 |
| Q27 | - |  |  | SI | 1st word	 |
| Q28 | - |  |  | SI | 2nd word sentence	 |
| Q29 | - |  |  | SI | Self feeding	 |
| Q30 | - |  |  | SI | Operative intervention	 |
| Q31 | - |  |  | SI | Type |
| Q32 | - |  |  | SI | At age	 |
| Q33 | - |  |  | SI | Place	 |
| Q34 | - |  |  | SI | Lip	 |
| Q35 | - |  |  | SI | Palate |
| Q36 | - |  |  | SI | Secondary repair	 |
| Q37 | - |  |  | SI | Fistula repair	 |
| Q38 | - |  |  | SI | Effect	 |
| Q39 | - |  |  | SI | Regurge |
| Q40 | - |  |  | SI | Speech	 |
| Q41 | - |  |  | SI | Previous speed therapy	 |
| Q42 | - |  |  | SI | Subjective impression	 |
| Q43 | - |  |  | SI | Hearing	 |
| Q44 | - |  |  | SI | Swallowing |
| Q45 | - |  |  | SI | Mental ability	 |
| Q46 | - |  |  | SI | Scholastic achievement	 |
| Q47 | - |  |  | SI | Auditory Perceptual Analysis (APA) of patient's sp... |
| Q48 | - |  |  | SI | Nasality |
| Q49 | - |  |  | SI | Type |
| Q50 | - |  |  | SI | Degree |
| Q51 | - |  |  | SI | Consonants |
| Q52 | - |  |  | SI | Others |
| Q53 | - |  |  | SI | Compensatory articulatory mechanisms	 |
| Q54 | - |  |  | SI | Glottal	 |
| Q55 | - |  |  | SI | Pharyngeal	 |
| Q56 | - |  |  | SI | Facial grimace |
| Q57 | - |  |  | SI | Audible nasal air escape	 |
| Q58 | - |  |  | SI | Overall intelligibility	 |
| Q59 | - |  |  | SI | Factors causing unintelligibility	 |
| Q60 | - |  |  | SI | Open nasality	 |
| Q61 | - |  |  | SI | Consonant imprecision	 |
| Q62 | - |  |  | SI | Glottal articulation	 |
| Q63 | - |  |  | SI | Pharyngealisation of fricatives	 |
| Q64 | - |  |  | SI | Nasal emission	 |
| Q65 | - |  |  | SI | Visual assessment of vocal tract	 |
| Q66 | - |  |  | SI | Lips |
| Q67 | - |  |  | SI | Intact |
| Q68 | - |  |  | SI | Right cleft	 |
| Q69 | - |  |  | SI | Left cleft	 |
| Q70 | - |  |  | SI | Median cleft	 |
| Q71 | - |  |  | SI | Philtrum |
| Q72 | - |  |  | SI | Bite angle occlusion	 |
| Q73 | - |  |  | SI | Cross bite	 |
| Q74 | - |  |  | SI | Open bite	 |
| Q75 | - |  |  | SI | Over bite	 |
| Q76 | - |  |  | SI | Simple clinical tests	 |
| Q77 | - |  |  | SI | Gutzman's (A/I) test	 |
| Q78 | - |  |  | SI | Czermak's (cold mirror) test	 |
| Q79 | - |  |  | SI | Tongue size |
| Q80 | - |  |  | SI | Tongue protrusion	 |
| Q81 | - |  |  | SI | Tongue deviation	 |
| Q82 | - |  |  | SI | Tongue movement	 |
| Q83 | - |  |  | SI | Alveolus, intact	 |
| Q84 | - |  |  | SI | Alveolus, cleft	 |
| Q85 | - |  |  | SI | Hard palate, intact	 |
| Q86 | - |  |  | SI | Hard palate, cleft	 |
| Q87 | - |  |  | SI | Hard palate, scar	 |
| Q88 | - |  |  | SI | Hard palate, fistula	 |
| Q89 | - |  |  | SI | Soft palate, length	 |
| Q90 | - |  |  | SI | Soft palate morphology, intact	 |
| Q91 | - |  |  | SI | Soft palate morphology, cleft	 |
| Q92 | - |  |  | SI | Soft palate morphology, subm. cleft	 |
| Q93 | - |  |  | SI | Soft palate, scar	 |
| Q94 | - |  |  | SI | Soft palate, flap	 |
| Q95 | - |  |  | SI | Soft palate, mobility	 |
| Q96 | - |  |  | SI | Soft palate, uvula	 |
| Q97 | - |  |  | SI | Pharyngeal wall	 |
| Q98 | - |  |  | SI | Side	 |
| Q99 | - |  |  | SI | Right lateral	 |
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