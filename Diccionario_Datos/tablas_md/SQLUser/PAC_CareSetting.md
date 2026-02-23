# SQLUser.PAC_CareSetting

**Schema:** SQLUser
**Columnas:** 170
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARESET_RowId | bigint | PK |  | NO | - |
| CARESET_Code | varchar |  |  | NO | Code |
| CARESET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CARESET_CreatedDate | date |  |  | SI | Created Date |
| CARESET_CreatedTime | time |  |  | SI | Created Time |
| CARESET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CARESET_DateFrom | date |  |  | SI | Date From |
| CARESET_DateTo | date |  |  | SI | Date To |
| CARESET_Desc | varchar |  |  | NO | Description |
| CARESET_Owner | varchar |  |  | SI | Owner |
| CARESET_UpdatedDate | date |  |  | SI | Updated Date |
| CARESET_UpdatedTime | time |  |  | SI | Updated Time |
| CARESET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ13DR | - |  |  | SI | Child Reference: Vegetables and fruits |
| Q01 | - |  |  | SI | Admission status |
| Q02 | - |  |  | SI | Age group |
| Q03 | - |  |  | SI | Diet history |
| Q04 | - |  |  | SI | Appetite |
| Q05 | - |  |  | SI | Difficulties in swallowing or chewing |
| Q06 | - |  |  | SI | If have swallowing difficulties |
| Q07 | - |  |  | SI | Bowel motions |
| Q08 | - |  |  | SI | Food allergies |
| Q09 | - |  |  | SI | If food allergies |
| Q10 | - |  |  | SI | Level of physical activity |
| Q100 | - |  |  | SI | If food drug interaction |
| Q101 | - |  |  | SI | Biochemistry |
| Q102 | - |  |  | SI | Nutritional diagnosis |
| Q103 | - |  |  | SI | Estimated energy needs (Kcal) |
| Q104 | - |  |  | SI | Method for estimating energy needs |
| Q105 | - |  |  | SI | Estimated protein needs (g) |
| Q106 | - |  |  | SI | Method for estimating protein needs |
| Q107 | - |  |  | SI | Fluid needs (ml) |
| Q108 | - |  |  | SI | Method for estimating fluid needs |
| Q109 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | GI problem |
| Q110 | - |  |  | SI | Time |
| Q111 | - |  |  | SI | Comments |
| Q112 | - |  |  | SI | Weight for age |
| Q113 | - |  |  | SI | % |
| Q114 | - |  |  | SI | Diet (Please specify) |
| Q115 | - |  |  | SI | Formula used |
| Q116 | - |  |  | SI | Route of feeding |
| Q117 | - |  |  | SI | Other routes of feeding |
| Q118 | - |  |  | SI | Ability to understand diet plan |
| Q119 | - |  |  | SI | Food assistance (need of medical device) |
| Q12 | - |  |  | SI | Is there any special formula used |
| Q120 | - |  |  | SI | Food considerations |
| Q121 | - |  |  | SI | Supplements / additives used |
| Q17 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | NR: total energy requirements (kCal/day) |
| Q25 | - |  |  | SI | NR: carbohydrate (gm/day) |
| Q26 | - |  |  | SI | NR: protein (gm/day) |
| Q27 | - |  |  | SI | NR: fat (gm/day) |
| Q28 | - |  |  | SI | NR: fluid  (ml/day) |
| Q29 | - |  |  | SI | Nutritional care plan |
| Q30 | - |  |  | SI | Measurable goals |
| Q31 | - |  |  | SI | Discharge plan |
| Q32 | - |  |  | SI | Patient and family education |
| Q33 | - |  |  | SI | Route of feeding |
| Q34 | - |  |  | SI | Delivery method |
| Q35 | - |  |  | SI | Formula type |
| Q36 | - |  |  | SI | Feeding rate |
| Q37 | - |  |  | SI | Flushing amount |
| Q38 | - |  |  | SI | Feeding tolerance |
| Q39 | - |  |  | SI | Gastric Residual Volume (GRV) |
| Q40 | - |  |  | SI | Additional notes |
| Q41 | - |  |  | SI | Height |
| Q41ObsDR | - |  |  | SI | Height DR |
| Q42 | - |  |  | SI | Weight |
| Q42ObsDR | - |  |  | SI | Weight DR |
| Q43 | - |  |  | SI | Height for age |
| Q44 | - |  |  | SI | Interpretation |
| Q45 | - |  |  | SI | Weight for height |
| Q46 | - |  |  | SI | Interpretation |
| Q46a | - |  |  | SI | Interpretation |
| Q47 | - |  |  | SI | IBW for age |
| Q48 | - |  |  | SI | IBW for height |
| Q49 | - |  |  | SI | IHT for age |
| Q50 | - |  |  | SI | Using waterflow criteria (ANS) |
| Q51 | - |  |  | SI | Stage |
| Q52 | - |  |  | SI | Using waterflow criteria (CNS) |
| Q53 | - |  |  | SI | Stage |
| Q56 | - |  |  | SI | BMI interpretation |
| Q57 | - |  |  | SI | Obesity |
| Q58 | - |  |  | SI | Percentage of weight changes |
| Q59 | - |  |  | SI | Interpretation |
| Q60 | - |  |  | SI | Ideal body weight |
| Q61 | - |  |  | SI | Adjusted body weight |
| Q61a | - |  |  | SI | Adjusted body weight |
| Q61aObsDR | - |  |  | SI | Adjusted body weight DR |
| Q62 | - |  |  | SI | Height |
| Q62ObsDR | - |  |  | SI | Height DR |
| Q63 | - |  |  | SI | Weight |
| Q63ObsDR | - |  |  | SI | Weight DR |
| Q64 | - |  |  | SI | BMI |
| Q65 | - |  |  | SI | Level of nutritional risk |
| Q66 | - |  |  | SI | Physical activity |
| Q67 | - |  |  | SI | Level of care plan |
| Q68 | - |  |  | SI | Food route |
| Q69 | - |  |  | SI | Diet |
| Q70 | - |  |  | SI | Change diet |
| Q71 | - |  |  | SI | Continue / Progress with MD diet order |
| Q72 | - |  |  | SI | Follow-up patient in clinic as needed |
| Q73 | - |  |  | SI | NR: sodium (gm/day) |
| Q74 | - |  |  | SI | NR: potassium (gm/day) |
| Q75 | - |  |  | SI | NR: phosphate (gm/day) |
| Q76 | - |  |  | SI | NR: calcium (gm/day) |
| Q77 | - |  |  | SI | NR: fibre (gm/day) |
| Q78 | - |  |  | SI | NR: iron (mg/day) |
| Q79 | - |  |  | SI | NR: total energy requirements (kCal/day) |
| Q80 | - |  |  | SI | NR: carbohydrate (gm/day) |
| Q81 | - |  |  | SI | NR: protein (gm/day) |
| Q82 | - |  |  | SI | NR: fat (gm/day) |
| Q83 | - |  |  | SI | In each of the sections below, choose the food ite... |
| Q84 | - |  |  | SI | kg |
| Q85 | - |  |  | SI | kg |
| Q86 | - |  |  | SI | kg |
| Q87 | - |  |  | SI | kg |
| Q88 | - |  |  | SI | kg |
| Q89 | - |  |  | SI | kg |
| Q90 | - |  |  | SI | cm |
| Q91 | - |  |  | SI | cm |
| Q92 | - |  |  | SI | cm |
| Q93 | - |  |  | SI | % |
| Q94 | - |  |  | SI | % |
| Q95 | - |  |  | SI | % |
| Q96 | - |  |  | SI | % |
| Q97 | - |  |  | SI | % |
| Q98 | - |  |  | SI | kg/m2 |
| Q99 | - |  |  | SI | Food drug interaction |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*