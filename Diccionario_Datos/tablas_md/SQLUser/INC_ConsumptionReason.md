# SQLUser.INC_ConsumptionReason

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONR_RowId | bigint | PK |  | NO | - |
| CONR_Code | varchar |  |  | NO | Code |
| CONR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONR_CreatedDate | date |  |  | SI | Created Date |
| CONR_CreatedTime | time |  |  | SI | Created Time |
| CONR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONR_Desc | varchar |  |  | NO | Description |
| CONR_Owner | varchar |  |  | SI | Owner |
| CONR_UpdatedDate | date |  |  | SI | Updated Date |
| CONR_UpdatedTime | time |  |  | SI | Updated Time |
| CONR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ60DR | - |  |  | SI | Child Reference: Central intravenous tissue plasmi... |
| Q52Q1 | - |  |  | SI | Assessment date and time |
| Q52Q2 | - |  |  | SI | Assessment time |
| Q52Q3 | - |  |  | SI | Assessment care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*