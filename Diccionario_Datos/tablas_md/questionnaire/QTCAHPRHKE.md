# questionnaire.QTCAHPRHKE

> Knee Evaluation

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Knee Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Occupation |
| Q02 | varchar |  |  | SI | Affected knee |
| Q03 | varchar |  |  | SI | Contralateral |
| Q04 | varchar |  |  | SI | VAS score |
| Q05 | varchar |  |  | SI | Pain location  |
| Q06 | varchar |  |  | SI | Pain description |
| Q07 | varchar |  |  | SI | Pain pattern worse with the following |
| Q08 | varchar |  |  | SI | Other |
| Q09 | varchar |  |  | SI | Pain pattern better with the following |
| Q10 | varchar |  |  | SI | Other |
| Q11 | varchar |  |  | SI | Pain pattern normal with the following |
| Q12 | varchar |  |  | SI | Other |
| Q13 | varchar |  |  | SI | Stiffness |
| Q14 | varchar |  |  | SI | Swelling |
| Q15 | varchar |  |  | SI | When the swelling happend |
| Q16 | date |  |  | SI | Pain present since |
| Q17 | varchar |  |  | SI | Pain progress |
| Q18 | varchar |  |  | SI | Reason |
| Q19 | varchar |  |  | SI | Mechanism of Injury  |
| Q20 | varchar |  |  | SI | Medical history |
| Q21 | varchar |  |  | SI | Other |
| Q22 | varchar |  |  | SI | Previous surgery  |
| Q23 | varchar |  |  | SI | Comment |
| Q24 | varchar |  |  | SI | Previous physical therapy treatment  |
| Q25 | varchar |  |  | SI | X-ray |
| Q26 | varchar |  |  | SI | Report |
| Q27 | varchar |  |  | SI | Patient goals |
| Q28 | varchar |  |  | SI | Gait |
| Q29 | varchar |  |  | SI | Comment |
| Q30 | varchar |  |  | SI | Normal genu valgum |
| Q31 | varchar |  |  | SI | Genu varum  |
| Q32 | varchar |  |  | SI | Genu recurvatum  |
| Q33 | varchar |  |  | SI | Patella position |
| Q34 | varchar |  |  | SI | Effusion |
| Q35 | varchar |  |  | SI | Effusion right |
| Q36 | varchar |  |  | SI | Effusion left |
| Q37 | varchar |  |  | SI | Atrophy |
| Q38 | varchar |  |  | SI | Other |
| Q39 | varchar |  |  | SI | Temperature |
| Q40 | varchar |  |  | SI | Patella mobility |
| Q41 | varchar |  |  | SI | Tibial tubercle  |
| Q42 | varchar |  |  | SI | Patella tendon  |
| Q43 | varchar |  |  | SI | Quadriceps tendon  |
| Q44 | varchar |  |  | SI | Ligaments LCL  |
| Q45 | varchar |  |  | SI | Ligaments MCL  |
| Q46 | varchar |  |  | SI | Other |
| Q47 | varchar |  |  | SI | Girth above 15 cm left |
| Q48 | varchar |  |  | SI | Girth above 15 cm right |
| Q49 | varchar |  |  | SI | Girth 5 cm left |
| Q50 | varchar |  |  | SI | Girth 5 cm right |
| Q51 | varchar |  |  | SI | Girth med patella left |
| Q52 | varchar |  |  | SI | Girth med patella right |
| Q53 | varchar |  |  | SI | Girth 15 cm left |
| Q54 | varchar |  |  | SI | Girth 15 cm right |
| Q55 | varchar |  |  | SI | Girth Measurements |
| Q58 | varchar |  |  | SI | Leg length |
| Q59 | numeric |  |  | SI | Leg length (cm) |
| Q60 | numeric |  |  | SI | Q Angle right |
| Q61 | numeric |  |  | SI | Q Angle left |
| Q65 | varchar |  |  | SI | Other special test |
| Q66 | varchar |  |  | SI | Diagnosis |
| Q67 | varchar |  |  | SI | Problems list |
| Q68 | varchar |  |  | SI | Rehabilitation potential |
| Q69 | varchar |  |  | SI | Patient / Family participation  |
| Q70 | varchar |  |  | SI | Comment |
| Q71 | varchar |  |  | SI | Education |
| Q72 | varchar |  |  | SI | Short term goals |
| Q73 | varchar |  |  | SI | Long term goals |
| Q74 | varchar |  |  | SI | Treatment |
| Q75 | varchar |  |  | SI | Other |
| Q76 | numeric |  |  | SI | Number of treatments per week |
| Q77 | numeric |  |  | SI | Number of weeks |
| Q78 | varchar |  |  | SI | Re Evaluation  |
| Q79 | varchar |  |  | SI | Chief Complaint |
| Q80 | varchar |  |  | SI | Observation |
| Q81 | varchar |  |  | SI | Alignment |
| Q82 | varchar |  |  | SI | Palpation |
| Q83 | varchar |  |  | SI | Examination |
| Q84 | date |  |  | SI | Date |
| Q85 | time |  |  | SI | Time |
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