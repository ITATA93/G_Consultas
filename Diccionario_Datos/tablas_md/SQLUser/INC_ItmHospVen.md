# SQLUser.INC_ItmHospVen

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VEN_ParRef | varchar | PK |  | NO | INC_ItmHosp Parent Reference |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Sex |
| Q03 | - |  |  | SI | Congestive heart failure history	 |
| Q04 | - |  |  | SI | Hypertension history	 |
| Q05 | - |  |  | SI | Stroke / Transient Ischemic Attack (TIA) / Thrombo... |
| Q06 | - |  |  | SI | Vascular disease history	 |
| Q07 | - |  |  | SI | Diabetes history	 |
| Q08 | - |  |  | SI | Stroke or Thromboembolism (TE) / 100 years at risk... |
| Q09 | - |  |  | SI | STROKE OR TE/100 PERSON-YEARS |
| Q10 | - |  |  | SI | Score	 |
| Q11 | - |  |  | SI | Ischemic Stroke	 |
| Q12 | - |  |  | SI | Stroke / TIA / TE |
| Q13 | - |  |  | SI | 0 |
| Q14 | - |  |  | SI | 1 |
| Q15 | - |  |  | SI | 2 |
| Q16 | - |  |  | SI | 3 |
| Q17 | - |  |  | SI | 4 |
| Q18 | - |  |  | SI | 5 |
| Q19 | - |  |  | SI | 6 |
| Q20 | - |  |  | SI | 7 |
| Q21 | - |  |  | SI | 8 |
| Q22 | - |  |  | SI | 9 |
| Q23 | - |  |  | SI | 0.2	 |
| Q24 | - |  |  | SI | 0.6 |
| Q25 | - |  |  | SI | 2.2 |
| Q26 | - |  |  | SI | 3.2	 |
| Q27 | - |  |  | SI | 4.8 |
| Q28 | - |  |  | SI | 7.2 |
| Q29 | - |  |  | SI | 9.7 |
| Q30 | - |  |  | SI | 11.2	 |
| Q31 | - |  |  | SI | 10.8	 |
| Q32 | - |  |  | SI | 12.23	 |
| Q33 | - |  |  | SI | 0.3 |
| Q34 | - |  |  | SI | 0.9 |
| Q35 | - |  |  | SI | 2.9 |
| Q36 | - |  |  | SI | 4.6 |
| Q37 | - |  |  | SI | 6.7 |
| Q38 | - |  |  | SI | 10.0 |
| Q39 | - |  |  | SI | 13.6 |
| Q40 | - |  |  | SI | 15.7 |
| Q41 | - |  |  | SI | 15.2 |
| Q42 | - |  |  | SI | 17.4 |
| Q43 | - |  |  | SI | Score |
| Q44 | - |  |  | SI | Classification	 |
| Q45 | - |  |  | SI | 0 |
| Q46 | - |  |  | SI | “Low” risk and may not require anticoagulation |
| Q47 | - |  |  | SI | 1 |
| Q48 | - |  |  | SI | “Low-moderate” risk and should consider anti-plate... |
| Q49 | - |  |  | SI | ≥2 |
| Q50 | - |  |  | SI | “Moderate-high” risk and should otherwise be an an... |
| Q51 | - |  |  | SI | The CHA2DS2-VASc score is one of several risk stra... |
| Q52 | - |  |  | SI | 1 year risk of a Thromboembolism (TE) event in a n... |
| Q53 | - |  |  | SI | 0: “Low” risk and may not require anticoagulation |
| Q54 | - |  |  | SI | 1: “Low-moderate” risk and should consider anti-pl... |
| Q55 | - |  |  | SI | >=2: “Moderate-high” risk and should otherwise be ... |
| Q56 | - |  |  | SI | Date |
| Q57 | - |  |  | SI | Time |
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
| VEN_APCVM_DR | bigint |  | FK | SI | Des Ref to APCVM |
| VEN_AgreedPrice | double |  |  | SI | Agreed Price |
| VEN_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| VEN_Category | varchar |  |  | SI | Category |
| VEN_Childsub | double |  |  | NO | Childsub |
| VEN_Claimable | varchar |  |  | SI | Claimable |
| VEN_Code | varchar |  |  | SI | Code |
| VEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VEN_CreatedDate | date |  |  | SI | Created Date |
| VEN_CreatedTime | time |  |  | SI | Created Time |
| VEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VEN_Date | date |  |  | SI | Date Used |
| VEN_DateFrom | date |  |  | SI | Date From |
| VEN_DateTo | date |  |  | SI | Date To |
| VEN_IncludeGST | varchar |  |  | SI | Include GST |
| VEN_Lead_Time | double |  |  | SI | Order Lead Time |
| VEN_Preferent | varchar |  |  | SI | Preferent |
| VEN_RowId | varchar |  |  | NO | - |
| VEN_ServiceTax_DR | bigint |  | FK | SI | Des Ref ServiceTax |
| VEN_StockCode | varchar |  |  | SI | StockCode |
| VEN_StockDesc | varchar |  |  | SI | Stock Description |
| VEN_UnitCost | double |  |  | SI | Unit Cost |
| VEN_UpdatedDate | date |  |  | SI | Updated Date |
| VEN_UpdatedTime | time |  |  | SI | Updated Time |
| VEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| VEN_VendorContract_DR | bigint |  | FK | SI | Des Ref to INCVendorContract |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*