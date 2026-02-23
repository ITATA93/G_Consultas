# SQLUser.PA_CodaExtract

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CODA_RowId | bigint | PK |  | NO | - |
| CODA_ADVAmt | double |  |  | SI | ADV Amt |
| CODA_ADVAmtDefined | double |  |  | SI | ADV Amt Defined |
| CODA_ADVAmtDiff | double |  |  | SI | ADV Amt Diff |
| CODA_ADVQty | double |  |  | SI | ADVQty |
| CODA_ADVTaxAmt | double |  |  | SI | ADVTaxAmt |
| CODA_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL |
| CODA_ARRecAlloc_DR | varchar |  | FK | SI | Des Ref ARRecAlloc |
| CODA_ARReceipt_DR | bigint |  | FK | SI | Des Ref ARReceipt |
| CODA_AccountPeriodCode | varchar |  |  | SI | AccountPeriodCode |
| CODA_AccountPeriond_DR | bigint |  | FK | SI | Des Ref AccountPeriond |
| CODA_AdmLocation | varchar |  |  | SI | Admlocation |
| CODA_Amount | double |  |  | SI | Amount |
| CODA_AmountDefined | double |  |  | SI | AmountDefined |
| CODA_AmtDiff | double |  |  | SI | AmtDiff |
| CODA_BillCharges_DR | varchar |  | FK | SI | Des Ref BillCharges |
| CODA_BillDateFrom | date |  |  | SI | BillDateFrom |
| CODA_BillDateTo | date |  |  | SI | BillDateTo |
| CODA_BillNo | varchar |  |  | SI | BillNo |
| CODA_DailyOrderDate | date |  |  | SI | DailyOrderDate |
| CODA_DebtorNumber | varchar |  |  | SI | DebtorNumber |
| CODA_DefinedPrice | double |  |  | SI | DefinedPrice |
| CODA_DiscountCode | varchar |  |  | SI | DiscountCode |
| CODA_EpisSubType | varchar |  |  | SI | EpisSubType |
| CODA_Episode | varchar |  |  | SI | Episode |
| CODA_EpisodeID_DR | bigint |  | FK | SI | Des Ref EpisodeID |
| CODA_ExtractBuild_DR | bigint |  | FK | SI | Des Ref CODA ExtractBuild |
| CODA_GL2 | varchar |  |  | SI | CODA_GL2 |
| CODA_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CODA_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| CODA_InvoiceDate | date |  |  | SI | InvoiceDate |
| CODA_ItemCat_DR | bigint |  | FK | SI | Des Ref ItemCat |
| CODA_ItemCategCode | varchar |  |  | SI | ItemCategCode |
| CODA_ItemDesc | varchar |  |  | SI | ItemDesc |
| CODA_Key1 | varchar |  |  | SI | Key1 |
| CODA_Key2 | varchar |  |  | SI | Key2 |
| CODA_Key3 | varchar |  |  | SI | Key3 |
| CODA_LocationCode | varchar |  |  | SI | LocationCode |
| CODA_Num1 | double |  |  | SI | Num1 |
| CODA_Num2 | double |  |  | SI | Num2 |
| CODA_OrdDate | date |  |  | SI | OrdDate |
| CODA_OrdItem_DR | varchar |  | FK | SI | Des Ref OrdItem_DR |
| CODA_OrdSttDate | date |  |  | SI | Ord SttDate |
| CODA_OrdSttdatePerCode | varchar |  |  | SI | OrdSttdatePerCode |
| CODA_OrderServiceDatePerID | bigint |  |  | SI | Des Ref OrderServiceDatePerID |
| CODA_PatientID_DR | bigint |  | FK | SI | Des Ref PatientID |
| CODA_PayorType | varchar |  |  | SI | PayorType |
| CODA_Qty | double |  |  | SI | Qty |
| CODA_ReceiptNumber | varchar |  |  | SI | ReceiptNumber |
| CODA_ReportAction | varchar |  |  | SI | ReportAction |
| CODA_SeqNo | varchar |  |  | SI | SeqNo |
| CODA_ServCat_DR | bigint |  | FK | SI | Des REf ServCat |
| CODA_ServiceCode | varchar |  |  | SI | ServiceCode |
| CODA_SundryDebtor_DR | bigint |  | FK | SI | Des Ref SundryDebtor |
| CODA_TaxAmt | double |  |  | SI | TaxAmt |
| CODA_Text1 | varchar |  |  | SI | Text1 |
| CODA_Text2 | varchar |  |  | SI | Text2 |
| CODA_Text3 | varchar |  |  | SI | Text3 |
| CODA_Transaction | varchar |  |  | SI | Transaction |
| CODA_UnitPrice | double |  |  | SI | UnitPrice |
| CODA_UnitPrice1 | double |  |  | SI | UnitPrice1 |
| CODA_WOReasonCode | varchar |  |  | SI | WOReasonCode |
| Q01 | - |  |  | SI | Result findings |
| Q01TxtOnly | - |  |  | SI | Result findings Plain Text Only |
| Q02 | - |  |  | SI | Additional result information |
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