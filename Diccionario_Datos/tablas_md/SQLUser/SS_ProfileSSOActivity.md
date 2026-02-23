# SQLUser.SS_ProfileSSOActivity

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOA_ParRef | bigint | PK |  | NO | Parent table |
| SSOA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSOA_DateFrom | date |  |  | SI | Date From |
| SSOA_DateTo | date |  |  | SI | Date To |
| SSOA_RowID | varchar |  |  | NO | - |
| SSOA_SingleSignOnActivity_DR | bigint |  | FK | SI | SingleSignOnActivity |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*