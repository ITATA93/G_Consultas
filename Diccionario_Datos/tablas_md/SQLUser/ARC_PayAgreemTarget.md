# SQLUser.ARC_PayAgreemTarget

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TARG_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| TARG_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| TARG_Amount | double |  |  | SI | Amount |
| TARG_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| TARG_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| TARG_Childsub | double |  |  | NO | Childsub |
| TARG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TARG_CreatedDate | date |  |  | SI | Created Date |
| TARG_CreatedTime | time |  |  | SI | Created Time |
| TARG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TARG_Qty | double |  |  | SI | Qty |
| TARG_RowId | varchar |  |  | NO | - |
| TARG_UpdatedDate | date |  |  | SI | Updated Date |
| TARG_UpdatedTime | time |  |  | SI | Updated Time |
| TARG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*