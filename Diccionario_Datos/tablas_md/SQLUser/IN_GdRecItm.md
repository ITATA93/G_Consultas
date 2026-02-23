# SQLUser.IN_GdRecItm

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGRI_INGR_ParRef | bigint | PK |  | NO | Des ref To INGR |
| INGRI_BNetAmt | double |  |  | SI | Base Net Amount  |
| INGRI_BatchNo | varchar |  |  | SI | Batch No |
| INGRI_CTLOC_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| INGRI_CTUOM_DR | bigint |  | FK | NO | UOM |
| INGRI_ChildSub | numeric |  |  | NO | INGRI Childsub (New Key) |
| INGRI_CommItems_DR | bigint |  | FK | SI | Des Ref CommItems |
| INGRI_Disc | double |  |  | SI | Discount Rate |
| INGRI_ExpDate | date |  |  | SI | Expiry Date |
| INGRI_GrossAmt | double |  |  | NO | Gross Amount |
| INGRI_HandChargeShare | double |  |  | SI | Share of Handling Charges |
| INGRI_INCGR_DR | bigint |  | FK | SI | Des Ref to INC_GdRecType |
| INGRI_INCLB_DR | varchar |  | FK | NO | Des Ref To INCLB |
| INGRI_INPOI_DR | varchar |  | FK | SI | Des Ref INPOI |
| INGRI_InvoiceNumber | varchar |  |  | SI | Invoice Number |
| INGRI_Margin | double |  |  | SI | Margin |
| INGRI_NetAmt | double |  |  | SI | Net Amount in foreign currency |
| INGRI_OverallDiscShare | double |  |  | SI | Share of the Overall Discount |
| INGRI_PreVATAmt | double |  |  | SI | PreVATAmt |
| INGRI_RecQty | double |  |  | NO | Receiving Quantity |
| INGRI_Remarks | varchar |  |  | SI | Remarks |
| INGRI_RowId | varchar |  |  | NO | - |
| INGRI_ServiceTax_DR | bigint |  | FK | SI | Des Ref To Service Tax |
| INGRI_StkDesc | varchar |  |  | NO | Stock Description |
| INGRI_StorageBin_DR | varchar |  | FK | SI | Des Ref CTLocStorageBin |
| INGRI_TaxAmount | double |  |  | SI | Tax Amount |
| INGRI_UnitCost | double |  |  | NO | UnitCost |
| Q1 | - |  |  | SI | Respiratory rate |
| Q10 | - |  |  | SI | Score 0 |
| Q11 | - |  |  | SI | Score 1 |
| Q12 | - |  |  | SI | Score 2 |
| Q13 | - |  |  | SI | The Clinical Respiratory Score (CRS, Nayani 2018) ... |
| Q14 | - |  |  | SI | 1. Crabtree EA, Mariscalco MM, Hesselgrave J, et a... |
| Q15 | - |  |  | SI | 2. Nayani K, Naeem R, Munir O, et al. The clinical... |
| Q2 | - |  |  | SI | Auscultation |
| Q3 | - |  |  | SI | Use of accessory muscles |
| Q4 | - |  |  | SI | Mental status |
| Q5 | - |  |  | SI | Room air spO2 |
| Q6 | - |  |  | SI | Color |
| Q7 | - |  |  | SI | Date |
| Q8 | - |  |  | SI | Time |
| Q9 | - |  |  | SI | Assess |
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