# SQLUser.ARC_Alias

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALIAS_RowId | bigint | PK |  | NO | - |
| ALIAS_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ALIAS_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ALIAS_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ALIAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALIAS_CreatedDate | date |  |  | SI | Created Date |
| ALIAS_CreatedTime | time |  |  | SI | Created Time |
| ALIAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALIAS_DateFrom | date |  |  | SI | Date From |
| ALIAS_DateTo | date |  |  | SI | Date To |
| ALIAS_Desc | varchar |  |  | SI | Order Item/Set Description |
| ALIAS_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| ALIAS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ALIAS_OrderOnItsOwn | varchar |  |  | SI | Order On Its Own |
| ALIAS_OrderSubCat_DR | bigint |  | FK | SI | Des Ref OrderSubCat |
| ALIAS_Owner | varchar |  |  | SI | Owner |
| ALIAS_Row_Calc | varchar |  |  | SI | Row Calculated |
| ALIAS_Service | varchar |  |  | SI | Service |
| ALIAS_ServiceSet_DR | bigint |  | FK | SI | Des Ref ServiceSet |
| ALIAS_Source | varchar |  |  | SI | Source |
| ALIAS_Superset_DR | bigint |  | FK | SI | Des Ref Superset |
| ALIAS_Text | varchar |  |  | NO | Text |
| ALIAS_Type | varchar |  |  | SI | Type(ARCIM,ARCOS) |
| ALIAS_UpdatedDate | date |  |  | SI | Updated Date |
| ALIAS_UpdatedTime | time |  |  | SI | Updated Time |
| ALIAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ39DR | - |  |  | SI | Child Reference: Medicamentos |
| Q33Q1 | - |  |  | SI | Descripción |
| Q33Q2 | - |  |  | SI | Estado |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*