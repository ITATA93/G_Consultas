# Tools_DrugUpload.ExternalIDEquiv

**Schema:** Tools_DrugUpload
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IDExt | varchar |  |  | NO | ID |
| IDRef | varchar |  |  | NO | ID reference (to be used if ID is requested) |
| IDRow | varchar |  |  | SI | Lose RowidRef from IDRef (e.g. RowId from GenericR... |
| Property | varchar |  |  | NO | Property that declaires which ID (e.g. "GenericRtF... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*