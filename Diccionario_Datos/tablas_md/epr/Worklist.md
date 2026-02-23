# epr.Worklist

**Schema:** epr
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Border | bit |  |  | SI | - |
| Deprecated | bit |  |  | SI | - |
| FrameSize1 | varchar |  |  | SI | - |
| FrameSize2 | varchar |  |  | SI | - |
| FrameSize3 | varchar |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| ResizeButtons | bit |  |  | SI | - |
| Resizeable | bit |  |  | SI | - |
| Script | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| Style | varchar |  |  | NO | - |
| WorklistSettings | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*