# SQLUser.AR_HICClaimRep

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CR_RowID | bigint | PK |  | NO | - |
| CR_Claim_DR | bigint |  | FK | SI | The claim the report is for |
| CR_PaymentAllocatedDate | date |  |  | SI | - |
| CR_PaymentAllocatedFlag | bit |  |  | SI | Payment allocated flag
This flag indicates if a p... |
| CR_PaymentAllocatedTime | time |  |  | SI | - |
| CR_PaymentReceipt_DR | bigint |  | FK | SI | - |
| CR_PaymentUnallocatedAmt | double |  |  | SI | - |
| CR_ReportType | varchar |  |  | SI | Report type
Payment or processing
Standard type:... |
| CR_RetrievalDate | date |  |  | SI | Date report retrieved |
| CR_RetrievalTime | time |  |  | SI | Time report retrieved |
| CR_RetrievalUser_DR | bigint |  | FK | SI | The user that retrieved the report
Blank if retri... |
| CR_StatusCode | varchar |  |  | SI | HIC Status Code |
| CR_TransactionID | varchar |  |  | SI | Transaction ID
A unique identifier maintained thr... |
| ChildQ185DR | - |  |  | SI | Child Reference: Tipo de Tratamiento |
| Q19aQ1 | - |  |  | SI | Listado de Dispositivos |
| Q19aQ2 | - |  |  | SI | Fecha instalación |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*