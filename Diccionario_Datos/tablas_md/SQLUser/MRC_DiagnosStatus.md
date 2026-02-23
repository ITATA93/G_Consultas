# SQLUser.MRC_DiagnosStatus

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSTAT_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Patrón de consumo |
| DSTAT_Code | varchar |  |  | NO | Code |
| DSTAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSTAT_CreatedDate | date |  |  | SI | Created Date |
| DSTAT_CreatedTime | time |  |  | SI | Created Time |
| DSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSTAT_Desc | varchar |  |  | NO | Description |
| DSTAT_Owner | varchar |  |  | SI | Owner |
| DSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| DSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| DSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q82Q1 | - |  |  | SI | Evaluación |
| Q82Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*