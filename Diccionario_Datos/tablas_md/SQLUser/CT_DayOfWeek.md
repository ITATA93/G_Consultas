# SQLUser.CT_DayOfWeek

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOW_RowId | double | PK |  | NO | - |
| DOW_Checked | varchar |  |  | SI | Checked |
| DOW_CreatedDate | date |  |  | SI | Created Date |
| DOW_CreatedTime | time |  |  | SI | Created Time |
| DOW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOW_Day | double |  |  | NO | Day (1-Monday, .. 7-Sunday) |
| DOW_Name | varchar |  |  | SI | Name of the day (eg. Monday, Tuesday ,...) |
| DOW_NameTranslated | varchar |  |  | SI | Description Translated (Computed) |
| DOW_Sequence | double |  |  | SI | Sequence |
| DOW_SequenceTranslated | varchar |  |  | SI | Code Translated (Computed) |
| DOW_UpdatedDate | date |  |  | SI | Updated Date |
| DOW_UpdatedTime | time |  |  | SI | Updated Time |
| DOW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DOW_Weekend | varchar |  |  | SI | Weekend |
| Q03Q1 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*