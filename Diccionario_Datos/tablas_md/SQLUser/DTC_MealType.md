# SQLUser.DTC_MealType

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEALT_RowId | bigint | PK |  | NO | - |
| ChildQ40DR | - |  |  | SI | Child Reference: Care provider(s) contributing to ... |
| MEALT_Code | varchar |  |  | NO | Code |
| MEALT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MEALT_Color | varchar |  |  | SI | Color |
| MEALT_CreatedDate | date |  |  | SI | Created Date |
| MEALT_CreatedTime | time |  |  | SI | Created Time |
| MEALT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEALT_CutOffBulkTime | time |  |  | SI | CutOffBulkTime |
| MEALT_CutOffTime | time |  |  | SI | Cut Off Time |
| MEALT_DateFrom | date |  |  | SI | DateFrom |
| MEALT_DateTo | date |  |  | SI | DateTo |
| MEALT_Desc | varchar |  |  | NO | Description |
| MEALT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| MEALT_Location_DR | bigint |  | FK | SI | Des Ref Location |
| MEALT_MainMeal | varchar |  |  | SI | Main Meal |
| MEALT_Owner | varchar |  |  | SI | Owner |
| MEALT_Time | time |  |  | SI | Meal Time |
| MEALT_UpdatedDate | date |  |  | SI | Updated Date |
| MEALT_UpdatedTime | time |  |  | SI | Updated Time |
| MEALT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Level of care for birth |
| Q04 | - |  |  | SI | Transfer location |
| Q05 | - |  |  | SI | Planned gestation at transfer |
| Q06 | - |  |  | SI | Planned gestation at transfer |
| Q07 | - |  |  | SI | Planned gestation at transfer (days) |
| Q08 | - |  |  | SI | weeks |
| Q09 | - |  |  | SI | days |
| Q10 | - |  |  | SI | Planned method of birth |
| Q11 | - |  |  | SI | Planned onset of labour |
| Q12 | - |  |  | SI | Recommended Prostaglandin E2 dose for induction of... |
| Q13 | - |  |  | SI | Planned onset of labour notes |
| Q14 | - |  |  | SI | Recommended intervention(s) and monitoring |
| Q15 | - |  |  | SI | Recommended anaesthetic technique |
| Q16 | - |  |  | SI | Recommendations for 1st stage |
| Q17 | - |  |  | SI | Special circumstances |
| Q18 | - |  |  | SI | Is patient on low molecular weight heparin |
| Q19 | - |  |  | SI | Inform ANAESTHETIST (epidural can be administered ... |
| Q20 | - |  |  | SI | Oxytocin augmentation |
| Q21 | - |  |  | SI | Preterm labour tocolysis notes |
| Q22 | - |  |  | SI | Preterm labour tocolysis |
| Q23 | - |  |  | SI | Oxytocin augmentation notes |
| Q24 | - |  |  | SI | Recommendations for 2nd stage |
| Q25 | - |  |  | SI | Assist if not birthed in |
| Q26 | - |  |  | SI | minutes |
| Q27 | - |  |  | SI | Recommendations for 3rd stage |
| Q28 | - |  |  | SI | Recommended oxytocin protocol |
| Q29 | - |  |  | SI | Oxytocin protocol notes |
| Q30 | - |  |  | SI | Special consideration(s) in post partum haemorrhag... |
| Q31 | - |  |  | SI | Recommendation(s) for post birth |
| Q32 | - |  |  | SI | LMWH duration |
| Q33 | - |  |  | SI | days for post birth |
| Q34 | - |  |  | SI | Postnatal stay for |
| Q35 | - |  |  | SI | days |
| Q36 | - |  |  | SI | Cardiac review required |
| Q37 | - |  |  | SI | weeks post-discharge |
| Q38 | - |  |  | SI | Contraceptive method notes |
| Q39 | - |  |  | SI | Notes |
| Q41 | - |  |  | SI | Onset of Labour |
| Q42 | - |  |  | SI | Intervention(s) and Monitoring |
| Q43 | - |  |  | SI | Anaesthesia |
| Q44 | - |  |  | SI | First Stage |
| Q45 | - |  |  | SI | Special Circumstances |
| Q46 | - |  |  | SI | Second Stage |
| Q47 | - |  |  | SI | Third Stage |
| Q48 | - |  |  | SI | Post Partum |
| Q49 | - |  |  | SI | Care provider(s) contributing to plan |
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