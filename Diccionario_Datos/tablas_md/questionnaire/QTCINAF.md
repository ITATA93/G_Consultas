# questionnaire.QTCINAF

> Initial Nutritional Assessment Form

**Schema:** questionnaire
**Columnas:** 157
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Initial Nutritional Assessment Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Admission status |
| Q02 | varchar |  |  | SI | Age group |
| Q03 | varchar |  |  | SI | Diet history |
| Q04 | varchar |  |  | SI | Appetite |
| Q05 | varchar |  |  | SI | Difficulties in swallowing or chewing |
| Q06 | varchar |  |  | SI | If have swallowing difficulties |
| Q07 | varchar |  |  | SI | Bowel motions |
| Q08 | varchar |  |  | SI | Food allergies |
| Q09 | varchar |  |  | SI | If food allergies |
| Q10 | varchar |  |  | SI | Level of physical activity |
| Q100 | varchar |  |  | SI | If food drug interaction |
| Q101 | varchar |  |  | SI | Biochemistry |
| Q102 | varchar |  |  | SI | Nutritional diagnosis |
| Q103 | numeric |  |  | SI | Estimated energy needs (Kcal) |
| Q104 | varchar |  |  | SI | Method for estimating energy needs |
| Q105 | numeric |  |  | SI | Estimated protein needs (g) |
| Q106 | varchar |  |  | SI | Method for estimating protein needs |
| Q107 | numeric |  |  | SI | Fluid needs (ml) |
| Q108 | varchar |  |  | SI | Method for estimating fluid needs |
| Q109 | date |  |  | SI | Date |
| Q11 | varchar |  |  | SI | GI problem |
| Q110 | time |  |  | SI | Time |
| Q111 | varchar |  |  | SI | Comments |
| Q112 | numeric |  |  | SI | Weight for age |
| Q113 | varchar |  |  | SI | % |
| Q114 | varchar |  |  | SI | Diet (Please specify) |
| Q115 | varchar |  |  | SI | Formula used |
| Q116 | varchar |  |  | SI | Route of feeding |
| Q117 | varchar |  |  | SI | Other routes of feeding |
| Q118 | varchar |  |  | SI | Ability to understand diet plan |
| Q119 | varchar |  |  | SI | Food assistance (need of medical device) |
| Q12 | varchar |  |  | SI | Is there any special formula used  |
| Q120 | varchar |  |  | SI | Food considerations |
| Q121 | varchar |  |  | SI | Supplements / additives used |
| Q17 | varchar |  |  | SI | Comments |
| Q24 | numeric |  |  | SI | NR: total energy requirements (kCal/day) |
| Q25 | numeric |  |  | SI | NR: carbohydrate (gm/day) |
| Q26 | numeric |  |  | SI | NR: protein (gm/day) |
| Q27 | numeric |  |  | SI | NR: fat (gm/day) |
| Q28 | numeric |  |  | SI | NR: fluid  (ml/day) |
| Q29 | varchar |  |  | SI | Nutritional care plan  |
| Q30 | varchar |  |  | SI | Measurable goals |
| Q31 | varchar |  |  | SI | Discharge plan |
| Q32 | varchar |  |  | SI | Patient and family education |
| Q33 | varchar |  |  | SI | Route of feeding |
| Q34 | varchar |  |  | SI | Delivery method |
| Q35 | varchar |  |  | SI | Formula type |
| Q36 | varchar |  |  | SI | Feeding rate |
| Q37 | varchar |  |  | SI | Flushing amount |
| Q38 | varchar |  |  | SI | Feeding tolerance |
| Q39 | varchar |  |  | SI | Gastric Residual Volume (GRV) |
| Q40 | varchar |  |  | SI | Additional notes |
| Q41 | varchar |  |  | SI | Height |
| Q41ObsDR | varchar |  | FK | SI | Height DR |
| Q42 | varchar |  |  | SI | Weight |
| Q42ObsDR | varchar |  | FK | SI | Weight DR |
| Q43 | numeric |  |  | SI | Height for age |
| Q44 | varchar |  |  | SI | Interpretation |
| Q45 | numeric |  |  | SI | Weight for height |
| Q46 | numeric |  |  | SI | Interpretation |
| Q46a | varchar |  |  | SI | Interpretation |
| Q47 | numeric |  |  | SI | IBW for age |
| Q48 | varchar |  |  | SI | IBW for height |
| Q49 | varchar |  |  | SI | IHT for age |
| Q50 | varchar |  |  | SI | Using waterflow criteria (ANS) |
| Q51 | varchar |  |  | SI | Stage |
| Q52 | varchar |  |  | SI | Using waterflow criteria (CNS) |
| Q53 | varchar |  |  | SI | Stage |
| Q56 | varchar |  |  | SI | BMI interpretation |
| Q57 | varchar |  |  | SI | Obesity |
| Q58 | varchar |  |  | SI | Percentage of weight changes |
| Q59 | varchar |  |  | SI | Interpretation |
| Q60 | varchar |  |  | SI | Ideal body weight |
| Q61 | varchar |  |  | SI | Adjusted body weight |
| Q61a | varchar |  |  | SI | Adjusted body weight |
| Q61aObsDR | varchar |  | FK | SI | Adjusted body weight DR |
| Q62 | varchar |  |  | SI | Height |
| Q62ObsDR | varchar |  | FK | SI | Height DR |
| Q63 | varchar |  |  | SI | Weight |
| Q63ObsDR | varchar |  | FK | SI | Weight DR |
| Q64 | varchar |  |  | SI | BMI |
| Q65 | varchar |  |  | SI | Level of nutritional risk |
| Q66 | varchar |  |  | SI | Physical activity |
| Q67 | varchar |  |  | SI | Level of care plan |
| Q68 | varchar |  |  | SI | Food route |
| Q69 | varchar |  |  | SI | Diet |
| Q70 | bit |  |  | SI | Change diet |
| Q71 | varchar |  |  | SI | Continue / Progress with MD diet order |
| Q72 | varchar |  |  | SI | Follow-up patient in clinic as needed |
| Q73 | numeric |  |  | SI | NR: sodium (gm/day) |
| Q74 | numeric |  |  | SI | NR: potassium (gm/day) |
| Q75 | numeric |  |  | SI | NR: phosphate (gm/day) |
| Q76 | numeric |  |  | SI | NR: calcium (gm/day) |
| Q77 | numeric |  |  | SI | NR: fibre (gm/day) |
| Q78 | numeric |  |  | SI | NR: iron (mg/day) |
| Q79 | numeric |  |  | SI | NR: total energy requirements (kCal/day) |
| Q80 | numeric |  |  | SI | NR: carbohydrate (gm/day) |
| Q81 | numeric |  |  | SI | NR: protein (gm/day) |
| Q82 | numeric |  |  | SI | NR: fat (gm/day) |
| Q83 | varchar |  |  | SI | In each of the sections below, choose the food ite... |
| Q84 | varchar |  |  | SI | kg |
| Q85 | varchar |  |  | SI | kg |
| Q86 | varchar |  |  | SI | kg |
| Q87 | varchar |  |  | SI | kg |
| Q88 | varchar |  |  | SI | kg |
| Q89 | varchar |  |  | SI | kg |
| Q90 | varchar |  |  | SI | cm |
| Q91 | varchar |  |  | SI | cm |
| Q92 | varchar |  |  | SI | cm |
| Q93 | varchar |  |  | SI | % |
| Q94 | varchar |  |  | SI | % |
| Q95 | varchar |  |  | SI | % |
| Q96 | varchar |  |  | SI | % |
| Q97 | varchar |  |  | SI | % |
| Q98 | varchar |  |  | SI | kg/m2 |
| Q99 | varchar |  |  | SI | Food drug interaction |
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