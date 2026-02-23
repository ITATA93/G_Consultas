# questionnaire.QTCDCS

> Diabetes Complication Status

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diabetes Complication Status

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Diabetes Complication Status |
| Q04 | date |  |  | SI | Eye review date |
| Q05 | varchar |  |  | SI | Eye review outcome |
| Q06 | varchar |  |  | SI | Macular oedema |
| Q07 | varchar |  |  | SI | Previous treatment |
| Q08 | varchar |  |  | SI | Laser treatment |
| Q09 | varchar |  |  | SI | Injections |
| Q10 | varchar |  |  | SI | Chronic kidney disease |
| Q11 | varchar |  |  | SI | Albuminuria test |
| Q12 | date |  |  | SI | Urine ACR or 24h urine protein date |
| Q13 | numeric |  |  | SI | Urine ACR or 24h urine protein result |
| Q14 | date |  |  | SI | Glomerular filtration rate (eGFR) date |
| Q15 | numeric |  |  | SI | eGFR result |
| Q16 | varchar |  |  | SI | Neuropathy |
| Q17 | varchar |  |  | SI | Examination findings |
| Q18 | varchar |  |  | SI | Sensory |
| Q19 | varchar |  |  | SI | Motor |
| Q20 | varchar |  |  | SI | Peripheral vascular disease |
| Q21 | varchar |  |  | SI | Symptoms |
| Q22 | varchar |  |  | SI | Which side, what muscle group |
| Q23 | varchar |  |  | SI | Pain location |
| Q24 | varchar |  |  | SI | Ulcer location |
| Q25 | varchar |  |  | SI | Examination findings |
| Q26 | varchar |  |  | SI | Femoral pulse |
| Q27 | varchar |  |  | SI | Popliteal pulse |
| Q28 | varchar |  |  | SI | Posterior tibial pulse |
| Q29 | varchar |  |  | SI | Dorsalis pedis pulse |
| Q30 | varchar |  |  | SI | Trophic changes |
| Q31 | varchar |  |  | SI | Ulcer grade (University of Texas system) |
| Q32 | varchar |  |  | SI | Ulcer stage (University of Texas system) |
| Q33 | varchar |  |  | SI | Imaging |
| Q34 | date |  |  | SI | Foot review date |
| Q35 | varchar |  |  | SI | Foot review outcome |
| Q36 | varchar |  |  | SI | Wound |
| Q37 | varchar |  |  | SI | Ischaemia - Toe pressure / TCPO2 |
| Q38 | varchar |  |  | SI | Foot infection |
| Q39 | varchar |  |  | SI | Acanthosis nigricans |
| Q40 | varchar |  |  | SI | Previous laser treatment |
| Q41 | varchar |  |  | SI | Previous injections |
| Q42 | varchar |  |  | SI | Ophthalmic review notes |
| Q43 | date |  |  | SI | Kidney function review date |
| Q44 | varchar |  |  | SI | Kidney disease review notes |
| Q45 | varchar |  |  | SI | Neuropathy notes |
| Q46 | varchar |  |  | SI | Peripheral vascular disease (PVD) symptom review |
| Q47 | varchar |  |  | SI | Claudication |
| Q48 | varchar |  |  | SI | Laterality |
| Q49 | varchar |  |  | SI | Muscle group(s) involved |
| Q50 | varchar |  |  | SI | Rest pain |
| Q51 | numeric |  |  | SI | Pain score at rest |
| Q52 | varchar |  |  | SI | Pain location |
| Q53 | varchar |  |  | SI | Non-healing ulcer(s) |
| Q55 | varchar |  |  | SI | Skin examination |
| Q56 | varchar |  |  | SI | Pulses examination |
| Q57 | varchar |  |  | SI | PVD review notes |
| Q58 | varchar |  |  | SI | Right Foot |
| Q59 | varchar |  |  | SI | Left Foot |
| Q60 | varchar |  |  | SI | Right foot wound |
| Q61 | varchar |  |  | SI | Left foot wound |
| Q62 | varchar |  |  | SI | Right foot ischaemia - Toe pressure / TCPO2 |
| Q63 | varchar |  |  | SI | Left foot ischaemia - Toe pressure / TCPO2 |
| Q64 | varchar |  |  | SI | Right foot infection |
| Q65 | varchar |  |  | SI | Left foot infection |
| Q66 | varchar |  |  | SI | Foot review notes |
| Q67 | date |  |  | SI | Date of last annual review of management and compl... |
| Q68 | varchar |  |  | SI | Diabetes complication status notes |
| Q69 | varchar |  |  | SI | Eye review outcome |
| Q70 | varchar |  |  | SI | Wound |
| Q71 | varchar |  |  | SI | Ischaemia Toe pressure / TCPO2 |
| Q72 | varchar |  |  | SI | Foot infection |
| Q73 | varchar |  |  | SI | Right Foot |
| Q74 | varchar |  |  | SI | Right Foot |
| Q75 | varchar |  |  | SI | Right Foot |
| Q76 | varchar |  |  | SI | Left Foot |
| Q77 | varchar |  |  | SI | Left Foot |
| Q78 | varchar |  |  | SI | Left Foot |
| Q79 | varchar |  |  | SI | Wound |
| Q80 | varchar |  |  | SI | Sensory loss |
| Q81 | varchar |  |  | SI | Monofilament (10 g semmes weinstein monofilament) |
| Q82 | varchar |  |  | SI | Vibration (128Hz tuning fork) |
| Q83 | varchar |  |  | SI | Pin prick |
| Q84 | varchar |  |  | SI | Joint position sense |
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