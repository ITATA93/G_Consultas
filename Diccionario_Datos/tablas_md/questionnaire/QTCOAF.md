# questionnaire.QTCOAF

> Osteoporosis Assessment

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Osteoporosis Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Assessment type |
| Q02 | date |  |  | SI | Assessment date |
| Q03 | time |  |  | SI | Assessment time |
| Q04 | varchar |  |  | SI | Osteoporosis diagnosis established |
| Q05 | varchar |  |  | SI | Previous osteoporosis diagnosis |
| Q06 | varchar |  |  | SI | New fragility fracture |
| Q07 | varchar |  |  | SI | Identify risk factors for fractures and falls |
| Q08 | varchar |  |  | SI | Prior fracture after age 50 years |
| Q09 | varchar |  |  | SI | Other fracture, specify |
| Q10 | varchar |  |  | SI | Prolonged glucocorticoid use |
| Q11 | varchar |  |  | SI | Parental hip fracture |
| Q12 | varchar |  |  | SI | Rheumatoid arthritis |
| Q13 | varchar |  |  | SI | Menopause at age <45 years |
| Q14 | varchar |  |  | SI | Current smoker |
| Q15 | varchar |  |  | SI | Consumes 3 units (oz.) alcohol/day |
| Q16 | varchar |  |  | SI | Has fallen 2 times in past 12 months |
| Q17 | varchar |  |  | SI | Low body weight (<60 kg)  |
| Q18 | varchar |  |  | SI | Major weight loss |
| Q19 | varchar |  |  | SI | Diet + supplement calcium intake 1200 mg/day |
| Q20 | varchar |  |  | SI | A. Assess balance and gait for fracture risk |
| Q21 | varchar |  |  | SI | Can patient rise from chair without using arms and... |
| Q22 | varchar |  |  | SI | B. Screening for vertebral fracture |
| Q23 | varchar |  |  | SI | Current height (cm) |
| Q23ObsDR | varchar |  | FK | SI | Current height (cm) DR |
| Q24 | varchar |  |  | SI | Prospective height loss > 2 cm |
| Q25 | varchar |  |  | SI | Historical height loss > 6 cm |
| Q26 | varchar |  |  | SI | Rib-pelvis distance ≥ 2 fingers |
| Q27 | varchar |  |  | SI | Occiput-wall distance > 5 cm |
| Q28 | varchar |  |  | SI | If Yes to any, order PA lateral spine x-ray to rul... |
| Q29 | varchar |  |  | SI | Lab test done and reviewed |
| Q33 | varchar |  |  | SI | Previous risk |
| Q34 | varchar |  |  | SI | Current risk |
| Q35 | varchar |  |  | SI | Low risk |
| Q36 | varchar |  |  | SI | No pharmacotherapy indicated |
| Q37 | varchar |  |  | SI | Reassessment in 1-3 years |
| Q38 | varchar |  |  | SI | Moderate risk |
| Q39 | varchar |  |  | SI | Consider pharmacotherapy if patient has at least o... |
| Q40 | varchar |  |  | SI | High risk |
| Q41 | varchar |  |  | SI | OR one fragility fracture hip/spine |
| Q42 | varchar |  |  | SI | OR more than one fragility fracture |
| Q43 | varchar |  |  | SI | Start pharmacotherapy |
| Q44 | varchar |  |  | SI | T-score fermoral neck (female) |
| Q45 | varchar |  |  | SI | T-score fermoral neck (male) |
| Q46 | date |  |  | SI | Date |
| Q47 | time |  |  | SI | Time |
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