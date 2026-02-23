# SQLUser.ORC_Intub_Route

**Schema:** SQLUser
**Columnas:** 170
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INROU_RowId | bigint | PK |  | NO | - |
| ChildQ103DR | - |  |  | SI | Child Reference: Nutritional Diagnosis |
| INROU_Code | varchar |  |  | NO | INROU Code |
| INROU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INROU_CreatedDate | date |  |  | SI | Created Date |
| INROU_CreatedTime | time |  |  | SI | Created Time |
| INROU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INROU_DateFrom | date |  |  | SI | Date From |
| INROU_DateTo | date |  |  | SI | Date To |
| INROU_Desc | varchar |  |  | NO | INROU Description |
| INROU_ETTType | varchar |  |  | SI | ETT(Endotracheal Tube) Type  |
| INROU_LMAType | varchar |  |  | SI | LMA(Laryngeal Mask Airway) Type  |
| INROU_Owner | varchar |  |  | SI | Owner |
| INROU_UpdatedDate | date |  |  | SI | Updated Date |
| INROU_UpdatedTime | time |  |  | SI | Updated Time |
| INROU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date seen |
| Q02 | - |  |  | SI | Date referred |
| Q03 | - |  |  | SI | Referral source |
| Q04 | - |  |  | SI | Diet type |
| Q05 | - |  |  | SI | Appetite |
| Q06 | - |  |  | SI | Bowels |
| Q07 | - |  |  | SI | Biochemistry |
| Q08 | - |  |  | SI | Risk factors |
| Q09 | - |  |  | SI | Chewing / Swallowing |
| Q10 | - |  |  | SI | Dentures |
| Q100 | - |  |  | SI | Estimated energy intake (kJ/day) |
| Q101 | - |  |  | SI | Other |
| Q102 | - |  |  | SI | Patient - Generated Subjective Global Assessment (... |
| Q104 | - |  |  | SI | Goals / Plans |
| Q105 | - |  |  | SI | Nutrition prescription |
| Q106 | - |  |  | SI | Nutrition intervention |
| Q107 | - |  |  | SI | Monitoring and evaluation |
| Q108 | - |  |  | SI | Frequency of follow up |
| Q109 | - |  |  | SI | Areas to monitor |
| Q11 | - |  |  | SI | Nausea / Vomiting |
| Q110 | - |  |  | SI | Date |
| Q111 | - |  |  | SI | Time |
| Q12 | - |  |  | SI | Taste changes |
| Q13 | - |  |  | SI | Other |
| Q14 | - |  |  | SI | Antrropometry |
| Q15 | - |  |  | SI | Current weight (kg) |
| Q15ObsDR | - |  |  | SI | Current weight (kg) DR |
| Q16 | - |  |  | SI | Height to weight ratio |
| Q17 | - |  |  | SI | BMI |
| Q18 | - |  |  | SI | Usual weight (kg) |
| Q19 | - |  |  | SI | Weight history |
| Q20 | - |  |  | SI | Height (cm) |
| Q20ObsDR | - |  |  | SI | Height (cm) DR |
| Q21 | - |  |  | SI | % |
| Q22 | - |  |  | SI | Weight change |
| Q23 | - |  |  | SI | Activity |
| Q24 | - |  |  | SI | Nutritional related ADL |
| Q25 | - |  |  | SI | Observatios ADL |
| Q26 | - |  |  | SI | General information |
| Q27 | - |  |  | SI | Diet history |
| Q28 | - |  |  | SI | Breakfast |
| Q29 | - |  |  | SI | Lunch |
| Q30 | - |  |  | SI | Dinner |
| Q31 | - |  |  | SI | Morning tea |
| Q32 | - |  |  | SI | Afternoon tea |
| Q33 | - |  |  | SI | Supper |
| Q34 | - |  |  | SI | Checklist |
| Q35 | - |  |  | SI | Milk |
| Q36 | - |  |  | SI | Cheese |
| Q37 | - |  |  | SI | Yoghurt / Custard |
| Q38 | - |  |  | SI | Icecream |
| Q39 | - |  |  | SI | Meat |
| Q40 | - |  |  | SI | Chicken |
| Q41 | - |  |  | SI | Fish |
| Q42 | - |  |  | SI | Eggs |
| Q43 | - |  |  | SI | Legumes |
| Q44 | - |  |  | SI | Fruit |
| Q45 | - |  |  | SI | Vegetables |
| Q46 | - |  |  | SI | Potato |
| Q47 | - |  |  | SI | Rice |
| Q48 | - |  |  | SI | Pasta / Noodles |
| Q49 | - |  |  | SI | Bread |
| Q50 | - |  |  | SI | Breakfast cereals |
| Q51 | - |  |  | SI | Biscuits |
| Q52 | - |  |  | SI | Cake |
| Q53 | - |  |  | SI | Confectionary |
| Q54 | - |  |  | SI | Nuts |
| Q55 | - |  |  | SI | Takeaway |
| Q56 | - |  |  | SI | Fluids |
| Q57 | - |  |  | SI | Salt |
| Q58 | - |  |  | SI | Fats |
| Q59 | - |  |  | SI | Crisps |
| Q60 | - |  |  | SI | Alcohol |
| Q61 | - |  |  | SI | Supplements |
| Q62 | - |  |  | SI | Estimated requirements |
| Q63 | - |  |  | SI | BMR (using kg) |
| Q64 | - |  |  | SI | Activity factor |
| Q65 | - |  |  | SI | Injury factor |
| Q66 | - |  |  | SI | Energy |
| Q67 | - |  |  | SI | Protein (g/Kg/day) |
| Q68 | - |  |  | SI | Fluid (mL/Kg/day) |
| Q69 | - |  |  | SI | Other nutrients at risk |
| Q70 | - |  |  | SI | Summary of nutritional assessment |
| Q71 | - |  |  | SI | Nutrition diagnosis |
| Q72 | - |  |  | SI | Goals / Plan |
| Q73 | - |  |  | SI | Student |
| Q74 | - |  |  | SI | Signed |
| Q74UDt | - |  |  | SI | Signed Last Updated Date |
| Q74UTm | - |  |  | SI | Signed Last Updated Time |
| Q75 | - |  |  | SI | Date |
| Q76 | - |  |  | SI | Dietitian |
| Q77 | - |  |  | SI | Signed |
| Q77UDt | - |  |  | SI | Signed Last Updated Date |
| Q77UTm | - |  |  | SI | Signed Last Updated Time |
| Q78 | - |  |  | SI | Date |
| Q79 | - |  |  | SI | % |
| Q81 | - |  |  | SI | Weight history |
| Q82 | - |  |  | SI | Subjective Global Assessment (SGA) |
| Q83 | - |  |  | SI | Date |
| Q84 | - |  |  | SI | Time |
| Q85 | - |  |  | SI | Notes on relevant medical history |
| Q86 | - |  |  | SI | Notes on relevant medications |
| Q87 | - |  |  | SI | Notes on relevant social history |
| Q89 | - |  |  | SI | Snacks |
| Q90 | - |  |  | SI | Eating behavior |
| Q91 | - |  |  | SI | Non hungry emotional eating |
| Q92 | - |  |  | SI | Social eating |
| Q93 | - |  |  | SI | Food allergies / Sensitivities recorded |
| Q94 | - |  |  | SI | Notes regarding food allergies |
| Q95 | - |  |  | SI | Notes regarding food intolerances |
| Q96 | - |  |  | SI | Cultural / Individual considerations |
| Q97 | - |  |  | SI | Factors affecting access to food |
| Q98 | - |  |  | SI | Estimated protein intake (g/Kg/day) |
| Q99 | - |  |  | SI | Estimated fluid intake (ml/Kg/day) |
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