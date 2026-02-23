# SQLUser.SS_SingleSignOnActivity

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOA_RowId | bigint | PK |  | NO | - |
| SSOA_Code | varchar |  |  | NO | Code |
| SSOA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSOA_DateFrom | date |  |  | SI | Date From |
| SSOA_DateTo | date |  |  | SI | Date To |
| SSOA_Desc | varchar |  |  | NO | Description |
| SSOA_Owner | varchar |  |  | SI | Owner |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*