# SQLUser.ARC_InsTypeTarAdjBillSub

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BS_ParRef | varchar | PK |  | NO | ARC_InsTypeTarAdjust Parent Reference |
| BS_Adjustment | double |  |  | SI | Adjustment |
| BS_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| BS_Childsub | double |  |  | NO | Childsub |
| BS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BS_CreatedDate | date |  |  | SI | Created Date |
| BS_CreatedTime | time |  |  | SI | Created Time |
| BS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BS_DateFrom | date |  |  | SI | Date From |
| BS_DateTo | date |  |  | SI | Date To |
| BS_MultFactor | double |  |  | SI | Multiplier Factor |
| BS_RowId | varchar |  |  | NO | - |
| BS_Type | varchar |  |  | SI | Type |
| BS_UpdatedDate | date |  |  | SI | Updated Date |
| BS_UpdatedTime | time |  |  | SI | Updated Time |
| BS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ13DR | - |  |  | SI | Child Reference: Conductas desadaptativas |
| Q39Q1 | - |  |  | SI | Área |
| Q39Q2 | - |  |  | SI | Orientación |
| Q39Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*