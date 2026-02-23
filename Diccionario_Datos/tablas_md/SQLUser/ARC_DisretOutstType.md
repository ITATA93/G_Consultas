# SQLUser.ARC_DisretOutstType

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOUTS_RowId | bigint | PK |  | NO | - |
| ChildQ52DR | - |  |  | SI | Child Reference: Abdomen Alterado |
| DOUTS_Code | varchar |  |  | NO | Code |
| DOUTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOUTS_CreatedDate | date |  |  | SI | Created Date |
| DOUTS_CreatedTime | time |  |  | SI | Created Time |
| DOUTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOUTS_CreditAdjDefault | varchar |  |  | SI | Credit Adjustment Default |
| DOUTS_DateFrom | date |  |  | SI | Date From |
| DOUTS_DateTo | date |  |  | SI | Date To |
| DOUTS_Desc | varchar |  |  | NO | Description |
| DOUTS_Owner | varchar |  |  | SI | Owner |
| DOUTS_Type | varchar |  |  | SI | Type |
| DOUTS_UpdatedDate | date |  |  | SI | Updated Date |
| DOUTS_UpdatedTime | time |  |  | SI | Updated Time |
| DOUTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q42Q1 | - |  |  | SI | Ritmo |
| Q42Q2 | - |  |  | SI | Ruidos |
| Q42Q3 | - |  |  | SI | Soplos |
| Q42Q4 | - |  |  | SI | Grado (soplos) |
| Q42Q5 | - |  |  | SI | Ubicación |
| Q42Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*