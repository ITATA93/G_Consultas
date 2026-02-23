# SQLUser.SS_ProfileLabSiteAdmin

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLSA_ParRef | bigint | PK |  | NO | Parent table |
| SSPLSA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPLSA_DateFrom | date |  |  | SI | Date From |
| SSPLSA_DateTo | date |  |  | SI | Date To |
| SSPLSA_LabSite_DR | bigint |  | FK | SI | Lab Sites for Code Tables |
| SSPLSA_ReadOnly | varchar |  |  | SI | Read Only |
| SSPLSA_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*