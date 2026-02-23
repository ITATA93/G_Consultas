# lab.BBP_Antigens

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPC_ParRef | varchar | PK |  | NO | BBP_PackDetails Parent Reference |
| BBPC_Genotype_DR | varchar |  | FK | NO | Genotype DR |
| BBPC_Result | varchar |  |  | SI | Result |
| BBPC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*