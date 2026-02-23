# SQLUser.ARC_InsTypeTarAdjust

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_ParRef | varchar | PK |  | NO | ARC_InsTypeTariff Parent Reference |
| ADJ_Adjustment | double |  |  | SI | Adjustment (%) |
| ADJ_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| ADJ_Childsub | double |  |  | NO | Childsub |
| ADJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADJ_CreatedDate | date |  |  | SI | Created Date |
| ADJ_CreatedTime | time |  |  | SI | Created Time |
| ADJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADJ_DateFrom | date |  |  | NO | Date From |
| ADJ_DateTo | date |  |  | SI | Date To |
| ADJ_MaxAmtCovered | double |  |  | SI | Max Amt Covered |
| ADJ_MultFactor | double |  |  | SI | Multiplier Factor |
| ADJ_PayorShare | double |  |  | SI | Payor Share |
| ADJ_RowId | varchar |  |  | NO | - |
| ADJ_Type | varchar |  |  | SI | Type |
| ADJ_UpdatedDate | date |  |  | SI | Updated Date |
| ADJ_UpdatedTime | time |  |  | SI | Updated Time |
| ADJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ250DR | - |  |  | SI | Child Reference: Sexualidad |
| Q84Q1 | - |  |  | SI | Características |
| Q84Q2 | - |  |  | SI | Evaluación |
| Q84Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*