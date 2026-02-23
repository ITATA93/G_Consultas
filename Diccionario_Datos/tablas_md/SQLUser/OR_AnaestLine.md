# SQLUser.OR_AnaestLine

**Schema:** SQLUser
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANALINE_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANALINE_Childsub | double |  |  | NO | Childsub |
| ANALINE_RowId | varchar |  |  | NO | - |
| ANALINE_Type_DR | bigint |  | FK | SI | Des Ref ORCLineType |
| ChildQ63DR | - |  |  | SI | Child Reference: Drinks |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Cereal / Porridge	 |
| Q03 | - |  |  | SI | Bread / Bread Roll |
| Q04 | - |  |  | SI | Total meal consumed |
| Q05 | - |  |  | SI | Amount of nourishing drinks consumed (ml) |
| Q06 | - |  |  | SI | Snack |
| Q07 | - |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q08 | - |  |  | SI | Soup |
| Q09 | - |  |  | SI | Main course	 |
| Q10 | - |  |  | SI | Sandwich	 |
| Q11 | - |  |  | SI | Salad |
| Q12 | - |  |  | SI | Vegetable	 |
| Q13 | - |  |  | SI | Potato / Rice / Pasta	 |
| Q14 | - |  |  | SI | Bread / Bread roll	 |
| Q15 | - |  |  | SI | Pudding	 |
| Q16 | - |  |  | SI | Fruit	 |
| Q17 | - |  |  | SI | Ice cream	 |
| Q18 | - |  |  | SI | Yoghurt	 |
| Q19 | - |  |  | SI | Total meal consumed	 |
| Q20 | - |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q21 | - |  |  | SI | Snack |
| Q22 | - |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q23 | - |  |  | SI | Soup	 |
| Q24 | - |  |  | SI | Main course	 |
| Q25 | - |  |  | SI | Sandwich |
| Q26 | - |  |  | SI | Salad	 |
| Q27 | - |  |  | SI | Vegetable |
| Q28 | - |  |  | SI | Potato / Rice / Pasta	 |
| Q29 | - |  |  | SI | Bread / Bread Roll	 |
| Q30 | - |  |  | SI | Pudding	 |
| Q31 | - |  |  | SI | Fruit	 |
| Q32 | - |  |  | SI | Ice cream	 |
| Q33 | - |  |  | SI | Yoghurt	 |
| Q34 | - |  |  | SI | Total meal consumed	 |
| Q35 | - |  |  | SI | Amount of nourishing drinks consumed (ml)	 |
| Q36 | - |  |  | SI | Snack	 |
| Q37 | - |  |  | SI | Comments |
| Q38 | - |  |  | SI | Food Intake (please select amount eaten)	 |
| Q39 | - |  |  | SI | Nourishing drinks (i.e. Supplements, cup of milk, ... |
| Q40 | - |  |  | SI | Snacks |
| Q41 | - |  |  | SI | Food / drink taken & amount consumed	 |
| Q42 | - |  |  | SI | Please document any variance |
| Q43 | - |  |  | SI | Snacks |
| Q44 | - |  |  | SI | Food / drink taken & amount consumed	 |
| Q45 | - |  |  | SI | Please document any variance |
| Q46 | - |  |  | SI | Snacks |
| Q47 | - |  |  | SI | Food / drink taken & amount consumed	 |
| Q48 | - |  |  | SI | Please document any variance |
| Q49 | - |  |  | SI | Food / drink taken & amount consumed |
| Q50 | - |  |  | SI | Please document any variance |
| Q51 | - |  |  | SI | Food / drink taken & amount consumed	 |
| Q52 | - |  |  | SI | Please document any variance |
| Q53 | - |  |  | SI | Please document each food item individually includ... |
| Q54 | - |  |  | SI | Time |
| Q55 | - |  |  | SI | Breakfast |
| Q56 | - |  |  | SI | Soup |
| Q57 | - |  |  | SI | Eggs |
| Q58 | - |  |  | SI | Baked beans / Tinned spaghetti |
| Q59 | - |  |  | SI | Yogurt |
| Q60 | - |  |  | SI | Bread |
| Q61 | - |  |  | SI | Bread |
| Q62 | - |  |  | SI | Fruit |
| Q64 | - |  |  | SI | Mid-morning |
| Q66 | - |  |  | SI | Lunch |
| Q67 | - |  |  | SI | Bread |
| Q68 | - |  |  | SI | Bread |
| Q69 | - |  |  | SI | Dessert |
| Q71 | - |  |  | SI | Mid-afternoon |
| Q73 | - |  |  | SI | Evening meal |
| Q74 | - |  |  | SI | Bread |
| Q75 | - |  |  | SI | Bread |
| Q77 | - |  |  | SI | Supper |
| Q79 | - |  |  | SI | Cheese |
| Q80 | - |  |  | SI | Meat |
| Q81 | - |  |  | SI | Vegetables |
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