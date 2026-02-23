# lab.CTBB_Location

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBL_RowID | varchar | PK |  | NO | - |
| BBL_Code | varchar |  |  | NO | Code |
| BBL_Controlled | varchar |  |  | SI | Controlled |
| BBL_Description | varchar |  |  | SI | Description |
| BBL_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*