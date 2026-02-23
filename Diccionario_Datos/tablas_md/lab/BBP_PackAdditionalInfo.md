# lab.BBP_PackAdditionalInfo

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPI_ParRef | varchar | PK |  | NO | BBP_PackDetails Parent Reference |
| BBPI_Code | varchar |  |  | NO | Code |
| BBPI_Comments | varchar |  |  | SI | BBPI_Comments |
| BBPI_Result | varchar |  |  | SI | Result |
| BBPI_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*