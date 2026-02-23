# SQLUser.ARC_Debtor

**Schema:** SQLUser
**Columnas:** 47
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCDR_RowId | bigint | PK |  | NO | - |
| ARCDR_Addressee | varchar |  |  | SI | Addressee |
| ARCDR_BatchTotal | double |  |  | SI | Total Receipts Per Batch (For Credit Card Co) |
| ARCDR_BillFmt | varchar |  |  | SI | Bill Format |
| ARCDR_BlackLstFlag | varchar |  |  | SI | BlackList Flag |
| ARCDR_CRAvail | double |  |  | SI | Credit Available  |
| ARCDR_CRLimit | double |  |  | SI | Credit Limit |
| ARCDR_CRTerm | double |  |  | SI | Credit Term |
| ARCDR_Cat_DR | bigint |  | FK | SI | not in use |
| ARCDR_ChrgExclFlag | varchar |  |  | SI | Charge Exclusion Flag |
| ARCDR_Code | varchar |  |  | NO | Debtor Code |
| ARCDR_CommCharge | double |  |  | SI | Commission Imposed By Hospital To Patient |
| ARCDR_CommPercent | double |  |  | SI | Commission Imposed by Card Co. To Hospital |
| ARCDR_CommType | varchar |  |  | SI | Commission Percent Calculation Type |
| ARCDR_CrRate_DR | varchar |  | FK | SI | not in use |
| ARCDR_CreatedDate | date |  |  | SI | Created Date |
| ARCDR_CreatedTime | time |  |  | SI | Created Time |
| ARCDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCDR_CtrlAcct_DR | varchar |  | FK | SI | Not Used Des Ref to ARCDA |
| ARCDR_Debtor_Origin_Info | varchar |  |  | SI | Debtor Origin Info |
| ARCDR_Designation | varchar |  |  | SI | Designation |
| ARCDR_EndDate | date |  |  | SI | End Date |
| ARCDR_IndepFlag | varchar |  |  | SI | Debtor created outside registration |
| ARCDR_Industry_DR | varchar |  | FK | SI | Not Used Des Ref to CTIND |
| ARCDR_IpChgType_DR | varchar |  | FK | SI | Des Ref to ARCCT(not in use) |
| ARCDR_LimitIP | varchar |  |  | SI | Days or Amt for Inpatient Limit Setup |
| ARCDR_LimitSDate | date |  |  | SI | Check Limit Start Date |
| ARCDR_LimitType | varchar |  |  | SI | Type of Limit Setup |
| ARCDR_Name | varchar |  |  | SI | Debtor Name |
| ARCDR_NoOfStaff | double |  |  | SI | No Of Staff |
| ARCDR_OpBillPolicy | varchar |  |  | SI | OutPatient Billing Policy |
| ARCDR_OpChgType_DR | varchar |  | FK | SI | Des Ref to ARCCT |
| ARCDR_Origin_ID | varchar |  |  | SI | Origin ID |
| ARCDR_Region_DR | bigint |  | FK | SI | Des Ref to CTRG |
| ARCDR_ServExcFlag | varchar |  |  | SI | Service Exclusion Flag |
| ARCDR_ShName | varchar |  |  | SI | Debtor Short Name |
| ARCDR_StartDate | date |  |  | SI | Start Date |
| ARCDR_StatementType | varchar |  |  | SI | Statement Type |
| ARCDR_UpdatedDate | date |  |  | SI | Updated Date |
| ARCDR_UpdatedTime | time |  |  | SI | Updated Time |
| ARCDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ39DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| Q35Q1 | - |  |  | SI | Percusión |
| Q35Q2 | - |  |  | SI | Auscultación |
| Q35Q3 | - |  |  | SI | Localización |
| Q35Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*