# websys.TMPStream

> Temporary Stream Storage

**Schema:** websys
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Temporary Stream Storage

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| SessionId | varchar |  |  | SI | stores the %session.SessionId (if it exists) |
| Text | longvarchar |  |  | SI | - |
| docData | longvarbinary |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*