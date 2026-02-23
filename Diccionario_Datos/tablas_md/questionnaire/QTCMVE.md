# questionnaire.QTCMVE

> Management of Voice Evaluation

**Schema:** questionnaire
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Management of Voice Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of examination	 |
| Q02 | varchar |  |  | SI | Residence	 |
| Q03 | varchar |  |  | SI | Father's job	 |
| Q04 | varchar |  |  | SI | Mother's job	 |
| Q05 | varchar |  |  | SI | Consanguinity	 |
| Q06 | varchar |  |  | SI | Similar condition	 |
| Q07 | varchar |  |  | SI | Education / occupation	 |
| Q08 | varchar |  |  | SI | Complaints and Analysis of Symptoms	 |
| Q09 | varchar |  |  | SI | Duration |
| Q10 | varchar |  |  | SI | Onset |
| Q11 | varchar |  |  | SI | Course |
| Q12 | varchar |  |  | SI | Phonasthenic symptoms (vocal fatigue)	 |
| Q13 | varchar |  |  | SI | Search for etiological factors	 |
| Q14 | varchar |  |  | SI | Type of job	 |
| Q15 | varchar |  |  | SI | Vocal demand	 |
| Q16 | numeric |  |  | SI | Number of hours exposure	 |
| Q17 | varchar |  |  | SI | Job environment	 |
| Q18 | varchar |  |  | SI | Level of ambient noise	 |
| Q19 | varchar |  |  | SI | Reverberation time	 |
| Q20 | varchar |  |  | SI | Relative humidity	 |
| Q21 | varchar |  |  | SI | Temperature	 |
| Q22 | varchar |  |  | SI | Irritants: Dust	 |
| Q23 | varchar |  |  | SI | Amount	 |
| Q24 | varchar |  |  | SI | Particle size	 |
| Q25 | varchar |  |  | SI | Irritants: Fumes	 |
| Q26 | varchar |  |  | SI | Type	 |
| Q27 | varchar |  |  | SI | Concentration	 |
| Q28 | varchar |  |  | SI | Temperament	 |
| Q29 | varchar |  |  | SI | Emotional dtress	 |
| Q30 | varchar |  |  | SI | Frequent and/or repeated Upper Respiratory Tract (... |
| Q31 | varchar |  |  | SI | Allergic tendencies	 |
| Q32 | varchar |  |  | SI | Chronic cough and chest diseases	 |
| Q33 | varchar |  |  | SI | Dyspnea	 |
| Q34 | varchar |  |  | SI | Breathing	 |
| Q35 | varchar |  |  | SI | Chewing and swallowing	 |
| Q36 | varchar |  |  | SI | Hyper-acidity and reflux	 |
| Q37 | varchar |  |  | SI | Surgical intervention	 |
| Q38 | varchar |  |  | SI | Factors that might influence therapy	 |
| Q39 | varchar |  |  | SI | Hearing |
| Q40 | varchar |  |  | SI | Musicality	 |
| Q41 | varchar |  |  | SI | Audiotory Perceptual Assessment (APA)	 |
| Q42 | varchar |  |  | SI | Overall grade	 |
| Q43 | varchar |  |  | SI | Character	 |
| Q44 | varchar |  |  | SI | Pitch	 |
| Q45 | varchar |  |  | SI | Loudness	 |
| Q46 | varchar |  |  | SI | ENT Examination	 |
| Q47 | varchar |  |  | SI | Oral cavity	 |
| Q48 | varchar |  |  | SI | Pharynx  |
| Q49 | varchar |  |  | SI | Tonsils	 |
| Q50 | varchar |  |  | SI | Post-nasal discharge	 |
| Q51 | varchar |  |  | SI | Nasal cavity 	 |
| Q52 | varchar |  |  | SI | Ears |
| Q53 | varchar |  |  | SI | Type of breathing	 |
| Q54 | varchar |  |  | SI | Laryngeal Examination	 |
| Q55 | varchar |  |  | SI | External laryngeal examination	 |
| Q56 | varchar |  |  | SI | Normal configuration	 |
| Q57 | varchar |  |  | SI | Fractures	 |
| Q58 | varchar |  |  | SI | Fractures, site	 |
| Q59 | varchar |  |  | SI | Fractures, type	 |
| Q60 | varchar |  |  | SI | Other abnormalities	 |
| Q61 | varchar |  |  | SI | Laryngeal click	 |
| Q62 | varchar |  |  | SI | Laryngeal position	 |
| Q63 | varchar |  |  | SI | Cervical veins	 |
| Q64 | varchar |  |  | SI | Neck scars, type	 |
| Q65 | varchar |  |  | SI | Neck scars, site	 |
| Q66 | varchar |  |  | SI | Elementary visual impression and indirect laryngos... |
| Q67 | varchar |  |  | SI | Items to be noticed	 |
| Q68 | varchar |  |  | SI | Muous membrane  |
| Q69 | varchar |  |  | SI | Vocal folds' configuration  |
| Q70 | varchar |  |  | SI | Vocal folds' movement:  |
| Q71 | varchar |  |  | SI | Ventricular folds |
| Q72 | varchar |  |  | SI | Visual impression	 |
| Q73 | varchar |  |  | SI | Structures to be examined	 |
| Q74 | varchar |  |  | SI | 1. Vollecula |
| Q75 | varchar |  |  | SI | 2. Epiglottis |
| Q76 | varchar |  |  | SI | 3. Vocal fold |
| Q77 | varchar |  |  | SI | 4. Pyrforn fossavaev |
| Q78 | varchar |  |  | SI | 5. Arytenoids |
| Q79 | varchar |  |  | SI | 6. Internal tensoids |
| Q80 | varchar |  |  | SI | 7. Anterior commisure |
| Q81 | varchar |  |  | SI | 8. Subglottis |
| Q82 | varchar |  |  | SI | 9. Ventricular folds |
| Q83 | varchar |  |  | SI | 10. Ventricles |
| Q84 | varchar |  |  | SI | 11. Aryepiglottic  |
| Q85 | varchar |  |  | SI | 12. Post Cricoid region |
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