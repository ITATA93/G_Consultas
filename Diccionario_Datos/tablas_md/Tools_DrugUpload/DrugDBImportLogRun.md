# Tools_DrugUpload.DrugDBImportLogRun

**Schema:** Tools_DrugUpload
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| guidMode | varchar |  |  | SI | - |
| key | varchar |  |  | SI | Key contains timestamp + type |
| keyINS | varchar |  |  | SI | Key for Inserts |
| keyRunType | varchar |  |  | SI | Single Character RunType (SQL optimization) |
| keyUPD | varchar |  |  | SI | Key for Updates |
| lvl | varchar |  |  | SI | contains the actual LogLevel (Filter) |
| plainkey | varchar |  |  | SI | run identifier without timestamp |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*