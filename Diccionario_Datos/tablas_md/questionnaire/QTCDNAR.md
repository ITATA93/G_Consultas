# questionnaire.QTCDNAR

> Dietetics Nutrition Assessment Report

**Schema:** questionnaire
**Columnas:** 155
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dietetics Nutrition Assessment Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date seen |
| Q02 | date |  |  | SI | Date referred |
| Q03 | varchar |  |  | SI | Referral source |
| Q04 | varchar |  |  | SI | Diet type |
| Q05 | varchar |  |  | SI | Appetite |
| Q06 | varchar |  |  | SI | Bowels |
| Q07 | varchar |  |  | SI | Biochemistry |
| Q08 | varchar |  |  | SI | Risk factors |
| Q09 | varchar |  |  | SI | Chewing / Swallowing |
| Q10 | varchar |  |  | SI | Dentures |
| Q100 | varchar |  |  | SI | Estimated energy intake (kJ/day) |
| Q101 | varchar |  |  | SI | Other |
| Q102 | varchar |  |  | SI | Patient - Generated Subjective Global Assessment (... |
| Q104 | varchar |  |  | SI | Goals / Plans |
| Q105 | varchar |  |  | SI | Nutrition prescription |
| Q106 | varchar |  |  | SI | Nutrition intervention |
| Q107 | varchar |  |  | SI | Monitoring and evaluation |
| Q108 | varchar |  |  | SI | Frequency of follow up |
| Q109 | varchar |  |  | SI | Areas to monitor |
| Q11 | varchar |  |  | SI | Nausea / Vomiting |
| Q110 | date |  |  | SI | Date |
| Q111 | time |  |  | SI | Time |
| Q12 | varchar |  |  | SI | Taste changes |
| Q13 | varchar |  |  | SI | Other |
| Q14 | varchar |  |  | SI | Antrropometry |
| Q15 | varchar |  |  | SI | Current weight (kg) |
| Q15ObsDR | varchar |  | FK | SI | Current weight (kg) DR |
| Q16 | numeric |  |  | SI | Height to weight ratio |
| Q17 | numeric |  |  | SI | BMI |
| Q18 | numeric |  |  | SI | Usual weight (kg) |
| Q19 | numeric |  |  | SI | Weight history |
| Q20 | varchar |  |  | SI | Height (cm) |
| Q20ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q21 | numeric |  |  | SI | % |
| Q22 | numeric |  |  | SI | Weight change |
| Q23 | varchar |  |  | SI | Activity |
| Q24 | varchar |  |  | SI | Nutritional related ADL |
| Q25 | varchar |  |  | SI | Observatios ADL |
| Q26 | varchar |  |  | SI | General information |
| Q27 | varchar |  |  | SI | Diet history |
| Q28 | varchar |  |  | SI | Breakfast |
| Q29 | varchar |  |  | SI | Lunch |
| Q30 | varchar |  |  | SI | Dinner |
| Q31 | varchar |  |  | SI | Morning tea |
| Q32 | varchar |  |  | SI | Afternoon tea |
| Q33 | varchar |  |  | SI | Supper |
| Q34 | varchar |  |  | SI | Checklist |
| Q35 | varchar |  |  | SI | Milk |
| Q36 | varchar |  |  | SI | Cheese |
| Q37 | varchar |  |  | SI | Yoghurt / Custard |
| Q38 | varchar |  |  | SI | Icecream |
| Q39 | varchar |  |  | SI | Meat |
| Q40 | varchar |  |  | SI | Chicken |
| Q41 | varchar |  |  | SI | Fish |
| Q42 | varchar |  |  | SI | Eggs |
| Q43 | varchar |  |  | SI | Legumes |
| Q44 | varchar |  |  | SI | Fruit |
| Q45 | varchar |  |  | SI | Vegetables |
| Q46 | varchar |  |  | SI | Potato |
| Q47 | varchar |  |  | SI | Rice |
| Q48 | varchar |  |  | SI | Pasta / Noodles |
| Q49 | varchar |  |  | SI | Bread |
| Q50 | varchar |  |  | SI | Breakfast cereals |
| Q51 | varchar |  |  | SI | Biscuits |
| Q52 | varchar |  |  | SI | Cake |
| Q53 | varchar |  |  | SI | Confectionary |
| Q54 | varchar |  |  | SI | Nuts |
| Q55 | varchar |  |  | SI | Takeaway |
| Q56 | varchar |  |  | SI | Fluids |
| Q57 | varchar |  |  | SI | Salt |
| Q58 | varchar |  |  | SI | Fats |
| Q59 | varchar |  |  | SI | Crisps |
| Q60 | varchar |  |  | SI | Alcohol |
| Q61 | varchar |  |  | SI | Supplements |
| Q62 | varchar |  |  | SI | Estimated requirements |
| Q63 | numeric |  |  | SI | BMR (using kg) |
| Q64 | varchar |  |  | SI | Activity factor |
| Q65 | varchar |  |  | SI | Injury factor |
| Q66 | varchar |  |  | SI | Energy |
| Q67 | varchar |  |  | SI | Protein (g/Kg/day) |
| Q68 | varchar |  |  | SI | Fluid (mL/Kg/day) |
| Q69 | varchar |  |  | SI | Other nutrients at risk |
| Q70 | varchar |  |  | SI | Summary of nutritional assessment |
| Q71 | varchar |  |  | SI | Nutrition diagnosis |
| Q72 | varchar |  |  | SI | Goals / Plan |
| Q73 | varchar |  |  | SI | Student |
| Q74 | longvarbinary |  |  | SI | Signed |
| Q74UDt | date |  |  | SI | Signed Last Updated Date |
| Q74UTm | time |  |  | SI | Signed Last Updated Time |
| Q75 | date |  |  | SI | Date |
| Q76 | varchar |  |  | SI | Dietitian |
| Q77 | longvarbinary |  |  | SI | Signed |
| Q77UDt | date |  |  | SI | Signed Last Updated Date |
| Q77UTm | time |  |  | SI | Signed Last Updated Time |
| Q78 | date |  |  | SI | Date |
| Q79 | varchar |  |  | SI | % |
| Q81 | varchar |  |  | SI | Weight history |
| Q82 | varchar |  |  | SI | Subjective Global Assessment (SGA) |
| Q83 | date |  |  | SI | Date |
| Q84 | time |  |  | SI | Time |
| Q85 | varchar |  |  | SI | Notes on relevant medical history |
| Q86 | varchar |  |  | SI | Notes on relevant medications |
| Q87 | varchar |  |  | SI | Notes on relevant social history |
| Q89 | varchar |  |  | SI | Snacks |
| Q90 | varchar |  |  | SI | Eating behavior |
| Q91 | varchar |  |  | SI | Non hungry emotional eating |
| Q92 | varchar |  |  | SI | Social eating |
| Q93 | varchar |  |  | SI | Food allergies / Sensitivities recorded |
| Q94 | varchar |  |  | SI | Notes regarding food allergies |
| Q95 | varchar |  |  | SI | Notes regarding food intolerances |
| Q96 | varchar |  |  | SI | Cultural / Individual considerations |
| Q97 | varchar |  |  | SI | Factors affecting access to food |
| Q98 | varchar |  |  | SI | Estimated protein intake (g/Kg/day) |
| Q99 | varchar |  |  | SI | Estimated fluid intake (ml/Kg/day) |
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