# SQLUser.OE_AdmixAdditive

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_OrdAdmix Parent Reference |
| ITM_AdditiveVolume | double |  |  | SI | Additive Volume (mL) |
| ITM_Additive_DR | varchar |  | FK | NO | Additive |
| ITM_Carrier | varchar |  |  | SI | Carrier |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_ConcOverideReason_DR | bigint |  | FK | SI | Reason for Ordered Concentration Override |
| ITM_Date | date |  |  | SI | Date |
| ITM_Dose | double |  |  | SI | Dose |
| ITM_DoseUOM_DR | bigint |  | FK | SI | Dose UOM |
| ITM_DrgHistDesc_DR | varchar |  | FK | SI | Des Ref PHCDrgHistDesc |
| ITM_DrugDeliveryPerUOM | varchar |  |  | SI | Drug Delivery Rate Per UOM |
| ITM_DrugDeliveryRate | double |  |  | SI | Drug Delivery Rate |
| ITM_DrugDeliveryUOM_DR | bigint |  | FK | SI | Drug Delivery Rate UOM |
| ITM_GenericHistDesc_DR | varchar |  | FK | SI | Des Ref PHCGenericHistDesc |
| ITM_IngrInstruction_DR | bigint |  | FK | SI | Ingredient Instructions |
| ITM_MainItem | varchar |  |  | SI | Main Item |
| ITM_ManfConcOverideReason_DR | bigint |  | FK | SI | Reason for Manufactured Concentration Override |
| ITM_ManufacturedVolume | double |  |  | SI | Manufactured Volume (mL) |
| ITM_MaxDrugDeliveryRate | double |  |  | SI | Max Drug Delivery Rate |
| ITM_MinDrugDeliveryRate | double |  |  | SI | Min Drug Delivery Rate |
| ITM_OtherInstructions | varchar |  |  | SI | Other Instructions |
| ITM_PCALoadingDose | double |  |  | SI | PCA Loading Dose |
| ITM_PCALoadingDoseUOM_DR | bigint |  | FK | SI | PCA Loading Dose UOM |
| ITM_PerQuantity | double |  |  | SI | Quantity |
| ITM_PerUOM_DR | bigint |  | FK | SI | UOM |
| ITM_Percentage | double |  |  | SI | Percentage |
| ITM_Quantity | double |  |  | SI | Quantity |
| ITM_ReqPercentage | double |  |  | SI | Required Percentage |
| ITM_ResolvedAdditive_DR | varchar |  | FK | SI | Resolved Additive |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_Significant | varchar |  |  | SI | Significant |
| ITM_Time | time |  |  | SI | Time |
| ITM_TotalBagVolume | double |  |  | SI | Total Bag Volume (mL) |
| ITM_UOM_DR | bigint |  | FK | SI | UOM |
| Q01 | - |  |  | SI | Surgical VTE Risk |
| Q02 | - |  |  | SI | Recommended VTE prophylaxis |
| Q03 | - |  |  | SI | Recommended VTE prophylaxis Freetext 1 |
| Q04 | - |  |  | SI | Recommended VTE prophylaxis Freetext 2 |
| Q05 | - |  |  | SI | Recommended VTE prophylaxis Freetext 3 |
| Q06 | - |  |  | SI | Recommended VTE prophylaxis Freetext 4 |
| Q07 | - |  |  | SI | Recommended VTE prophylaxis Freetext 5 |
| Q08 | - |  |  | SI | Recommended VTE prophylaxis Freetext 6 |
| Q09 | - |  |  | SI | Recommended VTE prophylaxis Freetext 7 |
| Q10 | - |  |  | SI | Recommended VTE prophylaxis Freetext 8 |
| Q13 | - |  |  | SI | Medical VTE Risk |
| Q16 | - |  |  | SI | Are there any contraindications to chemical or mec... |
| Q17 | - |  |  | SI | Chemical |
| Q19 | - |  |  | SI | Note |
| Q20 | - |  |  | SI | Prophylaxis required? |
| Q21 | - |  |  | SI | 0 - 3: Low risk |
| Q22 | - |  |  | SI | >= 5: High risk |
| Q23 | - |  |  | SI | The Venous Thromboembolism Risk Assessment assesse... |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | HIGH |
| Q25a | - |  |  | SI | Hip arthroplasty |
| Q25b | - |  |  | SI | Knee arthroplasty |
| Q25c | - |  |  | SI | Major trauma |
| Q25d | - |  |  | SI | Hip fracture surgery |
| Q25e | - |  |  | SI | Other surgery with prior VTE and/or active cancer |
| Q25f | - |  |  | SI | Major surgery and age >40 yrs |
| Q25g | - |  |  | SI | (Major surgery refers to intra-abdominal surgery a... |
| Q25h | - |  |  | SI | Other risk (please state) |
| Q26 | - |  |  | SI | LOWER |
| Q26a | - |  |  | SI | All other surgery |
| Q26b | - |  |  | SI | All other surgery with additional VTE risk factors |
| Q27 | - |  |  | SI | HIGH |
| Q27a | - |  |  | SI | Ischaemic stroke |
| Q27b | - |  |  | SI | History of VTE |
| Q27c | - |  |  | SI | Active cancer |
| Q27e | - |  |  | SI | Decompensated heart failure |
| Q27f | - |  |  | SI | Acute or chronic lung disease |
| Q27g | - |  |  | SI | Acute inflammatory disease |
| Q27h | - |  |  | SI | Age > 60 years |
| Q27i | - |  |  | SI | Other risk (please state) |
| Q28 | - |  |  | SI | LOW |
| Q28a | - |  |  | SI | None of the above risk factors |
| Q43 | - |  |  | SI | Mechanical |
| Q44 | - |  |  | SI | Time |
| Q45 | - |  |  | SI | Score |
| Q46 | - |  |  | SI | Classification |
| Q47 | - |  |  | SI | 0 - 3 |
| Q48 | - |  |  | SI | Low risk |
| Q49 | - |  |  | SI | >= 5 |
| Q50 | - |  |  | SI | High risk |
| Q51 | - |  |  | SI | Comment |
| Q52 | - |  |  | SI | Comment |
| Q53 | - |  |  | SI | !!!These are examples and must be verified by a do... |
| Q54 | - |  |  | SI | Planned interventions |
| Q55 | - |  |  | SI | Score to be visualized and verified by the physici... |
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