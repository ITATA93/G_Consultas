# questionnaire.QTCPSSTT

> Pediatric Septic Shock Trigger Tool

**Schema:** questionnaire
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pediatric Septic Shock Trigger Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Condition |
| Q04 | varchar |  |  | SI | High risk condition |
| Q05 | varchar |  |  | SI | Age range |
| Q06 | varchar |  |  | SI | Criteria: |
| Q07 | varchar |  |  | SI | Heart Rate > 205;  |
| Q08 | varchar |  |  | SI | Respiratory Rate: > 60; |
| Q09 | varchar |  |  | SI | Systolic BP: < 60;  |
| Q10 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q11 | varchar |  |  | SI | Criteria: |
| Q12 | varchar |  |  | SI | Heart Rate > 205; |
| Q13 | varchar |  |  | SI | Respiratory Rate: > 60; |
| Q14 | varchar |  |  | SI | Systolic BP: < 70; |
| Q15 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q16 | varchar |  |  | SI | Criteria: |
| Q17 | varchar |  |  | SI | Heart Rate > 190; |
| Q18 | varchar |  |  | SI | Respiratory Rate: > 60; |
| Q19 | varchar |  |  | SI | Systolic BP: < 70; |
| Q20 | varchar |  |  | SI | Temperature: <36 or >38.5 |
| Q21 | varchar |  |  | SI | Criteria: |
| Q22 | varchar |  |  | SI | Heart Rate > 190; |
| Q23 | varchar |  |  | SI | Respiratory Rate: > 40; |
| Q24 | varchar |  |  | SI | Systolic BP: < 70 + (Age in yr x2); |
| Q25 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q26 | varchar |  |  | SI | Criteria: |
| Q27 | varchar |  |  | SI | Heart Rate > 140; |
| Q28 | varchar |  |  | SI | Respiratory Rate: > 40; |
| Q29 | varchar |  |  | SI | Systolic BP: < 70 + (Age in yr x2); |
| Q30 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q31 | varchar |  |  | SI | Criteria: |
| Q32 | varchar |  |  | SI | Heart Rate > 140; |
| Q33 | varchar |  |  | SI | Respiratory Rate: > 34; |
| Q34 | varchar |  |  | SI | Systolic BP: < 70 + (Age in yr x2); |
| Q35 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q36 | varchar |  |  | SI | Criteria:  |
| Q37 | varchar |  |  | SI | Heart Rate > 140; |
| Q38 | varchar |  |  | SI | Respiratory Rate: > 30; |
| Q39 | varchar |  |  | SI | Systolic BP: < 70 + (Age in yr x2); |
| Q40 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q41 | varchar |  |  | SI | Criteria:  |
| Q42 | varchar |  |  | SI | Heart Rate > 100; |
| Q43 | varchar |  |  | SI | Respiratory Rate: > 30; |
| Q44 | varchar |  |  | SI | Systolic BP: < 90; |
| Q45 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q46 | varchar |  |  | SI | Criteria: |
| Q47 | varchar |  |  | SI | Heart Rate > 100; |
| Q48 | varchar |  |  | SI | Respiratory Rate: > 16; |
| Q49 | varchar |  |  | SI | Systolic BP: < 90; |
| Q50 | varchar |  |  | SI | Temperature: <36 or >38 |
| Q51 | varchar |  |  | SI | Temperature abnormal |
| Q52 | varchar |  |  | SI | Hypotension |
| Q53 | varchar |  |  | SI | Tachycardia |
| Q54 | varchar |  |  | SI | Capillary refill abnormal |
| Q55 | varchar |  |  | SI | Capillary refill (central vs. peripheral) |
| Q56 | varchar |  |  | SI | Mental status abnormal |
| Q57 | varchar |  |  | SI | Comment |
| Q58 | varchar |  |  | SI | Pulse abnormal |
| Q59 | varchar |  |  | SI | Pulse characteristics |
| Q60 | varchar |  |  | SI | Skin abnormal |
| Q61 | varchar |  |  | SI | Skin |
| Q62 | varchar |  |  | SI | Conclusion: (Positive or Negative based on the sco... |
| Q63 | varchar |  |  | SI | Patient will be positive if meets 3 or more risk f... |
| Q64 | varchar |  |  | SI | Patient will be positive if meets 2 or more risk f... |
| Q65 | varchar |  |  | SI | Score |
| Q66 | varchar |  |  | SI | Positive Low Risk |
| Q67 | varchar |  |  | SI | Positive High Risk |
| Q68 | varchar |  |  | SI | Negative High Risk |
| Q69 | varchar |  |  | SI | Negative Low Risk |
| Q70 | varchar |  |  | SI | Score |
| Q71 | varchar |  |  | SI | Classification |
| Q72 | varchar |  |  | SI | ≥ 3 |
| Q73 | varchar |  |  | SI | Positive Low Risk |
| Q74 | varchar |  |  | SI | <3 |
| Q75 | varchar |  |  | SI | Negative Low Risk |
| Q76 | varchar |  |  | SI | ≥ 2 |
| Q77 | varchar |  |  | SI | Positive High Risk |
| Q78 | varchar |  |  | SI | <2 |
| Q79 | varchar |  |  | SI | Negative High Risk |
| Q80 | varchar |  |  | SI | ≥ 3: 	Positive Low Risk |
| Q81 | varchar |  |  | SI | <3: Negative Low Risk |
| Q82 | varchar |  |  | SI | ≥ 2: Positive High Risk |
| Q83 | varchar |  |  | SI | <2: Negative High Risk |
| Q84 | varchar |  |  | SI | Pediatric Septic Shock Trigger Tool is used to all... |
| Q85 | varchar |  |  | SI | Tachypnea |
| Q86 | varchar |  |  | SI | Score |
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