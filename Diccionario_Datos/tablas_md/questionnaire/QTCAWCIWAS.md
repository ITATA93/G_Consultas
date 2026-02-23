# questionnaire.QTCAWCIWAS

> Clinical Institute Withdrawal Assessment for Alcohol, Revised (CIWA-Ar)

**Schema:** questionnaire
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Institute Withdrawal Assessment for Alcohol, Revised (CIWA-Ar)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Ask 'Do you feel sick to your stomach? Have you vo... |
| Q02 | varchar |  |  | SI | Nausea / Vomiting |
| Q03 | varchar |  |  | SI | Arms extended and fingers spread apart |
| Q04 | varchar |  |  | SI | Tremor |
| Q05 | varchar |  |  | SI | Paroxysmal sweats - Observe |
| Q06 | varchar |  |  | SI | Ask 'Does your head feel different? Does it feel l... |
| Q07 | varchar |  |  | SI | Headache / fullness in head |
| Q08 | varchar |  |  | SI | Ask 'What day is this? Where are you? Who am I? |
| Q09 | varchar |  |  | SI | Orientation / clouding of sensorium |
| Q10 | varchar |  |  | SI | Ask, 'Do you feel nervous?' |
| Q11 | varchar |  |  | SI | Anxiety |
| Q12 | varchar |  |  | SI | Agitation |
| Q13 | varchar |  |  | SI | Ask 'Does the light appear to be too bright? Is it... |
| Q14 | varchar |  |  | SI | Visual disturbances |
| Q15 | varchar |  |  | SI | Ask, 'Have you any itching, pins and needles sensa... |
| Q16 | varchar |  |  | SI | Tactile disturbances |
| Q17 | varchar |  |  | SI | Auditory disturbances |
| Q18 | varchar |  |  | SI | CIWA-Ar score |
| Q19 | varchar |  |  | SI | Interpretation (Withdrawal severity) |
| Q20 | varchar |  |  | SI | 0 – 9 |
| Q21 | varchar |  |  | SI | Absent or minimal |
| Q22 | varchar |  |  | SI | 10 – 15 |
| Q23 | varchar |  |  | SI | Mild |
| Q24 | varchar |  |  | SI | 16 – 20 |
| Q25 | varchar |  |  | SI | Moderate |
| Q26 | varchar |  |  | SI | 21 – 67 |
| Q27 | varchar |  |  | SI | Severe |
| Q28 | varchar |  |  | SI | 0 – 9: Absent or minimal |
| Q29 | varchar |  |  | SI | 10 – 15: Mild |
| Q30 | varchar |  |  | SI | 16 – 20: Moderate |
| Q31 | varchar |  |  | SI | 21 – 67: Severe |
| Q32 | varchar |  |  | SI | The CIWA-Ar is a shortened version of a previous 1... |
| Q33 | varchar |  |  | SI | This program to improve recognition and treatment ... |
| Q34 | varchar |  |  | SI | Symptom |
| Q35 | varchar |  |  | SI | Nausea / vomiting |
| Q36 | varchar |  |  | SI | Tremor |
| Q37 | varchar |  |  | SI | Paroxysmal sweats |
| Q38 | varchar |  |  | SI | Headache / sensation of fullness in head |
| Q39 | varchar |  |  | SI | Orientation / clouding of sensorium |
| Q40 | varchar |  |  | SI | Anxiety |
| Q41 | varchar |  |  | SI | Agitation |
| Q42 | varchar |  |  | SI | Visual disturbances |
| Q43 | varchar |  |  | SI | Tactile disturbances |
| Q44 | varchar |  |  | SI | Auditory disturbances |
| Q45 | varchar |  |  | SI | Possible questions to accompany evaluation |
| Q46 | varchar |  |  | SI | Do you feel sick to your stomach? Have you vomited... |
| Q47 | varchar |  |  | SI | n/a |
| Q48 | varchar |  |  | SI | n/a |
| Q49 | varchar |  |  | SI | Does your head feel different? Does it feel like t... |
| Q50 | varchar |  |  | SI | Questions about current date and time, recognition... |
| Q51 | varchar |  |  | SI | Are you feeling anxious? Does something worry you? |
| Q52 | varchar |  |  | SI | n/a |
| Q53 | varchar |  |  | SI | Does the light appear to be too bright? Is its col... |
| Q54 | varchar |  |  | SI | Have you any itching, pins and needles sensations,... |
| Q55 | varchar |  |  | SI | Are you more aware of sounds around you? Are they ... |
| Q56 | varchar |  |  | SI | Other information |
| Q57 | varchar |  |  | SI | Assessor to ask about symptom frequency |
| Q58 | varchar |  |  | SI | Observation of tremor state, in relaxed position a... |
| Q59 | varchar |  |  | SI | Observation of sweating degree, localization and t... |
| Q60 | varchar |  |  | SI | Headache severity should be accounted for |
| Q61 | varchar |  |  | SI | Evaluation of orientation degree |
| Q62 | varchar |  |  | SI | Evaluation of general degree of nervousness and th... |
| Q63 | varchar |  |  | SI | Observation of agitation degree |
| Q64 | varchar |  |  | SI | Checks for visual or hallucinatory events |
| Q65 | varchar |  |  | SI | Checks for abnormal tactile sensations |
| Q66 | varchar |  |  | SI | Evaluation of auditory sensations |
| Q67 | date |  |  | SI | Date |
| Q68 | time |  |  | SI | Time |
| Q69 | varchar |  |  | SI | Ask, 'Are you more aware of sounds around you? Are... |
| Q70 | varchar |  |  | SI | Generic description label1 |
| Q71 | varchar |  |  | SI | Generic description label2 |
| Q72 | varchar |  |  | SI | Generic description label3 |
| Q73 | varchar |  |  | SI | Generic description label4 |
| Q74 | varchar |  |  | SI | Generic description label5 |
| Q75 | varchar |  |  | SI | The Clinical Institute Withdrawal Assessment for A... |
| Q76 | varchar |  |  | SI | Shaw JM, Kolesar GS, Sellers EM, Kaplan HL, Sandor... |
| Q77 | varchar |  |  | SI | Sullivan JT, Sykora K, Schneiderman J, Naranjo CA,... |
| Q78 | varchar |  |  | SI | Vital signs observation chart is required when com... |
| Q79 | varchar |  |  | SI | Heart rate |
| Q79ObsDR | varchar |  | FK | SI | Heart rate DR |
| Q80 | varchar |  |  | SI | Respirations |
| Q80ObsDR | varchar |  | FK | SI | Respirations DR |
| Q81 | varchar |  |  | SI | Saturation |
| Q81ObsDR | varchar |  | FK | SI | Saturation DR |
| Q82 | varchar |  |  | SI | Systolic |
| Q82ObsDR | varchar |  | FK | SI | Systolic DR |
| Q83 | varchar |  |  | SI | Diastolic |
| Q83ObsDR | varchar |  | FK | SI | Diastolic DR |
| Q84 | varchar |  |  | SI | Breath alcohol content |
| Q84ObsDR | varchar |  | FK | SI | Breath alcohol content DR |
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