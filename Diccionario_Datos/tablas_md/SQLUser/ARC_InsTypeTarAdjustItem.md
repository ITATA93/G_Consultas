# SQLUser.ARC_InsTypeTarAdjustItem

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | ARC_InsTypeTarAdjBillSub Parent Reference |
| ChildQ55DR | - |  |  | SI | Child Reference: Piel |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_Adjustment | double |  |  | SI | Adjustment |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_DateFrom | date |  |  | SI | Date From |
| ITM_DateTo | date |  |  | SI | Date To |
| ITM_MultFactor | double |  |  | SI | Multiplier Factor |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_Type | varchar |  |  | SI | Type |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q13Q1 | - |  |  | SI | Área |
| Q13Q2 | - |  |  | SI | Comentarios (Texto libre): |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*