# SQLUser.PAC_PatientType

**Schema:** SQLUser
**Columnas:** 174
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PTYPE_RowId | bigint | PK |  | NO | - |
| PTYPE_AvailableOnDataEntry | varchar |  |  | SI | List of PTYPEAvailable On Data Entry |
| PTYPE_AvailablePatientEpisode | varchar |  |  | SI | [DEPRECATED]Replaced by PTYPEAvailableOnDataEntry ... |
| PTYPE_Code | varchar |  |  | NO | Code |
| PTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PTYPE_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| PTYPE_Consent | varchar |  |  | SI | Consent |
| PTYPE_CreatedDate | date |  |  | SI | Created Date |
| PTYPE_CreatedTime | time |  |  | SI | Created Time |
| PTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PTYPE_DateFrom | date |  |  | SI | DateFrom |
| PTYPE_DateTo | date |  |  | SI | DateTo |
| PTYPE_Desc | varchar |  |  | NO | Description |
| PTYPE_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| PTYPE_Owner | varchar |  |  | SI | Owner |
| PTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| PTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| PTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Time of examination |
| Q03 | - |  |  | SI | 1. Face |
| Q04 | - |  |  | SI | Symmetry |
| Q05 | - |  |  | SI | Tics |
| Q06 | - |  |  | SI | Ptosis |
| Q07 | - |  |  | SI | 2. Lips |
| Q08 | - |  |  | SI | Symmetry |
| Q09 | - |  |  | SI | Spread |
| Q10 | - |  |  | SI | Pucker |
| Q100 | - |  |  | SI | Tonsils |
| Q101 | - |  |  | SI | 7. Tongue |
| Q102 | - |  |  | SI | by 3 repetitions of a motorically complex word |
| Q103 | - |  |  | SI | eg. bubblegum, pickety, pattycake, kittycat, |
| Q104 | - |  |  | SI | buttercup, topcat |
| Q105 | - |  |  | SI | 4. Clinician judgment of voice quality in speech |
| Q106 | - |  |  | SI | 2. Take a deep breath and release slowly |
| Q107 | - |  |  | SI | 3. Count to 20 (breaths) |
| Q108 | - |  |  | SI | 4. Breathing pattern |
| Q109 | - |  |  | SI | 5. Mouth breathing? |
| Q11 | - |  |  | SI | Seal |
| Q110 | - |  |  | SI | Other observations |
| Q111 | - |  |  | SI | A. Structures |
| Q112 | - |  |  | SI | B. Diadochokinetic Rates |
| Q113 | - |  |  | SI | C. Phonation |
| Q114 | - |  |  | SI | D. Respiration |
| Q115 | - |  |  | SI | E. Reflexive |
| Q116 | - |  |  | SI | F. Other Observations |
| Q12 | - |  |  | SI | Bite upper lip |
| Q13 | - |  |  | SI | Bite lower lip |
| Q14 | - |  |  | SI | 3. Teeth and Mandible |
| Q15 | - |  |  | SI | Type of occlucsion |
| Q16 | - |  |  | SI | Missing teeth |
| Q17 | - |  |  | SI | Condition of teeth |
| Q18 | - |  |  | SI | Mandible |
| Q19 | - |  |  | SI | Lateralisation |
| Q20 | - |  |  | SI | Open / close |
| Q21 | - |  |  | SI | Produce /f/ |
| Q22 | - |  |  | SI | Produce /v/ |
| Q23 | - |  |  | SI | Prosthesis |
| Q24 | - |  |  | SI | If prosthesis present, describe: |
| Q25 | - |  |  | SI | Teeth and mandible comments |
| Q26 | - |  |  | SI | 4. Hard Palate |
| Q27 | - |  |  | SI | Colour |
| Q28 | - |  |  | SI | Vault |
| Q29 | - |  |  | SI | Rugae |
| Q30 | - |  |  | SI | 5. Soft Palate |
| Q31 | - |  |  | SI | Colour |
| Q32 | - |  |  | SI | Uvula |
| Q33 | - |  |  | SI | Elevation 'ah |
| Q34 | - |  |  | SI | Resonance 'Buy baby a bib.' 'Kate eats cake' 'Mama... |
| Q35 | - |  |  | SI | 6. Tonsils |
| Q36 | - |  |  | SI | Appearance |
| Q37 | - |  |  | SI | At rest |
| Q38 | - |  |  | SI | Protrude |
| Q39 | - |  |  | SI | Retract |
| Q40 | - |  |  | SI | Lateralise - R |
| Q41 | - |  |  | SI | Lateralise - L |
| Q42 | - |  |  | SI | Elevate lip |
| Q43 | - |  |  | SI | Lower tip |
| Q44 | - |  |  | SI | Frenulum |
| Q45 | - |  |  | SI | Tongue 'clicks |
| Q46 | - |  |  | SI | Strength |
| Q47 | - |  |  | SI | Size |
| Q48 | - |  |  | SI | Number of seconds required for 20 repetitions |
| Q49 | - |  |  | SI | Puh |
| Q50 | - |  |  | SI | Tuh |
| Q51 | - |  |  | SI | Kuh |
| Q52 | - |  |  | SI | Fuh |
| Q53 | - |  |  | SI | Luh |
| Q54 | - |  |  | SI | Number of seconds required for 15 repetitions |
| Q55 | - |  |  | SI | Puh Tuh |
| Q56 | - |  |  | SI | Puh Kuh |
| Q57 | - |  |  | SI | Tuh Kuh |
| Q58 | - |  |  | SI | Number of seconds required for 10 repetitions |
| Q59 | - |  |  | SI | Puh Tuh Kuh |
| Q60 | - |  |  | SI | If patient cannot produce PuhTuhKuh after training... |
| Q61 | - |  |  | SI | 1. Time of approximation |
| Q62 | - |  |  | SI | /a/ (seconds) |
| Q63 | - |  |  | SI | /f/ (seconds) |
| Q64 | - |  |  | SI | 2. Volume (Count 1 - 5) |
| Q65 | - |  |  | SI | Whisper |
| Q66 | - |  |  | SI | Whisper comment |
| Q67 | - |  |  | SI | Soft |
| Q68 | - |  |  | SI | Soft comment |
| Q69 | - |  |  | SI | Normal |
| Q70 | - |  |  | SI | Normal comment |
| Q71 | - |  |  | SI | Loud |
| Q72 | - |  |  | SI | Loud comment |
| Q73 | - |  |  | SI | Change soft to loud |
| Q74 | - |  |  | SI | Change soft to loud comment |
| Q75 | - |  |  | SI | 3. Pitch (Count 1 - 5) |
| Q76 | - |  |  | SI | Low |
| Q77 | - |  |  | SI | Low comment |
| Q78 | - |  |  | SI | Modal |
| Q79 | - |  |  | SI | Modal commment |
| Q80 | - |  |  | SI | Falsetto |
| Q81 | - |  |  | SI | Falsetto comment |
| Q82 | - |  |  | SI | Glottal fry |
| Q83 | - |  |  | SI | Glottal fry comment |
| Q84 | - |  |  | SI | Change low to high |
| Q85 | - |  |  | SI | Change low to high comment |
| Q86 | - |  |  | SI | 4. Clinician judgment of voice quality in speech |
| Q87 | - |  |  | SI | 1. Nasal cavity : |
| Q88 | - |  |  | SI | Inhale and exhale through |
| Q89 | - |  |  | SI | Nasal cavity |
| Q90 | - |  |  | SI | Nasal cavity comment |
| Q91 | - |  |  | SI | Oral cavity |
| Q92 | - |  |  | SI | Oral cavity comment |
| Q93 | - |  |  | SI | 2. Take a deep breath and release slowly |
| Q94 | - |  |  | SI | 3. Count to 20 (breaths) |
| Q95 | - |  |  | SI | 4. Breathing pattern |
| Q96 | - |  |  | SI | 5. Mouth breathing? |
| Q97 | - |  |  | SI | Drool or dribble at corners of mouth |
| Q98 | - |  |  | SI | Drool or dribble at corners of mouth comment |
| Q99 | - |  |  | SI | Other observations |
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