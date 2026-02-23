# SQLUser.PAC_LegalStatus

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LEGALST_RowId | bigint | PK |  | NO | - |
| LEGALST_Code | varchar |  |  | NO | Code |
| LEGALST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LEGALST_CreatedDate | date |  |  | SI | Created Date |
| LEGALST_CreatedTime | time |  |  | SI | Created Time |
| LEGALST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LEGALST_DateFrom | date |  |  | SI | Date From |
| LEGALST_DateTo | date |  |  | SI | Date To |
| LEGALST_Desc | varchar |  |  | NO | Description |
| LEGALST_Owner | varchar |  |  | SI | Owner |
| LEGALST_UpdatedDate | date |  |  | SI | Updated Date |
| LEGALST_UpdatedTime | time |  |  | SI | Updated Time |
| LEGALST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of examination	 |
| Q02 | - |  |  | SI | Residence	 |
| Q03 | - |  |  | SI | Father's job	 |
| Q04 | - |  |  | SI | Mother's job	 |
| Q05 | - |  |  | SI | Consanguinity	 |
| Q06 | - |  |  | SI | Similar condition	 |
| Q07 | - |  |  | SI | Education / occupation	 |
| Q08 | - |  |  | SI | Complaints and Analysis of Symptoms	 |
| Q09 | - |  |  | SI | Duration |
| Q10 | - |  |  | SI | Onset |
| Q11 | - |  |  | SI | Course |
| Q12 | - |  |  | SI | Phonasthenic symptoms (vocal fatigue)	 |
| Q13 | - |  |  | SI | Search for etiological factors	 |
| Q14 | - |  |  | SI | Type of job	 |
| Q15 | - |  |  | SI | Vocal demand	 |
| Q16 | - |  |  | SI | Number of hours exposure	 |
| Q17 | - |  |  | SI | Job environment	 |
| Q18 | - |  |  | SI | Level of ambient noise	 |
| Q19 | - |  |  | SI | Reverberation time	 |
| Q20 | - |  |  | SI | Relative humidity	 |
| Q21 | - |  |  | SI | Temperature	 |
| Q22 | - |  |  | SI | Irritants: Dust	 |
| Q23 | - |  |  | SI | Amount	 |
| Q24 | - |  |  | SI | Particle size	 |
| Q25 | - |  |  | SI | Irritants: Fumes	 |
| Q26 | - |  |  | SI | Type	 |
| Q27 | - |  |  | SI | Concentration	 |
| Q28 | - |  |  | SI | Temperament	 |
| Q29 | - |  |  | SI | Emotional dtress	 |
| Q30 | - |  |  | SI | Frequent and/or repeated Upper Respiratory Tract (... |
| Q31 | - |  |  | SI | Allergic tendencies	 |
| Q32 | - |  |  | SI | Chronic cough and chest diseases	 |
| Q33 | - |  |  | SI | Dyspnea	 |
| Q34 | - |  |  | SI | Breathing	 |
| Q35 | - |  |  | SI | Chewing and swallowing	 |
| Q36 | - |  |  | SI | Hyper-acidity and reflux	 |
| Q37 | - |  |  | SI | Surgical intervention	 |
| Q38 | - |  |  | SI | Factors that might influence therapy	 |
| Q39 | - |  |  | SI | Hearing |
| Q40 | - |  |  | SI | Musicality	 |
| Q41 | - |  |  | SI | Audiotory Perceptual Assessment (APA)	 |
| Q42 | - |  |  | SI | Overall grade	 |
| Q43 | - |  |  | SI | Character	 |
| Q44 | - |  |  | SI | Pitch	 |
| Q45 | - |  |  | SI | Loudness	 |
| Q46 | - |  |  | SI | ENT Examination	 |
| Q47 | - |  |  | SI | Oral cavity	 |
| Q48 | - |  |  | SI | Pharynx |
| Q49 | - |  |  | SI | Tonsils	 |
| Q50 | - |  |  | SI | Post-nasal discharge	 |
| Q51 | - |  |  | SI | Nasal cavity 	 |
| Q52 | - |  |  | SI | Ears |
| Q53 | - |  |  | SI | Type of breathing	 |
| Q54 | - |  |  | SI | Laryngeal Examination	 |
| Q55 | - |  |  | SI | External laryngeal examination	 |
| Q56 | - |  |  | SI | Normal configuration	 |
| Q57 | - |  |  | SI | Fractures	 |
| Q58 | - |  |  | SI | Fractures, site	 |
| Q59 | - |  |  | SI | Fractures, type	 |
| Q60 | - |  |  | SI | Other abnormalities	 |
| Q61 | - |  |  | SI | Laryngeal click	 |
| Q62 | - |  |  | SI | Laryngeal position	 |
| Q63 | - |  |  | SI | Cervical veins	 |
| Q64 | - |  |  | SI | Neck scars, type	 |
| Q65 | - |  |  | SI | Neck scars, site	 |
| Q66 | - |  |  | SI | Elementary visual impression and indirect laryngos... |
| Q67 | - |  |  | SI | Items to be noticed	 |
| Q68 | - |  |  | SI | Muous membrane |
| Q69 | - |  |  | SI | Vocal folds' configuration |
| Q70 | - |  |  | SI | Vocal folds' movement: |
| Q71 | - |  |  | SI | Ventricular folds |
| Q72 | - |  |  | SI | Visual impression	 |
| Q73 | - |  |  | SI | Structures to be examined	 |
| Q74 | - |  |  | SI | 1. Vollecula |
| Q75 | - |  |  | SI | 2. Epiglottis |
| Q76 | - |  |  | SI | 3. Vocal fold |
| Q77 | - |  |  | SI | 4. Pyrforn fossavaev |
| Q78 | - |  |  | SI | 5. Arytenoids |
| Q79 | - |  |  | SI | 6. Internal tensoids |
| Q80 | - |  |  | SI | 7. Anterior commisure |
| Q81 | - |  |  | SI | 8. Subglottis |
| Q82 | - |  |  | SI | 9. Ventricular folds |
| Q83 | - |  |  | SI | 10. Ventricles |
| Q84 | - |  |  | SI | 11. Aryepiglottic |
| Q85 | - |  |  | SI | 12. Post Cricoid region |
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