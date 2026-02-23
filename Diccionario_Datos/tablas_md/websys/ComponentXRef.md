# websys.ComponentXRef

> Generate rountines based on components.

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Generate rountines based on components.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| App | varchar |  |  | SI | - |
| ComponentId | varchar |  |  | SI | - |
| Context | varchar |  |  | SI | - |
| Dirty | bit |  |  | SI | Used to flag if the defining params have changed (... |
| LangId | varchar |  |  | SI | - |
| LastUpdateDate | date |  |  | SI | - |
| LastUpdateTime | time |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*