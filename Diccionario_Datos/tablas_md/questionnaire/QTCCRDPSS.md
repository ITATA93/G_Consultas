# questionnaire.QTCCRDPSS

> Clinician-Rated Dimensions of Psychosis Symptom Severity

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinician-Rated Dimensions of Psychosis Symptom Severity

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Based on all the information you have on the indiv... |
| Q02 | varchar |  |  | SI | Hallucinations |
| Q03 | varchar |  |  | SI | Delusions |
| Q04 | varchar |  |  | SI | Disorganized speech |
| Q05 | varchar |  |  | SI | Abnormal psycho-motor behaviour |
| Q06 | varchar |  |  | SI | Negative symptoms (restricted emotional expression... |
| Q07 | varchar |  |  | SI | Impaired cognition |
| Q08 | varchar |  |  | SI | Depression |
| Q09 | varchar |  |  | SI | Mania |
| Q10 | varchar |  |  | SI | The Clinician-Rated Dimensions of Psychosis Sympto... |
| Q11 | varchar |  |  | SI | disorganized speech, abnormal psychomotor behaviou... |
| Q12 | varchar |  |  | SI | The severity of these symptoms can predict importa... |
| Q13 | varchar |  |  | SI | The measure is intended to capture meaningful vari... |
| Q14 | varchar |  |  | SI | The measure is completed by the clinician at the t... |
| Q15 | varchar |  |  | SI | Each item on the measure is rated on a 5-point sca... |
| Q16 | varchar |  |  | SI | The clinician may review all of the individual’s a... |
| Q17 | varchar |  |  | SI | The clinician then indicates the score for each it... |
| Q18 | varchar |  |  | SI | The response on each item should be interpreted in... |
| Q19 | varchar |  |  | SI | To track changes in the individual’s symptom sever... |
| Q20 | varchar |  |  | SI | Consistently high scores on a particular domain ma... |
| Q21 | varchar |  |  | SI | Clinical judgment should guide decision making. |
| Q22 | varchar |  |  | SI | Hallucinations Score	 |
| Q23 | varchar |  |  | SI | Delusions Score	 |
| Q24 | varchar |  |  | SI | Disorganized speech Score	 |
| Q25 | varchar |  |  | SI | Abnormal psycho-motor behaviour Score	 |
| Q26 | varchar |  |  | SI | Negative symptoms Score	 |
| Q27 | varchar |  |  | SI | Impaired cognition Score	 |
| Q28 | varchar |  |  | SI | Depression Score |
| Q29 | varchar |  |  | SI | Mania Score |
| Q30 | varchar |  |  | SI | 0   -      None |
| Q31 | varchar |  |  | SI | 1   -      Equivocal |
| Q32 | varchar |  |  | SI | 2   -      Present but Mild  |
| Q33 | varchar |  |  | SI | 3   -      Present and moderate |
| Q34 | varchar |  |  | SI | 4   -      Present and severe |
| Q35 | varchar |  |  | SI | The Clinician-Rated Dimensions of Psychosis Sympto... |
| Q36 | varchar |  |  | SI | Score |
| Q37 | varchar |  |  | SI | Classification |
| Q38 | varchar |  |  | SI | Score |
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