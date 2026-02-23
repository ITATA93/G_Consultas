# SQLUser.SS_ProfileARCOSRestLink

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSRLINK_RowId | bigint | PK |  | NO | - |
| OSRLINK_ARCOSRestProfile_DR | bigint |  | FK | SI | Des Ref SSARCOSRestProfile |
| OSRLINK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OSRLINK_Owner | varchar |  |  | SI | Owner |
| OSRLINK_Profile_DR | bigint |  | FK | SI | Des Ref SSProfile |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*