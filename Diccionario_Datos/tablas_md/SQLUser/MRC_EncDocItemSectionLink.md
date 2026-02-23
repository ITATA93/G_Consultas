# SQLUser.MRC_EncDocItemSectionLink

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_RowID | bigint | PK |  | NO | - |
| ChildQ78DR | - |  |  | SI | Child Reference: Funcionamiento Cognitivo |
| LINK_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LINK_DateFrom | date |  |  | SI | Effective date for the record |
| LINK_DateTo | date |  |  | SI | Last day the record is active  |
| LINK_DocItemType_DR | bigint |  | FK | SI | Documentation Item Type |
| LINK_Owner | varchar |  |  | SI | Code Table Owner |
| LINK_Section_DR | bigint |  | FK | SI | Default Section |
| Q75Q1 | - |  |  | SI | Área |
| Q75Q2 | - |  |  | SI | Evaluación |
| Q75Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*