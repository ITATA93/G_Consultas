# SQLUser.IN_DispItm

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDSI_INDS_ParRef | bigint | PK |  | NO | Des Ref To INDS |
| INDSI_AdmixManuf_DR | varchar |  | FK | SI | Des Ref User.OEAdmixManuf |
| INDSI_AmountSoldFor | double |  |  | SI | Amount Sold for |
| INDSI_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INDSI_CTUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| INDSI_ChildSub | numeric |  |  | NO | INDSI ChildSub (NewKey) |
| INDSI_CompanySoldTo_DR | bigint |  | FK | SI | Company Sold To |
| INDSI_ConsReason_DR | bigint |  | FK | SI | Des REf ConsReason |
| INDSI_INCLB_DR | varchar |  | FK | NO | Des Ref to INCLB |
| INDSI_Qty | double |  |  | SI | Quantity |
| INDSI_Remarks | varchar |  |  | SI | Remarks |
| INDSI_RowId | varchar |  |  | NO | - |
| INDSI_Type | varchar |  |  | SI | Type |
| INDSI_UCost | double |  |  | SI | Unit Cost |
| Q01 | - |  |  | SI | Food and Nutrient Intake |
| Q02 | - |  |  | SI | Food and Nutrient Administration |
| Q02a | - |  |  | SI | Specify Other Food and Nutrient Administration |
| Q03 | - |  |  | SI | Medication and Herbal Supplement Use |
| Q03a | - |  |  | SI | Specify Other Medication & Supplement use |
| Q04 | - |  |  | SI | Knowledge/ Beliefs/ Attitudes/ Behaviour |
| Q04a | - |  |  | SI | Specify Other Knowledge, Beliefs etc |
| Q05 | - |  |  | SI | Factors Affecting Access to Food and Food / Nutrit... |
| Q05a | - |  |  | SI | Specfy Other Factors Affecting |
| Q06 | - |  |  | SI | Physical Activity and Function |
| Q06a | - |  |  | SI | Specify Other Physical Activity and Function |
| Q07 | - |  |  | SI | Nutrition-Focused Physical Findings |
| Q07a | - |  |  | SI | Specify Other Nutirition Focussed Physical Finding... |
| Q08 | - |  |  | SI | Biochemical Data, Medical Tests and Procedures |
| Q09 | - |  |  | SI | Height (cm) |
| Q10 | - |  |  | SI | Weight (kg) |
| Q11 | - |  |  | SI | Estimated Dry Wt: |
| Q12 | - |  |  | SI | BMI |
| Q13 | - |  |  | SI | Frame Size |
| Q14 | - |  |  | SI | Ideal Body Wt (kg) |
| Q15 | - |  |  | SI | % Ideal Body Wt |
| Q16 | - |  |  | SI | Adjusted Wt (kg) |
| Q17 | - |  |  | SI | Usual Body Wt (kg) |
| Q18 | - |  |  | SI | % Usual Body Wt |
| Q19 | - |  |  | SI | Height/ Length (cm) |
| Q20 | - |  |  | SI | Height/ Length Percentile |
| Q20a | - |  |  | SI | %ile |
| Q21 | - |  |  | SI | Weight (kg) |
| Q22 | - |  |  | SI | Weight Percentile |
| Q22a | - |  |  | SI | %ile |
| Q23 | - |  |  | SI | BMI |
| Q24 | - |  |  | SI | BMI Percentile |
| Q24a | - |  |  | SI | %ile |
| Q25 | - |  |  | SI | Weight for Length %ile |
| Q25a | - |  |  | SI | %ile |
| Q26 | - |  |  | SI | Ideal BMI |
| Q27 | - |  |  | SI | IBW |
| Q28 | - |  |  | SI | Anthropometric History |
| Q29 | - |  |  | SI | Estimated energy needs (Kcal) |
| Q29a | - |  |  | SI | Method for estimating energy needs |
| Q30 | - |  |  | SI | Estimated protein needs (gms/day) |
| Q30a | - |  |  | SI | Method for estimating protein needs |
| Q31 | - |  |  | SI | Fluid needs (ml) |
| Q31a | - |  |  | SI | Method for estimating fluid needs |
| Q32 | - |  |  | SI | Additional Information (if needed) |
| Q33 | - |  |  | SI | Nutritional Diagnosis / Problems |
| Q34 | - |  |  | SI | Nutrition Prescription |
| Q35 | - |  |  | SI | Food and/or Nutrient Delivery |
| Q36 | - |  |  | SI | Meals and Snacks |
| Q36a | - |  |  | SI | Specify Meals and Snacks |
| Q37 | - |  |  | SI | Enteral / Parenteral feeding |
| Q37a | - |  |  | SI | Specify Enteral feeding |
| Q38 | - |  |  | SI | Supplements |
| Q38a | - |  |  | SI | Specify Supplements |
| Q39 | - |  |  | SI | Vitamins/ Minerals Supplements |
| Q39a | - |  |  | SI | Specify Vitamins/ Minerals Supplements |
| Q40 | - |  |  | SI | Feeding assistance and environment |
| Q40a | - |  |  | SI | Specify Feeding assistance and environment |
| Q41 | - |  |  | SI | Changing in medication that can optimize patients’... |
| Q41a | - |  |  | SI | Specify Changing in medication that can optimize p... |
| Q42 | - |  |  | SI | Nutrition Education and Counseling |
| Q43 | - |  |  | SI | Coordination of Care |
| Q44 | - |  |  | SI | Additional intervention if needed |
| Q45 | - |  |  | SI | Monitoring and Evaluation |
| Q46 | - |  |  | SI | Recommendations |
| Q47 | - |  |  | SI | Level of Care |
| Q48 | - |  |  | SI | Signature |
| Q48UDt | - |  |  | SI | Signature Last Updated Date |
| Q48UTm | - |  |  | SI | Signature Last Updated Time |
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