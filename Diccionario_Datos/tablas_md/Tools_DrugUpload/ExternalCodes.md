# Tools_DrugUpload.ExternalCodes

**Schema:** Tools_DrugUpload
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ExtCode | varchar |  |  | NO | Code        = External Code        e.g. 36567 |
| ExtDateFrom | date |  |  | SI | Date From  |
| ExtDateTo | date |  |  | SI | Date To  |
| ExtSystem | varchar |  |  | NO | System      = External CodeSystem       RxNorm (go... |
| ExtTypeCode | varchar |  |  | NO | TypeCode    = External CodeType         IN (goes i... |
| ExtTypeDesc | varchar |  |  | NO | Desc        = External Type Desc        Ingredient |
| TrakCode | varchar |  |  | NO | Code depending on Type |
| TrakType | varchar |  |  | NO | TrakType that declaires which Type, can be PCK,ING... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*