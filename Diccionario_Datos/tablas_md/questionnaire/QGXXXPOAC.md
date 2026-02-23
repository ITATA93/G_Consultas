# questionnaire.QGXXXPOAC

> Pre Operative Anaesthesia Checklist

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre Operative Anaesthesia Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Allergies |
| Q02 | varchar |  |  | SI | Smoking |
| Q03 | varchar |  |  | SI | Hypertension |
| Q04 | varchar |  |  | SI | Ischaemic Heart Disease |
| Q05 | varchar |  |  | SI | Congestive Heart Failure |
| Q06 | varchar |  |  | SI | Congestive Heart Failure |
| Q07 | varchar |  |  | SI | Chronic Obstructive Pulmonary Disease |
| Q08 | varchar |  |  | SI | Diabetes |
| Q10 | varchar |  |  | SI | Thyroid Disease |
| Q11 | varchar |  |  | SI | Jaundice |
| Q12 | varchar |  |  | SI | Chronic Renal Failure |
| Q13 | varchar |  |  | SI | Dialysis |
| Q14 | varchar |  |  | SI | Steroids |
| Q15 | varchar |  |  | SI | Prev. Anaesthestics |
| Q15a | varchar |  |  | SI | Note |
| Q16 | varchar |  |  | SI | Intubation Problems |
| Q16a | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | ICU |
| Q17a | varchar |  |  | SI | Note |
| Q18 | varchar |  |  | SI | History And Systemic Examination |
| Q19 | varchar |  |  | SI | Lab / ECG / RAD |
| Q20 | varchar |  |  | SI | Medications |
| Q21 | varchar |  |  | SI | Allergies |
| Q22 | varchar |  |  | SI | Smoking |
| Q23 | varchar |  |  | SI | Hypertension |
| Q24 | varchar |  |  | SI | Ischaemic Heart Disease  |
| Q25 | varchar |  |  | SI | Congestive Heart Failure  |
| Q26 | varchar |  |  | SI | Bronchial Asthma  |
| Q27 | varchar |  |  | SI | Chronic Obstructive Pulmonary Disease  |
| Q28 | varchar |  |  | SI | Thyroid Disease  |
| Q29 | varchar |  |  | SI | Jaundice |
| Q29ObsDR | varchar |  | FK | SI | Jaundice DR |
| Q30 | varchar |  |  | SI | Diabetes  |
| Q31 | varchar |  |  | SI | Chronic Renal Failure  |
| Q32 | varchar |  |  | SI | Dialysis |
| Q33 | varchar |  |  | SI | Steroids |
| Q37 | varchar |  |  | SI | Patient Fit For Surgery |
| Q38 | varchar |  |  | SI | Mallampatti score |
| Q39 | varchar |  |  | SI | Examinations |
| Q40 | varchar |  |  | SI | HR |
| Q40ObsDR | varchar |  | FK | SI | HR DR |
| Q41 | bit |  |  | SI | Investigations Not Required |
| Q42 | varchar |  |  | SI | SpO2 |
| Q42ObsDR | varchar |  | FK | SI | SpO2 DR |
| Q43 | varchar |  |  | SI | Systolic BP |
| Q43ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q44 | varchar |  |  | SI | Diastolic BP |
| Q44ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q45 | varchar |  |  | SI | Weight |
| Q45ObsDR | varchar |  | FK | SI | Weight DR |
| Q47 | varchar |  |  | SI | Height |
| Q47ObsDR | varchar |  | FK | SI | Height DR |
| Q48 | varchar |  |  | SI | Allergies |
| Q49 | varchar |  |  | SI | Bronchial Asthm |
| Q50 | varchar |  |  | SI | Anaesthesia |
| Q51 | bit |  |  | SI | Anaesthesia Plan, alternatives and risks explained... |
| Q52 | bit |  |  | SI | Patient understands and agrees to the anaesthesia ... |
| Q53 | bit |  |  | SI | Plan for peri-operative and post-operative pain co... |
| Q54 | varchar |  |  | SI | Investigations |
| Q56 | bigint |  |  | SI | test HTML |
| Q56TxtOnly | bigint |  |  | SI | test HTML Plain Text Only |
| Q57 | varchar |  |  | SI | Note |
| Q58 | varchar |  |  | SI | CHF |
| Q581 | varchar |  |  | SI | Abd Aus |
| Q581ObsDR | varchar |  | FK | SI | Abd Aus DR |
| Q59 | varchar |  |  | SI | Diabe |
| Q60 | numeric |  |  | SI | Age |
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