# SQLUser.ARC_InsTypeTarBillGrp

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BG_ParRef | varchar | PK |  | NO | ARC_InsTypeTariff Parent Reference |
| BG_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| BG_Childsub | double |  |  | NO | Childsub |
| BG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BG_CreatedDate | date |  |  | SI | Created Date |
| BG_CreatedTime | time |  |  | SI | Created Time |
| BG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BG_RowId | varchar |  |  | NO | - |
| BG_UpdatedDate | date |  |  | SI | Updated Date |
| BG_UpdatedTime | time |  |  | SI | Updated Time |
| BG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ251DR | - |  |  | SI | Child Reference: Evaluación Motivacional |
| Q250Q1 | - |  |  | SI | Evaluación |
| Q250Q2 | - |  |  | SI | Comentario (texto Libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*