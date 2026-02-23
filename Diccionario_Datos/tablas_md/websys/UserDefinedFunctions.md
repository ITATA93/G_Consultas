# websys.UserDefinedFunctions

> "User defined functions which are called in response to websys events

**Schema:** websys
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "User defined functions which are called in response to websys events

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CacheScript | varchar |  |  | NO | - |
| ClassName | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| Event | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*