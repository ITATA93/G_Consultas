# SQLUser.RVB_InsurBatchClaim

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLM_ParRef | bigint | PK |  | NO | RVB_InsurBatch Parent Reference |
| CLM_BillingFlag_DR | bigint |  | FK | SI | Des Ref BillingFlag |
| CLM_Childsub | double |  |  | NO | Childsub |
| CLM_ClaimNo | varchar |  |  | SI | Claim No |
| CLM_OverPaidFlag | varchar |  |  | SI | OverPaid Flag |
| CLM_OverPaidNotifID | varchar |  |  | SI | OverPaid NotifID |
| CLM_RVIInsCoBill_DR | bigint |  | FK | SI | Des Ref RVIInsCoBill |
| CLM_ReadOnly | varchar |  |  | SI | Read Only |
| CLM_ReasonForReject_DR | bigint |  | FK | SI | Des REf ReasonForReject_DR |
| CLM_ReclaimFlag | varchar |  |  | SI | Reclaim Flag |
| CLM_RowId | varchar |  |  | NO | - |
| CLM_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*