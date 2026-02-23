# epr.CTIconAssociation

**Schema:** epr
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionMenuCondDescription | varchar |  |  | SI | Conditional Description displayed underneath the i... |
| Code | varchar |  |  | NO | - |
| CondDescription | varchar |  |  | SI | Conditional Description displayed as the tooltip f... |
| CondExpr | varchar |  |  | SI | Conditional Expression that determines whether the... |
| Description | varchar |  |  | SI | - |
| Icon | varchar |  |  | SI | - |
| IsDirty | bit |  |  | SI | internal flag for marking the record has been upda... |
| MultiEpisodes | bit |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| SVGIcon | varchar |  |  | SI | SVG Icon typcially as expression or path |
| ShortDescription | varchar |  |  | SI | - |
| SystemIcon | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*