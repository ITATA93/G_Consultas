# SQLUser.AR_HICBulkBillClaimRep

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REP_ParRef | bigint | PK |  | NO | AR_HICBulkBillClaimHist Parent Reference |
| REP_Childsub | double |  |  | NO | Childsub |
| REP_Date | date |  |  | SI | Date |
| REP_PaymentAllocatedDate | date |  |  | SI | - |
| REP_PaymentAllocatedFlag | bit |  |  | SI | Payment allocated flag
This flag indicates if a p... |
| REP_PaymentAllocatedTime | time |  |  | SI | - |
| REP_PaymentReceipt_DR | bigint |  | FK | SI | Des Ref ARReceipts |
| REP_PaymentUnallocatedAmt | double |  |  | SI | - |
| REP_ReportType | varchar |  |  | SI | ReportType |
| REP_ReturnCode | varchar |  |  | SI | ReturnCode |
| REP_ReturnText | varchar |  |  | SI | ReturnText |
| REP_RowId | varchar |  |  | NO | - |
| REP_Time | time |  |  | SI | Time |
| REP_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*