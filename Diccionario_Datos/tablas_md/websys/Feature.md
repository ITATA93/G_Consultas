# websys.Feature

> Class for store and manage Features

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Class for store and manage Features

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | NO | Code |
| DateFrom | date |  |  | SI | Data From |
| DateTo | date |  |  | SI | Date To |
| ExternalReferences | varchar |  |  | SI | List of reference numbers (comma delimited string)... |
| LongDesc | varchar |  |  | SI | Long description for the feature |
| ServerOnly | varchar |  |  | SI | Indicates if feature parameters should be exposed ... |
| ShortDesc | varchar |  |  | SI | Short description for the feature (title) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*