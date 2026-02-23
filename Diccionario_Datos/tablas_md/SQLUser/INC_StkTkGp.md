# SQLUser.INC_StkTkGp

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCTG_RowId | bigint | PK |  | NO | - |
| ChildQ25DR | - |  |  | SI | Child Reference: Motivo de consulta según acompaña... |
| INCTG_Code | varchar |  |  | NO | Stock Take Group Code |
| INCTG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCTG_CreatedDate | date |  |  | SI | Created Date |
| INCTG_CreatedTime | time |  |  | SI | Created Time |
| INCTG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCTG_Desc | varchar |  |  | NO | Description |
| INCTG_Owner | varchar |  |  | SI | Owner |
| INCTG_UpdatedDate | date |  |  | SI | Updated Date |
| INCTG_UpdatedTime | time |  |  | SI | Updated Time |
| INCTG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q24Q1 | - |  |  | SI | Motivo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*