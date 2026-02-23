# SQLUser.INC_ItmConsumption

**Schema:** SQLUser
**Columnas:** 151
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONS_ParRef | bigint | PK |  | NO | INC_Itm Parent Reference |
| CONS_Amount | double |  |  | SI | Amount |
| CONS_CreatedDate | date |  |  | SI | Created Date |
| CONS_CreatedTime | time |  |  | SI | Created Time |
| CONS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONS_Month | double |  |  | NO | Month |
| CONS_Qty | double |  |  | SI | Qty |
| CONS_RowId | varchar |  |  | NO | - |
| CONS_Type | varchar |  |  | NO | Type |
| CONS_UpdatedDate | date |  |  | SI | Updated Date |
| CONS_UpdatedTime | time |  |  | SI | Updated Time |
| CONS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CONS_Year | double |  |  | NO | Year |
| ChildQ67DR | - |  |  | SI | Child Reference: Sensory Examination |
| Q01 | - |  |  | SI | Occupation |
| Q02 | - |  |  | SI | Work : Mechanical Stress |
| Q03 | - |  |  | SI | Other |
| Q04 | - |  |  | SI | Leisure : Mechanical Stress |
| Q05 | - |  |  | SI | Other |
| Q06 | - |  |  | SI | Pain Location |
| Q06A | - |  |  | SI | Mark the Pain Location |
| Q07 | - |  |  | SI | VAS Score |
| Q07A | - |  |  | SI | (0 No pain at all - 10 pain as bad as it can be) |
| Q08 | - |  |  | SI | Is Your Pain |
| Q09 | - |  |  | SI | Pain Description |
| Q10 | - |  |  | SI | Pain Present Since |
| Q100 | - |  |  | SI | Observation |
| Q101 | - |  |  | SI | Tenderness on Palpation |
| Q102 | - |  |  | SI | Neurological |
| Q103 | - |  |  | SI | Static Tests |
| Q104 | - |  |  | SI | Special Test |
| Q105 | - |  |  | SI | Assessment |
| Q106 | - |  |  | SI | Treatment Plan |
| Q107 | - |  |  | SI | Treatment |
| Q11 | - |  |  | SI | Pain Progress |
| Q12 | - |  |  | SI | Current Pain History |
| Q13 | - |  |  | SI | Commenced as a Result of |
| Q14 | - |  |  | SI | Other |
| Q15 | - |  |  | SI | Symptoms At Onset |
| Q16 | - |  |  | SI | Constant Symptom |
| Q17 | - |  |  | SI | Intermittent Symptom |
| Q18 | - |  |  | SI | Pain Pattern Worse With the Following |
| Q19 | - |  |  | SI | Other |
| Q20 | - |  |  | SI | Pain Pattern Better With the Following |
| Q21 | - |  |  | SI | Other |
| Q22 | - |  |  | SI | Gait |
| Q23 | - |  |  | SI | Disturbed Sleep |
| Q24 | - |  |  | SI | Sleeping Postures |
| Q25 | - |  |  | SI | Surface |
| Q26 | - |  |  | SI | Previous Episodes |
| Q27 | - |  |  | SI | Year of First Episode |
| Q28 | - |  |  | SI | Night Pain |
| Q29 | - |  |  | SI | General Health |
| Q30 | - |  |  | SI | Medical History |
| Q31 | - |  |  | SI | Other |
| Q32 | - |  |  | SI | Medications |
| Q33 | - |  |  | SI | Other |
| Q34 | - |  |  | SI | Bladder |
| Q35 | - |  |  | SI | Previous Surgery |
| Q36 | - |  |  | SI | Comment |
| Q37 | - |  |  | SI | Previous Physical Therapy Treatment |
| Q38 | - |  |  | SI | X-ray |
| Q39 | - |  |  | SI | Report |
| Q40 | - |  |  | SI | Unexplained Weight Loss |
| Q41 | - |  |  | SI | Patient Goals |
| Q42 | - |  |  | SI | SECTION 1 - Pain Intensity |
| Q43 | - |  |  | SI | SECTION 2 - Personal Care |
| Q43A | - |  |  | SI | (Washing, Dressing, etc.) |
| Q44 | - |  |  | SI | SECTION 3 - Lifting |
| Q45 | - |  |  | SI | SECTION 4 - Reading |
| Q46 | - |  |  | SI | SECTION 5 - Headaches |
| Q47 | - |  |  | SI | SECTION 6 - Concentration |
| Q48 | - |  |  | SI | SECTION 7 - Work |
| Q49 | - |  |  | SI | SECTION 8 - Driving |
| Q50 | - |  |  | SI | SECTION 9 - Sleeping |
| Q51 | - |  |  | SI | SECTION 10 - Recreation |
| Q53 | - |  |  | SI | Sitting |
| Q54 | - |  |  | SI | Standing |
| Q55 | - |  |  | SI | Protruded Head |
| Q56 | - |  |  | SI | Thoracic Kyphosis |
| Q57 | - |  |  | SI | Correction of Posture |
| Q59 | - |  |  | SI | A. Spinous processes of Cervical Vertebrae C5 |
| Q60 | - |  |  | SI | B. Spinous processes of Cervical Vertebrae C6 |
| Q61 | - |  |  | SI | C. Spinous processes of Cervical Vertebrae C7 |
| Q62 | - |  |  | SI | D. Paraspinous muscles |
| Q63 | - |  |  | SI | Other |
| Q72 | - |  |  | SI | Protrusion |
| Q73 | - |  |  | SI | Flexion |
| Q74 | - |  |  | SI | Retraction |
| Q75 | - |  |  | SI | Extension Sitting |
| Q76 | - |  |  | SI | Extension Prone |
| Q77 | - |  |  | SI | Extension Supine |
| Q78 | - |  |  | SI | Special Test |
| Q80 | - |  |  | SI | PT Diagnosis |
| Q81 | - |  |  | SI | Derangement Pain Location |
| Q82 | - |  |  | SI | Other Diagnosis |
| Q83 | - |  |  | SI | Problems List |
| Q85 | - |  |  | SI | Rehabilitation Potential |
| Q86 | - |  |  | SI | Family / patient involved in |
| Q86A | - |  |  | SI | and verbalized understanding of goals |
| Q87 | - |  |  | SI | Comment |
| Q88 | - |  |  | SI | Education |
| Q89 | - |  |  | SI | Short Term Goals |
| Q90 | - |  |  | SI | Long Term Goals |
| Q92 | - |  |  | SI | Number of Treatments per week |
| Q93 | - |  |  | SI | Number of weeks |
| Q94 | - |  |  | SI | Re Evaluation |
| Q95 | - |  |  | SI | Mechanical Therapy |
| Q96 | - |  |  | SI | Therapy Type |
| Q98 | - |  |  | SI | Others |
| Q99 | - |  |  | SI | Comment |
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