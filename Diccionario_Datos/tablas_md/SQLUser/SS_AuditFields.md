# SQLUser.SS_AuditFields

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLD_ParRef | bigint | PK |  | NO | SS_Audit Parent Reference |
| FLD_Childsub | double |  |  | NO | Childsub |
| FLD_FieldNumber | varchar |  |  | SI | Field Number |
| FLD_NewValue | varchar |  |  | SI | New Value |
| FLD_OldValue | varchar |  |  | SI | Old Value |
| FLD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*