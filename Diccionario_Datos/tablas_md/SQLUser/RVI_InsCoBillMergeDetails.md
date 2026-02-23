# SQLUser.RVI_InsCoBillMergeDetails

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MD_ParRef | bigint | PK |  | NO | RVI_InsCompanyBill Parent Reference |
| MD_ARCOS_DR | varchar |  | FK | SI | Des Ref to ARCOS |
| MD_AmtReceived | double |  |  | SI | Amt Received |
| MD_ChargeCode | varchar |  |  | SI | Charge Code |
| MD_Childsub | double |  |  | NO | Childsub |
| MD_CutAmt | double |  |  | SI | Cut Amt |
| MD_CutDays | double |  |  | SI | Cut Days |
| MD_CutQty | double |  |  | SI | Cut Qty |
| MD_DailyQty | double |  |  | SI | Daily Qty |
| MD_Date | date |  |  | SI | Date |
| MD_Days | double |  |  | SI | Days |
| MD_InsAmount | double |  |  | SI | Ins Amount |
| MD_MergeComment | varchar |  |  | SI | Merge Comment |
| MD_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| MD_ReasonForCut_DR | bigint |  | FK | SI | Des Ref Reason For Cut |
| MD_ReclaimAmt | double |  |  | SI | Reclaim Amt |
| MD_RowId | varchar |  |  | NO | - |
| MD_Status | varchar |  |  | SI | Status |
| MD_SubGroup_DR | varchar |  | FK | SI | Des Ref to BillSubGroup |
| MD_UnitPrice | double |  |  | SI | Unit Price |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*