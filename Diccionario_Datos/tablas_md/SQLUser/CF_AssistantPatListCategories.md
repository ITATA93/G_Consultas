# SQLUser.CF_AssistantPatListCategories

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APLC_RowID | bigint | PK |  | NO | - |
| APLC_Code | varchar |  |  | NO | Code |
| APLC_CreatedDate | date |  |  | SI | Created Date |
| APLC_CreatedTime | time |  |  | SI | Created Time |
| APLC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APLC_DateFrom | date |  |  | NO | Date From |
| APLC_DateTo | date |  |  | SI | Date To |
| APLC_Desc | varchar |  |  | NO | Description |
| APLC_Owner | varchar |  |  | SI | Owner |
| APLC_UpdatedDate | date |  |  | SI | Updated Date |
| APLC_UpdatedTime | time |  |  | SI | Updated Time |
| APLC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ05DR | - |  |  | SI | Child Reference: AREA PSICOSOCIAL |
| Q02Q1 | - |  |  | SI | Metas |
| Q02Q2 | - |  |  | SI | Logro |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*