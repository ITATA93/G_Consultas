# websys.GridTemplate

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| GridCSSClass | varchar |  |  | SI | - |
| GridCode | varchar |  |  | SI | - |
| HeaderMethod | varchar |  |  | SI | allow alternative HeaderMethod name |
| HeaderParameters | varchar |  |  | SI | - |
| QueryClass | varchar |  |  | SI | Name of class contining Query |
| QueryMethod | varchar |  |  | SI | Query is expected to return one row per grid row. ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*