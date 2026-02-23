# epr.CTGraphRefRange

**Schema:** epr
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| GREFCode | varchar |  |  | NO | - |
| GREFDesc | varchar |  |  | SI | - |
| GREFLineColour | varchar |  |  | SI | - |
| GREFLineType | varchar |  |  | SI | - |
| GREFPercDesc | varchar |  |  | SI | - |
| GREFTimeStart | varchar |  |  | SI | Time Starting Point |
| GREFXAxisIncrement | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*