# SQLUser.RVI_InsCoBillChargesSurch

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUR_ParRef | varchar | PK |  | NO | RVI_InsCoBillCharges Parent Reference |
| SUR_Childsub | double |  |  | NO | Childsub |
| SUR_Desc | varchar |  |  | SI | Description |
| SUR_GovtShare | double |  |  | SI | Govt Share |
| SUR_HandicappedShare | double |  |  | SI | Handicapped Share |
| SUR_InsCoShare | double |  |  | SI | Ins Co Share |
| SUR_NoDays | double |  |  | SI | No of Days |
| SUR_PatientShare | double |  |  | SI | Patient Share |
| SUR_QtyDay | double |  |  | SI | Qty/Day |
| SUR_RowId | varchar |  |  | NO | - |
| SUR_SurchDiscountType | double |  |  | SI | Surcharge Discount Type |
| SUR_SurchargeCode_DR | bigint |  | FK | SI | Des Ref Surcharge Code |
| SUR_TotalAmt | double |  |  | SI | Total Amt |
| SUR_UnitPrice | double |  |  | SI | Unit Price |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*