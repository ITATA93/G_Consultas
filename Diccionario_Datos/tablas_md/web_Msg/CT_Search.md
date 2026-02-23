# web_Msg.CT_Search

**Schema:** web_Msg
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| RestrictionGroupList | varchar |  |  | SI | - |
| RestrictionLocationList | varchar |  |  | SI | - |
| RestrictionUserList | varchar |  |  | SI | - |
| SRCH_AccessReference | varchar |  |  | SI | Access Reference
Default to current logged in Use... |
| SRCH_AccessType | varchar |  |  | SI | Access Type 
Default to User |
| SRCH_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| SRCH_Component | bigint |  |  | SI | Component |
| SRCH_Context | varchar |  |  | SI | Context |
| SRCH_CreatedDate | date |  |  | SI | Created Date |
| SRCH_CreatedTime | time |  |  | SI | Created Time |
| SRCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SRCH_DPLAccessType | varchar |  |  | SI | Dynamic Patient List Access Type |
| SRCH_Default | varchar |  |  | SI | Default |
| SRCH_Desc | varchar |  |  | SI | Description
Required by User.CTSearch. |
| SRCH_ExtendedDesc | varchar |  |  | SI | Extended Description |
| SRCH_Favourite | varchar |  |  | SI | Favourite |
| SRCH_Function | varchar |  |  | SI | Function |
| SRCH_Owner | varchar |  |  | SI | Owner |
| SRCH_RowID | varchar |  |  | SI | - |
| SRCH_UpdatedDate | date |  |  | SI | Updated Date |
| SRCH_UpdatedTime | time |  |  | SI | Updated Time |
| SRCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*