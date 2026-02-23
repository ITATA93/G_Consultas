# SQLUser.MRC_AreaCodeRestraint

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AREACR_RowId | bigint | PK |  | NO | - |
| AREACR_Code | varchar |  |  | NO | Code |
| AREACR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AREACR_CreatedDate | date |  |  | SI | Created Date |
| AREACR_CreatedTime | time |  |  | SI | Created Time |
| AREACR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AREACR_DateFrom | date |  |  | SI | DateFrom |
| AREACR_DateTo | date |  |  | SI | DateTo |
| AREACR_Desc | varchar |  |  | NO | Description |
| AREACR_Owner | varchar |  |  | SI | Owner |
| AREACR_UpdatedDate | date |  |  | SI | Updated Date |
| AREACR_UpdatedTime | time |  |  | SI | Updated Time |
| AREACR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ127DR | - |  |  | SI | Child Reference: Acciones preventivas |
| Q112Q1 | - |  |  | SI | Pulsos |
| Q112Q2 | - |  |  | SI | Lateralidad |
| Q112Q3 | - |  |  | SI | Hallazgos |
| Q112Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*