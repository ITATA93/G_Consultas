# SQLUser.SS_AuditTrailFields

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLD_ParRef | bigint | PK |  | NO | SS_AuditTrail Parent Reference |
| FLD_Childsub | double |  |  | NO | Childsub |
| FLD_FieldNo | varchar |  |  | SI | Field No |
| FLD_OldPairedValue | varchar |  |  | SI | Old Paired Value |
| FLD_OldStreamObjectValue | longvarchar |  |  | SI | Old Stream Object Value
object %Stream.GlobalChar... |
| FLD_OldStreamValue | longvarbinary |  |  | SI | Old WebSys Binary Stream Value |
| FLD_OldValue | varchar |  |  | SI | Old Value |
| FLD_PairedFieldName | varchar |  |  | SI | Paired Field Name |
| FLD_PairedValue | varchar |  |  | SI | New Paired Value |
| FLD_RowId | varchar |  |  | NO | - |
| FLD_Value | varchar |  |  | SI | New Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*