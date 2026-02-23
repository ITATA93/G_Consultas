# questionnaire.QTCPESMA

> Physical Examination for Sport Medicine Assessment

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physical Examination for Sport Medicine Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Trophism |
| Q02 | varchar |  |  | SI | Weight (kg) |
| Q02ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q03 | varchar |  |  | SI | Height (cm) |
| Q03ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q04 | varchar |  |  | SI | Locomotor system |
| Q05 | varchar |  |  | SI | Cardio - circulatory system |
| Q06 | varchar |  |  | SI | Peripheral pulse (bpm) |
| Q06ObsDR | varchar |  | FK | SI | Peripheral pulse (bpm) DR |
| Q07 | varchar |  |  | SI | Resting systolic blood pressure (mmHg) |
| Q07ObsDR | varchar |  | FK | SI | Resting systolic blood pressure (mmHg) DR |
| Q08 | varchar |  |  | SI | Resting diastolic blood pressure (mmHg) |
| Q08ObsDR | varchar |  | FK | SI | Resting diastolic blood pressure (mmHg) DR |
| Q09 | varchar |  |  | SI | Abdomen and genital organs |
| Q10 | varchar |  |  | SI | Limbs |
| Q11 | numeric |  |  | SI | Natural right eye visual acuity |
| Q12 | varchar |  |  | SI | /10 |
| Q13 | numeric |  |  | SI | Natural left eye visual acuity |
| Q14 | varchar |  |  | SI | /10 |
| Q15 | numeric |  |  | SI | Corrected right eye visual acuity |
| Q16 | varchar |  |  | SI | /10 |
| Q17 | numeric |  |  | SI | Corrected left eye visual acuity |
| Q18 | varchar |  |  | SI | /10 |
| Q19 | varchar |  |  | SI | Colour blindness |
| Q20 | varchar |  |  | SI | Hearing |
| Q21 | varchar |  |  | SI | Conclusions of physical exam |
| Q22 | numeric |  |  | SI | Average heart rate (bpm) |
| Q23 | numeric |  |  | SI | PR interval |
| Q24 | numeric |  |  | SI | QT interval |
| Q25 | numeric |  |  | SI | Average heart rate (bpm) |
| Q26 | numeric |  |  | SI | PR interval |
| Q27 | numeric |  |  | SI | QT interval |
| Q28 | varchar |  |  | SI | Report |
| Q29 | varchar |  |  | SI | Appearance |
| Q30 | varchar |  |  | SI | Colour |
| Q31 | varchar |  |  | SI | Density |
| Q32 | varchar |  |  | SI | Reaction |
| Q33 | varchar |  |  | SI | Report |
| Q34 | numeric |  |  | SI | Vital capacity VC (L) |
| Q35 | numeric |  |  | SI | Maximum exhaled volume per second MEVS (L) |
| Q36 | numeric |  |  | SI | Tiffeneau index MEVS/VC % |
| Q37 | numeric |  |  | SI | Maximum voluntary ventilation MVV (L/min) |
| Q38 | varchar |  |  | SI | Conclusions |
| Q39 | varchar |  |  | SI | Electroencephalogram |
| Q40 | varchar |  |  | SI | Neurological examination |
| Q41 | varchar |  |  | SI | ENT examination |
| Q42 | varchar |  |  | SI | Audiometry |
| Q43 | varchar |  |  | SI | Eye examination |
| Q44 | varchar |  |  | SI | Other exams |
| Q45 | varchar |  |  | SI | Judgement |
| Q46 | varchar |  |  | SI | At the time of the examination, the athlete has no... |
| Q47 | varchar |  |  | SI | At the time of the visit, the athlete has previous... |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
| Q50 | varchar |  |  | SI | Sport for which the visit was requested |
| Q51 | varchar |  |  | SI | Other sports practised |
| Q52 | varchar |  |  | SI | Family history |
| Q53 | varchar |  |  | SI | Physiological anamnesis |
| Q54 | date |  |  | SI | Menarche |
| Q55 | date |  |  | SI | Last menstruation date |
| Q56 | varchar |  |  | SI | Smoke |
| Q57 | varchar |  |  | SI | Alcohol |
| Q58 | varchar |  |  | SI | Caffeine |
| Q59 | varchar |  |  | SI | Drugs |
| Q60 | varchar |  |  | SI | Supplements |
| Q61 | varchar |  |  | SI | Disease suffered |
| Q62 | varchar |  |  | SI | Surgical interventions |
| Q63 | varchar |  |  | SI | Injuries |
| Q64 | varchar |  |  | SI | Symptomatology |
| Q65 | varchar |  |  | SI | Examination |
| Q66 | numeric |  |  | SI | Normal vital capacity VC (L) |
| Q67 | numeric |  |  | SI | Maximum exhaled volume per second MEVS (L/sec) |
| Q68 | numeric |  |  | SI | Normal maximum exhaled volume per second MEVS (L/s... |
| Q69 | numeric |  |  | SI | Normal tiffeneau index MEVS/VC % |
| Q70 | numeric |  |  | SI | Normal maximum voluntary ventilation MVV (L/min) |
| Q73 | varchar |  |  | SI | Sport |
| Q74 | varchar |  |  | SI | For the period |
| Q75 | varchar |  |  | SI | The athlete declares, assuming all civil or crimin... |
| Q76 | varchar |  |  | SI | The athlete gives informed consent for the require... |
| Q77 | varchar |  |  | SI | Others |
| Q78 | varchar |  |  | SI | Notes |
| Q79 | varchar |  |  | SI | Respiratory system |
| Q80 | varchar |  |  | SI | Report |
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