# websys.ComponentHistory

> "Stores the most recently used components (up to 50) for each source control user

**Schema:** websys
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

*Descripción original:* "Stores the most recently used components (up to 50) for each source control user

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ComponentId | varchar |  |  | NO | - |
| Timestamp | timestamp |  |  | NO | - |
| Username | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*