# SQLUser.ARC_PayAgreemTheatreBand

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TB_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| TB_AnaestType_DR | bigint |  | FK | SI | Des Ref ORCAnaestType |
| TB_AssocClassif_DR | bigint |  | FK | SI | Des Ref AssocClassif |
| TB_Childsub | double |  |  | NO | Childsub |
| TB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TB_CreatedDate | date |  |  | SI | Created Date |
| TB_CreatedTime | time |  |  | SI | Created Time |
| TB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TB_Fee | double |  |  | SI | Fee |
| TB_RowId | varchar |  |  | NO | - |
| TB_UpdatedDate | date |  |  | SI | Updated Date |
| TB_UpdatedTime | time |  |  | SI | Updated Time |
| TB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*