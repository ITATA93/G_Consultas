# lab.BBP_XM

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPX_ParRef | varchar | PK |  | NO | BBP_PackDetails Parent Reference |
| BBPX_Episode_DR | varchar |  | FK | NO | Episode DR |
| BBPX_Phases | varchar |  |  | SI | Phases |
| BBPX_RowID | varchar |  |  | NO | - |
| BBPX_TestCounter | double |  |  | NO | Test Counter |
| BBPX_TestSet_DR | varchar |  | FK | NO | Test Set DR |
| BBPX_XMStatus | varchar |  |  | SI | XM Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*