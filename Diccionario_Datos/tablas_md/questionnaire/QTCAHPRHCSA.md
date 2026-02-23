# questionnaire.QTCAHPRHCSA

> Cervical Spine Assessment

**Schema:** questionnaire
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cervical Spine Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Occupation |
| Q02 | varchar |  |  | SI | Work : Mechanical Stress |
| Q03 | varchar |  |  | SI | Other |
| Q04 | varchar |  |  | SI | Leisure : Mechanical Stress |
| Q05 | varchar |  |  | SI | Other |
| Q06 | varchar |  |  | SI | Pain Location |
| Q06A | varchar |  |  | SI | Mark the Pain Location |
| Q07 | varchar |  |  | SI | VAS Score |
| Q07A | varchar |  |  | SI | (0 No pain at all - 10 pain as bad as it can be) |
| Q08 | varchar |  |  | SI | Is Your Pain |
| Q09 | varchar |  |  | SI | Pain Description |
| Q10 | date |  |  | SI | Pain Present Since |
| Q100 | varchar |  |  | SI | Observation |
| Q101 | varchar |  |  | SI | Tenderness on Palpation |
| Q102 | varchar |  |  | SI | Neurological |
| Q103 | varchar |  |  | SI | Static Tests |
| Q104 | varchar |  |  | SI | Special Test |
| Q105 | varchar |  |  | SI | Assessment |
| Q106 | varchar |  |  | SI | Treatment Plan |
| Q107 | varchar |  |  | SI | Treatment |
| Q11 | varchar |  |  | SI | Pain Progress |
| Q12 | varchar |  |  | SI | Current Pain History |
| Q13 | varchar |  |  | SI | Commenced as a Result of |
| Q14 | varchar |  |  | SI | Other |
| Q15 | varchar |  |  | SI | Symptoms At Onset |
| Q16 | varchar |  |  | SI | Constant Symptom |
| Q17 | varchar |  |  | SI | Intermittent Symptom |
| Q18 | varchar |  |  | SI | Pain Pattern Worse With the Following |
| Q19 | varchar |  |  | SI | Other |
| Q20 | varchar |  |  | SI | Pain Pattern Better With the Following |
| Q21 | varchar |  |  | SI | Other |
| Q22 | varchar |  |  | SI | Gait |
| Q23 | varchar |  |  | SI | Disturbed Sleep |
| Q24 | varchar |  |  | SI | Sleeping Postures |
| Q25 | varchar |  |  | SI | Surface |
| Q26 | varchar |  |  | SI | Previous Episodes |
| Q27 | date |  |  | SI | Year of First Episode |
| Q28 | varchar |  |  | SI | Night Pain |
| Q29 | varchar |  |  | SI | General Health |
| Q30 | varchar |  |  | SI | Medical History |
| Q31 | varchar |  |  | SI | Other |
| Q32 | varchar |  |  | SI | Medications |
| Q33 | varchar |  |  | SI | Other |
| Q34 | varchar |  |  | SI | Bladder |
| Q35 | varchar |  |  | SI | Previous Surgery |
| Q36 | varchar |  |  | SI | Comment |
| Q37 | varchar |  |  | SI | Previous Physical Therapy Treatment |
| Q38 | varchar |  |  | SI | X-ray  |
| Q39 | varchar |  |  | SI | Report |
| Q40 | varchar |  |  | SI | Unexplained Weight Loss |
| Q41 | varchar |  |  | SI | Patient Goals |
| Q42 | varchar |  |  | SI | SECTION 1 - Pain Intensity |
| Q43 | varchar |  |  | SI | SECTION 2 - Personal Care |
| Q43A | varchar |  |  | SI | (Washing, Dressing, etc.) |
| Q44 | varchar |  |  | SI | SECTION 3 - Lifting   |
| Q45 | varchar |  |  | SI | SECTION 4 - Reading |
| Q46 | varchar |  |  | SI | SECTION 5 - Headaches |
| Q47 | varchar |  |  | SI | SECTION 6 - Concentration |
| Q48 | varchar |  |  | SI | SECTION 7 - Work |
| Q49 | varchar |  |  | SI | SECTION 8 - Driving |
| Q50 | varchar |  |  | SI | SECTION 9 - Sleeping |
| Q51 | varchar |  |  | SI | SECTION 10 - Recreation |
| Q53 | varchar |  |  | SI | Sitting |
| Q54 | varchar |  |  | SI | Standing |
| Q55 | varchar |  |  | SI | Protruded Head |
| Q56 | varchar |  |  | SI | Thoracic Kyphosis |
| Q57 | varchar |  |  | SI | Correction of Posture |
| Q59 | varchar |  |  | SI | A. Spinous processes of Cervical Vertebrae C5 |
| Q60 | varchar |  |  | SI | B. Spinous processes of Cervical Vertebrae C6 |
| Q61 | varchar |  |  | SI | C. Spinous processes of Cervical Vertebrae C7 |
| Q62 | varchar |  |  | SI | D. Paraspinous muscles |
| Q63 | varchar |  |  | SI | Other |
| Q72 | varchar |  |  | SI | Protrusion |
| Q73 | varchar |  |  | SI | Flexion |
| Q74 | varchar |  |  | SI | Retraction |
| Q75 | varchar |  |  | SI | Extension Sitting |
| Q76 | varchar |  |  | SI | Extension Prone |
| Q77 | varchar |  |  | SI | Extension Supine |
| Q78 | varchar |  |  | SI | Special Test |
| Q80 | varchar |  |  | SI | PT Diagnosis |
| Q81 | varchar |  |  | SI | Derangement Pain Location |
| Q82 | varchar |  |  | SI | Other Diagnosis |
| Q83 | varchar |  |  | SI | Problems List |
| Q85 | varchar |  |  | SI | Rehabilitation Potential |
| Q86 | varchar |  |  | SI | Family / patient involved in |
| Q86A | varchar |  |  | SI | and verbalized understanding of goals |
| Q87 | varchar |  |  | SI | Comment |
| Q88 | varchar |  |  | SI | Education |
| Q89 | varchar |  |  | SI | Short Term Goals |
| Q90 | varchar |  |  | SI | Long Term Goals |
| Q92 | numeric |  |  | SI | Number of Treatments per week |
| Q93 | numeric |  |  | SI | Number of weeks |
| Q94 | varchar |  |  | SI | Re Evaluation |
| Q95 | varchar |  |  | SI | Mechanical Therapy |
| Q96 | varchar |  |  | SI | Therapy Type |
| Q98 | varchar |  |  | SI | Others |
| Q99 | varchar |  |  | SI | Comment |
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