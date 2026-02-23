# questionnaire.QTCFIF

> Food Intake Chart

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Food Intake Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | varchar |  |  | SI | Cereal / Porridge	 |
| Q03 | varchar |  |  | SI | Bread / Bread Roll |
| Q04 | varchar |  |  | SI | Total meal consumed |
| Q05 | numeric |  |  | SI | Amount of nourishing drinks consumed (ml) |
| Q06 | varchar |  |  | SI | Snack |
| Q07 | numeric |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q08 | varchar |  |  | SI | Soup |
| Q09 | varchar |  |  | SI | Main course	 |
| Q10 | varchar |  |  | SI | Sandwich	 |
| Q11 | varchar |  |  | SI | Salad |
| Q12 | varchar |  |  | SI | Vegetable	 |
| Q13 | varchar |  |  | SI | Potato / Rice / Pasta	 |
| Q14 | varchar |  |  | SI | Bread / Bread roll	 |
| Q15 | varchar |  |  | SI | Pudding	 |
| Q16 | varchar |  |  | SI | Fruit	 |
| Q17 | varchar |  |  | SI | Ice cream	 |
| Q18 | varchar |  |  | SI | Yoghurt	 |
| Q19 | varchar |  |  | SI | Total meal consumed	 |
| Q20 | numeric |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q21 | varchar |  |  | SI | Snack |
| Q22 | numeric |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q23 | varchar |  |  | SI | Soup	 |
| Q24 | varchar |  |  | SI | Main course	 |
| Q25 | varchar |  |  | SI | Sandwich |
| Q26 | varchar |  |  | SI | Salad	 |
| Q27 | varchar |  |  | SI | Vegetable |
| Q28 | varchar |  |  | SI | Potato / Rice / Pasta	 |
| Q29 | varchar |  |  | SI | Bread / Bread Roll	 |
| Q30 | varchar |  |  | SI | Pudding	 |
| Q31 | varchar |  |  | SI | Fruit	 |
| Q32 | varchar |  |  | SI | Ice cream	 |
| Q33 | varchar |  |  | SI | Yoghurt	 |
| Q34 | varchar |  |  | SI | Total meal consumed	 |
| Q35 | numeric |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q36 | varchar |  |  | SI | Snack	 |
| Q37 | varchar |  |  | SI | Comments |
| Q38 | varchar |  |  | SI | Food Intake (please select amount eaten)	 |
| Q39 | varchar |  |  | SI | Nourishing drinks (i.e. Supplements, cup of milk, ... |
| Q40 | varchar |  |  | SI | Snacks |
| Q41 | varchar |  |  | SI | Food / drink taken & amount consumed	 |
| Q42 | varchar |  |  | SI | Please document any variance |
| Q43 | varchar |  |  | SI | Snacks |
| Q44 | varchar |  |  | SI | Food / drink taken & amount consumed	 |
| Q45 | varchar |  |  | SI | Please document any variance |
| Q46 | varchar |  |  | SI | Snacks |
| Q47 | varchar |  |  | SI | Food / drink taken & amount consumed	 |
| Q48 | varchar |  |  | SI | Please document any variance |
| Q49 | varchar |  |  | SI | Food / drink taken & amount consumed |
| Q50 | varchar |  |  | SI | Please document any variance |
| Q51 | varchar |  |  | SI | Food / drink taken & amount consumed	 |
| Q52 | varchar |  |  | SI | Please document any variance |
| Q53 | varchar |  |  | SI | Please document each food item individually includ... |
| Q54 | time |  |  | SI | Time |
| Q55 | varchar |  |  | SI | Breakfast |
| Q56 | varchar |  |  | SI | Soup |
| Q57 | varchar |  |  | SI | Eggs |
| Q58 | varchar |  |  | SI | Baked beans / Tinned spaghetti |
| Q59 | varchar |  |  | SI | Yogurt |
| Q60 | varchar |  |  | SI | Bread |
| Q61 | varchar |  |  | SI | Bread |
| Q62 | varchar |  |  | SI | Fruit |
| Q64 | varchar |  |  | SI | Mid-morning |
| Q66 | varchar |  |  | SI | Lunch |
| Q67 | varchar |  |  | SI | Bread |
| Q68 | varchar |  |  | SI | Bread |
| Q69 | varchar |  |  | SI | Dessert |
| Q71 | varchar |  |  | SI | Mid-afternoon |
| Q73 | varchar |  |  | SI | Evening meal |
| Q74 | varchar |  |  | SI | Bread |
| Q75 | varchar |  |  | SI | Bread |
| Q77 | varchar |  |  | SI | Supper |
| Q79 | varchar |  |  | SI | Cheese |
| Q80 | varchar |  |  | SI | Meat |
| Q81 | varchar |  |  | SI | Vegetables |
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