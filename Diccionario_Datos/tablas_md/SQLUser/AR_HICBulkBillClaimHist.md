# SQLUser.AR_HICBulkBillClaimHist

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLH_RowId | bigint | PK |  | NO | - |
| CLH_BatchInvoice_DR | bigint |  | FK | SI | Des Ref BatchInvoice |
| CLH_ClaimCertifiedDate | date |  |  | SI | Claim Certified Date |
| CLH_ClaimCertifiedInd | varchar |  |  | SI | Claim Certified Indicator |
| CLH_ClaimStatus | varchar |  |  | SI | ClaimStatus |
| CLH_DateSent | date |  |  | SI | DateSent |
| CLH_PayeeProviderNum | varchar |  |  | SI | Payee Provider Number |
| CLH_PmsClaimID | varchar |  |  | SI | PmsClaimID |
| CLH_ReturnCode | varchar |  |  | SI | ReturnCode |
| CLH_ReturnText | varchar |  |  | SI | ReturnText |
| CLH_ServProviderNum | varchar |  |  | SI | Service ProviderNum |
| CLH_ServiceTypeCode | varchar |  |  | SI | ServiceTypeCode |
| CLH_TimeSent | time |  |  | SI | Time Sent |
| CLH_Type | varchar |  |  | SI | Bulk Bill Type |
| CLH_User_DR | bigint |  | FK | SI | Des Ref User |
| ChildQ174DR | - |  |  | SI | Child Reference: Tipo de Tratamiento |
| Q169Q1 | - |  |  | SI | Inmunización que protege contra |
| Q169Q2 | - |  |  | SI | Número de Dosis |
| Q169Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*