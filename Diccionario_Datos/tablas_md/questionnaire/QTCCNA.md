# questionnaire.QTCCNA

> Clinical Nutrition Assessment

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Nutrition Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Food and Nutrient Intake |
| Q02 | varchar |  |  | SI | Food and Nutrient Administration |
| Q02a | varchar |  |  | SI | Specify Other Food and Nutrient Administration |
| Q03 | varchar |  |  | SI | Medication and Herbal Supplement Use |
| Q03a | varchar |  |  | SI | Specify Other Medication & Supplement use |
| Q04 | varchar |  |  | SI | Knowledge/ Beliefs/ Attitudes/ Behaviour |
| Q04a | varchar |  |  | SI | Specify Other Knowledge, Beliefs etc |
| Q05 | varchar |  |  | SI | Factors Affecting Access to Food and Food / Nutrit... |
| Q05a | varchar |  |  | SI | Specfy Other Factors Affecting |
| Q06 | varchar |  |  | SI | Physical Activity and Function |
| Q06a | varchar |  |  | SI | Specify Other Physical Activity and Function |
| Q07 | varchar |  |  | SI | Nutrition-Focused Physical Findings |
| Q07a | varchar |  |  | SI | Specify Other Nutirition Focussed Physical Finding... |
| Q08 | varchar |  |  | SI | Biochemical Data, Medical Tests and Procedures |
| Q09 | numeric |  |  | SI | Height (cm) |
| Q10 | numeric |  |  | SI | Weight (kg) |
| Q11 | numeric |  |  | SI | Estimated Dry Wt: |
| Q12 | varchar |  |  | SI | BMI |
| Q13 | varchar |  |  | SI | Frame Size |
| Q14 | numeric |  |  | SI | Ideal Body Wt (kg) |
| Q15 | numeric |  |  | SI | % Ideal Body Wt |
| Q16 | numeric |  |  | SI | Adjusted Wt (kg) |
| Q17 | numeric |  |  | SI | Usual Body Wt (kg) |
| Q18 | numeric |  |  | SI | % Usual Body Wt |
| Q19 | numeric |  |  | SI | Height/ Length (cm) |
| Q20 | numeric |  |  | SI | Height/ Length Percentile |
| Q20a | varchar |  |  | SI | %ile |
| Q21 | numeric |  |  | SI | Weight (kg) |
| Q22 | numeric |  |  | SI | Weight Percentile |
| Q22a | varchar |  |  | SI | %ile |
| Q23 | varchar |  |  | SI | BMI |
| Q24 | numeric |  |  | SI | BMI Percentile |
| Q24a | varchar |  |  | SI | %ile |
| Q25 | numeric |  |  | SI | Weight for Length %ile |
| Q25a | varchar |  |  | SI | %ile |
| Q26 | numeric |  |  | SI | Ideal BMI |
| Q27 | numeric |  |  | SI | IBW |
| Q28 | varchar |  |  | SI | Anthropometric History |
| Q29 | numeric |  |  | SI | Estimated energy needs (Kcal) |
| Q29a | varchar |  |  | SI | Method for estimating energy needs |
| Q30 | numeric |  |  | SI | Estimated protein needs (gms/day) |
| Q30a | varchar |  |  | SI | Method for estimating protein needs |
| Q31 | numeric |  |  | SI | Fluid needs (ml) |
| Q31a | varchar |  |  | SI | Method for estimating fluid needs |
| Q32 | varchar |  |  | SI | Additional Information (if needed) |
| Q33 | varchar |  |  | SI | Nutritional Diagnosis / Problems |
| Q34 | varchar |  |  | SI | Nutrition Prescription |
| Q35 | varchar |  |  | SI | Food and/or Nutrient Delivery |
| Q36 | bit |  |  | SI | Meals and Snacks |
| Q36a | varchar |  |  | SI | Specify Meals and Snacks |
| Q37 | bit |  |  | SI | Enteral / Parenteral feeding |
| Q37a | varchar |  |  | SI | Specify Enteral feeding |
| Q38 | bit |  |  | SI | Supplements |
| Q38a | varchar |  |  | SI | Specify Supplements |
| Q39 | bit |  |  | SI | Vitamins/ Minerals Supplements |
| Q39a | varchar |  |  | SI | Specify Vitamins/ Minerals Supplements |
| Q40 | bit |  |  | SI | Feeding assistance and environment |
| Q40a | varchar |  |  | SI | Specify Feeding assistance and environment |
| Q41 | bit |  |  | SI | Changing in medication that can optimize patients’... |
| Q41a | varchar |  |  | SI | Specify Changing in medication that can optimize p... |
| Q42 | varchar |  |  | SI | Nutrition Education and Counseling |
| Q43 | varchar |  |  | SI | Coordination of Care |
| Q44 | varchar |  |  | SI | Additional intervention if needed |
| Q45 | varchar |  |  | SI | Monitoring and Evaluation |
| Q46 | varchar |  |  | SI | Recommendations |
| Q47 | varchar |  |  | SI | Level of Care |
| Q48 | longvarbinary |  |  | SI | Signature |
| Q48UDt | date |  |  | SI | Signature Last Updated Date |
| Q48UTm | time |  |  | SI | Signature Last Updated Time |
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