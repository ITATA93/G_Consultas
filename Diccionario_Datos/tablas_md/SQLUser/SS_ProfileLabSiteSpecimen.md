# SQLUser.SS_ProfileLabSiteSpecimen

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPLSS_ParRef | bigint | PK |  | NO | Parent table |
| SSPLSS_AllowAliquot | varchar |  |  | SI | Can Aliquot specimens |
| SSPLSS_AllowPooling | varchar |  |  | SI | Can Pool specimens |
| SSPLSS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPLSS_DateFrom | date |  |  | SI | Date From |
| SSPLSS_DateTo | date |  |  | SI | Date To |
| SSPLSS_LabSite_DR | bigint |  | FK | SI | LabSite |
| SSPLSS_OverrideFinanceCondition | varchar |  |  | SI | Can override finance condition |
| SSPLSS_RowID | varchar |  |  | NO | - |
| SSPLSS_Sequence | numeric |  |  | SI | Priority  Sequence |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*