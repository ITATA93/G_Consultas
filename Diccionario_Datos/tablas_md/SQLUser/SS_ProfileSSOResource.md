# SQLUser.SS_ProfileSSOResource

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSOR_ParRef | bigint | PK |  | NO | Parent table |
| SSOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSOR_DateFrom | date |  |  | SI | Date From |
| SSOR_DateTo | date |  |  | SI | Date To |
| SSOR_RowID | varchar |  |  | NO | - |
| SSOR_SingleSignOnResource_DR | bigint |  | FK | SI | SingleSignOnResource |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*