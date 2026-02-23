# lab.CT_SpecimenLabBlockOrder

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPD_ParRef | varchar | PK |  | NO | CT_SpecimenLabBlock Parent Reference |
| CTSPD_Complete | varchar |  |  | SI | Complete |
| CTSPD_Level | varchar |  |  | SI | Level |
| CTSPD_Order | varchar |  |  | NO | Order |
| CTSPD_ProcedureCode | varchar |  |  | SI | Procedure Code |
| CTSPD_RowId | varchar |  |  | NO | - |
| CTSPD_StainCode | varchar |  |  | SI | StainCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*