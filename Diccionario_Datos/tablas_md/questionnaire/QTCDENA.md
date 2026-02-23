# questionnaire.QTCDENA

> Diabetes Education Need Assessment

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diabetes Education Need Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of Diabetes |
| Q02 | varchar |  |  | SI | General Well Being |
| Q03 | varchar |  |  | SI | Patient Feels |
| Q04 | varchar |  |  | SI | Notes |
| Q05 | varchar |  |  | SI | Symptoms Experienced |
| Q06 | varchar |  |  | SI | Symptoms Experienced |
| Q07 | varchar |  |  | SI | Nutritional Aspects |
| Q08 | varchar |  |  | SI | Weight (kg) |
| Q08ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q09 | varchar |  |  | SI | Height (cm) |
| Q09ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q10 | varchar |  |  | SI | Body Mass Index (BMI) |
| Q11 | varchar |  |  | SI | Recent Weight Changes |
| Q12 | varchar |  |  | SI | Weight Changes  |
| Q13 | varchar |  |  | SI | Adheres to Diet Plan |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Current Level Of Activity |
| Q16 | varchar |  |  | SI | Activities of Daily Living (ADL) |
| Q17 | varchar |  |  | SI | Exercise |
| Q18 | varchar |  |  | SI | Frequency |
| Q19 | varchar |  |  | SI | Diabetes Therapy |
| Q20 | varchar |  |  | SI | Self Monitoring Of Blood Glucose (Smbg) |
| Q21 | varchar |  |  | SI | Glucometer |
| Q22 | varchar |  |  | SI | Glucometer Type |
| Q23 | varchar |  |  | SI | Cleans |
| Q24 | varchar |  |  | SI | Calibrates |
| Q25 | varchar |  |  | SI | Records Clearly |
| Q26 | varchar |  |  | SI | Brought Previous Record Of SMBG |
| Q27 | varchar |  |  | SI | Frequency Of SMBG |
| Q28 | varchar |  |  | SI | HbA1c |
| Q29 | varchar |  |  | SI | Range of Blood Sugars |
| Q30 | varchar |  |  | SI | Medical Mangement |
| Q31 | varchar |  |  | SI | Compliant with medications prescribed |
| Q32 | varchar |  |  | SI | Oral |
| Q33 | varchar |  |  | SI | Insulin |
| Q34 | varchar |  |  | SI | Insulin Method |
| Q34A | varchar |  |  | SI | Insulin Type |
| Q35 | varchar |  |  | SI | Uses Correct Technique Of Insulin Administration |
| Q36 | varchar |  |  | SI | Stores Insulin |
| Q37 | varchar |  |  | SI | Use Proper Injection Site |
| Q38 | varchar |  |  | SI | Rotates Injection Site |
| Q39 | varchar |  |  | SI | Disposes of Needle Safely |
| Q40 | varchar |  |  | SI | Psychological Status |
| Q41 | varchar |  |  | SI | Have You Ever Been Screened For Depression? |
| Q42 | varchar |  |  | SI | Have You Ever Been Diagnosed With Depression? |
| Q43 | varchar |  |  | SI | Awareness |
| Q44 | varchar |  |  | SI | Hypoglycemia |
| Q45 | varchar |  |  | SI | Hyperglycemia |
| Q46 | varchar |  |  | SI | Aware Of Symptoms |
| Q47 | varchar |  |  | SI | Aware Of Symptoms (Hyper) |
| Q48 | varchar |  |  | SI | Has experienced an attack in the past |
| Q49 | varchar |  |  | SI | Has experienced an attack in the past (Hyper) |
| Q50 | varchar |  |  | SI | Aware Of Treatment Strategies |
| Q51 | varchar |  |  | SI | Aware Of Treatment Strategies (Hyper) |
| Q52 | varchar |  |  | SI | Aware of when and how to use Glucagon |
| Q53 | varchar |  |  | SI | Aware of when and how to use Glucagon (Hyper) |
| Q54 | varchar |  |  | SI | Skin Integrity |
| Q55 | varchar |  |  | SI | Notes |
| Q56 | varchar |  |  | SI | Extremities |
| Q57 | varchar |  |  | SI | Feet - Healthy |
| Q58 | varchar |  |  | SI | Deformities |
| Q59 | varchar |  |  | SI | Pedal Pulse (Right Leg) |
| Q60 | varchar |  |  | SI | Pedal Pulse (Left Leg) |
| Q61 | varchar |  |  | SI | Footwear |
| Q62 | varchar |  |  | SI | Appropriate Shoes |
| Q63 | varchar |  |  | SI | Proper Fit |
| Q64 | varchar |  |  | SI | Loss of Sensation |
| Q65 | varchar |  |  | SI | Oedema |
| Q66 | varchar |  |  | SI | Cellulitis |
| Q67 | varchar |  |  | SI | Notes |
| Q68 | varchar |  |  | SI | Nail Condition |
| Q69 | varchar |  |  | SI | Notes |
| Q70 | varchar |  |  | SI | Neuro Sensory Assessment |
| Q71 | varchar |  |  | SI | Vision – Any Changes |
| Q72 | varchar |  |  | SI | Stress Identified / Education Given |
| Q73 | varchar |  |  | SI | Readiness To Learn |
| Q74 | varchar |  |  | SI | Asks Questions |
| Q75 | varchar |  |  | SI | Eager To Learn |
| Q76 | varchar |  |  | SI | Anxious |
| Q77 | varchar |  |  | SI | Denies Need For Education |
| Q78 | varchar |  |  | SI | Uncooperative |
| Q79 | varchar |  |  | SI | Unable To Learn |
| Q80 | varchar |  |  | SI | Notes |
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