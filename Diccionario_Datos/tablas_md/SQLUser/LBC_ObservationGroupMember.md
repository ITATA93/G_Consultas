# SQLUser.LBC_ObservationGroupMember

**Schema:** SQLUser
**Columnas:** 132
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCOBSGM_ParRef | bigint | PK |  | NO | LBCPathogen Parent Reference |
| LBCOBSGM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCOBSGM_Column | double |  |  | SI | Column |
| LBCOBSGM_DateFrom | date |  |  | SI | Effective date for the record |
| LBCOBSGM_DateTo | date |  |  | SI | Last day the record is active  |
| LBCOBSGM_Observation_DR | bigint |  | FK | SI | Des Ref LBCObservation |
| LBCOBSGM_RowID | varchar |  |  | NO | - |
| LBCOBSGM_Sequence | double |  |  | SI | Sequence |
| Q01 | - |  |  | SI | Type of Diabetes |
| Q02 | - |  |  | SI | General Well Being |
| Q03 | - |  |  | SI | Patient Feels |
| Q04 | - |  |  | SI | Notes |
| Q05 | - |  |  | SI | Symptoms Experienced |
| Q06 | - |  |  | SI | Symptoms Experienced |
| Q07 | - |  |  | SI | Nutritional Aspects |
| Q08 | - |  |  | SI | Weight (kg) |
| Q08ObsDR | - |  |  | SI | Weight (kg) DR |
| Q09 | - |  |  | SI | Height (cm) |
| Q09ObsDR | - |  |  | SI | Height (cm) DR |
| Q10 | - |  |  | SI | Body Mass Index (BMI) |
| Q11 | - |  |  | SI | Recent Weight Changes |
| Q12 | - |  |  | SI | Weight Changes |
| Q13 | - |  |  | SI | Adheres to Diet Plan |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Current Level Of Activity |
| Q16 | - |  |  | SI | Activities of Daily Living (ADL) |
| Q17 | - |  |  | SI | Exercise |
| Q18 | - |  |  | SI | Frequency |
| Q19 | - |  |  | SI | Diabetes Therapy |
| Q20 | - |  |  | SI | Self Monitoring Of Blood Glucose (Smbg) |
| Q21 | - |  |  | SI | Glucometer |
| Q22 | - |  |  | SI | Glucometer Type |
| Q23 | - |  |  | SI | Cleans |
| Q24 | - |  |  | SI | Calibrates |
| Q25 | - |  |  | SI | Records Clearly |
| Q26 | - |  |  | SI | Brought Previous Record Of SMBG |
| Q27 | - |  |  | SI | Frequency Of SMBG |
| Q28 | - |  |  | SI | HbA1c |
| Q29 | - |  |  | SI | Range of Blood Sugars |
| Q30 | - |  |  | SI | Medical Mangement |
| Q31 | - |  |  | SI | Compliant with medications prescribed |
| Q32 | - |  |  | SI | Oral |
| Q33 | - |  |  | SI | Insulin |
| Q34 | - |  |  | SI | Insulin Method |
| Q34A | - |  |  | SI | Insulin Type |
| Q35 | - |  |  | SI | Uses Correct Technique Of Insulin Administration |
| Q36 | - |  |  | SI | Stores Insulin |
| Q37 | - |  |  | SI | Use Proper Injection Site |
| Q38 | - |  |  | SI | Rotates Injection Site |
| Q39 | - |  |  | SI | Disposes of Needle Safely |
| Q40 | - |  |  | SI | Psychological Status |
| Q41 | - |  |  | SI | Have You Ever Been Screened For Depression? |
| Q42 | - |  |  | SI | Have You Ever Been Diagnosed With Depression? |
| Q43 | - |  |  | SI | Awareness |
| Q44 | - |  |  | SI | Hypoglycemia |
| Q45 | - |  |  | SI | Hyperglycemia |
| Q46 | - |  |  | SI | Aware Of Symptoms |
| Q47 | - |  |  | SI | Aware Of Symptoms (Hyper) |
| Q48 | - |  |  | SI | Has experienced an attack in the past |
| Q49 | - |  |  | SI | Has experienced an attack in the past (Hyper) |
| Q50 | - |  |  | SI | Aware Of Treatment Strategies |
| Q51 | - |  |  | SI | Aware Of Treatment Strategies (Hyper) |
| Q52 | - |  |  | SI | Aware of when and how to use Glucagon |
| Q53 | - |  |  | SI | Aware of when and how to use Glucagon (Hyper) |
| Q54 | - |  |  | SI | Skin Integrity |
| Q55 | - |  |  | SI | Notes |
| Q56 | - |  |  | SI | Extremities |
| Q57 | - |  |  | SI | Feet - Healthy |
| Q58 | - |  |  | SI | Deformities |
| Q59 | - |  |  | SI | Pedal Pulse (Right Leg) |
| Q60 | - |  |  | SI | Pedal Pulse (Left Leg) |
| Q61 | - |  |  | SI | Footwear |
| Q62 | - |  |  | SI | Appropriate Shoes |
| Q63 | - |  |  | SI | Proper Fit |
| Q64 | - |  |  | SI | Loss of Sensation |
| Q65 | - |  |  | SI | Oedema |
| Q66 | - |  |  | SI | Cellulitis |
| Q67 | - |  |  | SI | Notes |
| Q68 | - |  |  | SI | Nail Condition |
| Q69 | - |  |  | SI | Notes |
| Q70 | - |  |  | SI | Neuro Sensory Assessment |
| Q71 | - |  |  | SI | Vision – Any Changes |
| Q72 | - |  |  | SI | Stress Identified / Education Given |
| Q73 | - |  |  | SI | Readiness To Learn |
| Q74 | - |  |  | SI | Asks Questions |
| Q75 | - |  |  | SI | Eager To Learn |
| Q76 | - |  |  | SI | Anxious |
| Q77 | - |  |  | SI | Denies Need For Education |
| Q78 | - |  |  | SI | Uncooperative |
| Q79 | - |  |  | SI | Unable To Learn |
| Q80 | - |  |  | SI | Notes |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*