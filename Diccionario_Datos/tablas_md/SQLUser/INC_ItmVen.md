# SQLUser.INC_ItmVen

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCV_ParRef | bigint | PK |  | NO | INC_Itm Parent Reference |
| INCV_APCVM_DR | bigint |  | FK | SI | Des Ref to APCVM |
| INCV_AgreedPrice | double |  |  | SI | Agreed Price |
| INCV_CTUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| INCV_CatalogueNo | varchar |  |  | SI | Catalogue No |
| INCV_Category | varchar |  |  | SI | Category |
| INCV_Childsub | double |  |  | NO | Childsub |
| INCV_Claimable | varchar |  |  | SI | Claimable |
| INCV_Code | varchar |  |  | SI | Code |
| INCV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCV_CreatedDate | date |  |  | SI | Created Date |
| INCV_CreatedTime | time |  |  | SI | Created Time |
| INCV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCV_Date | date |  |  | SI | Date Used |
| INCV_DateFrom | date |  |  | SI | Date From |
| INCV_DateTo | date |  |  | SI | Date To |
| INCV_IncludeGST | varchar |  |  | SI | Include GST |
| INCV_Lead_Time | double |  |  | SI | Order Lead Time |
| INCV_POType | varchar |  |  | SI | PO Type |
| INCV_Preferent | varchar |  |  | SI | Preferent |
| INCV_RebateCode | varchar |  |  | SI | Rebate Code |
| INCV_RowId | varchar |  |  | NO | - |
| INCV_ServiceTax_DR | bigint |  | FK | SI | Des Ref ServiceTax |
| INCV_StockBarCode | varchar |  |  | SI | StockBarCode |
| INCV_StockCode | varchar |  |  | SI | StockCode |
| INCV_StockDesc | varchar |  |  | SI | Stock Description |
| INCV_UnitCost | double |  |  | SI | Unit Cost |
| INCV_UpdatedDate | date |  |  | SI | Updated Date |
| INCV_UpdatedTime | time |  |  | SI | Updated Time |
| INCV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INCV_VendorContract_DR | bigint |  | FK | SI | Des Ref to INCVendorContract |
| Q01 | - |  |  | SI | Height |
| Q01ObsDR | - |  |  | SI | Height DR |
| Q02 | - |  |  | SI | Weight |
| Q02ObsDR | - |  |  | SI | Weight DR |
| Q03 | - |  |  | SI | Patient's protocol	 |
| Q04 | - |  |  | SI | Cycle number	 |
| Q05 | - |  |  | SI | Date of assessment	 |
| Q06 | - |  |  | SI | Dose reduction %	 |
| Q07 | - |  |  | SI | Is dose reduction permanent? 	 |
| Q08 | - |  |  | SI | Biochemistry / Tumour Markers	 |
| Q09 | - |  |  | SI | Bloods checked	 |
| Q10 | - |  |  | SI | Date bloods taken	 |
| Q11 | - |  |  | SI | Date of chemotherapy	 |
| Q12 | - |  |  | SI | Other test results	 |
| Q13 | - |  |  | SI | Grade - Please select the appropriate item in each... |
| Q14 | - |  |  | SI | Performance status	 |
| Q15 | - |  |  | SI | Nausea	 |
| Q16 | - |  |  | SI | Vomiting	 |
| Q17 | - |  |  | SI | Diarrhoea	 |
| Q18 | - |  |  | SI | Skin rash	 |
| Q19 | - |  |  | SI | Neurosensory	 |
| Q20 | - |  |  | SI | Assessment findings: 	 |
| Q21 | - |  |  | SI | Bloods reviewed and chemotherapy to proceed? 	 |
| Q22 | - |  |  | SI | Take home medications ordered |
| Q23 | - |  |  | SI | Method of next appointment	 |
| Q24 | - |  |  | SI | Is end of treatment letter needed? If last cycle	 |
| Q25 | - |  |  | SI | Toxicity assessment completed?	 |
| Q27 | - |  |  | SI | Confirmed patient received the pre medication if a... |
| Q28 | - |  |  | SI | Secured patient and family education |
| Q29 | - |  |  | SI | Secured informed consent for every new protocol |
| Q30 | - |  |  | SI | Double checking of dose calculation and orders ind... |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
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