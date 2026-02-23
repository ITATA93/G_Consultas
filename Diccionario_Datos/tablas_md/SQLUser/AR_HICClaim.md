# SQLUser.AR_HICClaim

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HICC_RowID | bigint | PK |  | NO | - |
| ChildQ174DR | - |  |  | SI | Child Reference: Tipo de Tratamiento |
| HICC_Adm_DR | bigint |  | FK | SI | Episode |
| HICC_Batch_DR | bigint |  | FK | SI | Batch of the claim |
| HICC_CurPatFirstName | varchar |  |  | SI | CurrentPatientFirstName |
| HICC_CurPatMedicareCardNum | varchar |  |  | SI | Current Patient Medicare Card Number |
| HICC_CurPatReferenceNum | varchar |  |  | SI | Current Patient Reference Num |
| HICC_ErrorDetails | varchar |  |  | SI | Error details 
TrakCare internal error details |
| HICC_FundStatusCode | varchar |  |  | SI | Funds PVF assessment result code. |
| HICC_ManualSubmission | varchar |  |  | SI | Manual Submission |
| HICC_MedicareStatusCode | varchar |  |  | SI | Medicare Status Code |
| HICC_PatientBill_DR | bigint |  | FK | SI | Patient bill of the claim |
| HICC_ProcessStatusCode | varchar |  |  | SI | Code to indicate the processing status of the clai... |
| HICC_StatusCode | varchar |  |  | SI | HIC Status Code
1716 - the Hub is acknowledging t... |
| HICC_StoreFoward | bit |  |  | SI | Store Forward Claim |
| HICC_TransactionID | varchar |  |  | SI | Transaction ID
A unique identifier maintained thr... |
| HICC_TransmissionDate | date |  |  | SI | Date of transmission |
| HICC_TransmissionTime | time |  |  | SI | Time of transmission |
| HICC_TransmissionUser_DR | bigint |  | FK | SI | Transmitting user |
| HICC_Type | varchar |  |  | SI | Claim Type |
| IHC_ReportStatusCode | varchar |  |  | SI | Code to indicate the report status
PROCESSING 
I... |
| Q169Q1 | - |  |  | SI | Inmunización que protege contra |
| Q169Q2 | - |  |  | SI | Número de Dosis |
| Q169Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*