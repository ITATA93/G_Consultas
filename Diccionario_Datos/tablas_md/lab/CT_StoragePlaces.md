# lab.CT_StoragePlaces

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSTP_RowId | varchar | PK |  | NO | - |
| CTSTP_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTSTP_Code | varchar |  |  | NO | Code |
| CTSTP_Description | varchar |  |  | SI | Description |
| CTSTP_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*