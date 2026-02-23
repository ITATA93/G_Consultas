# SQLUser.LBC_ContainerLabelRule

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCONLR_ParRef | bigint | PK |  | NO | Parent Container DR |
| ChildQ20DR | - |  |  | SI | Child Reference: Embryo Thaw |
| LBCCONLR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCONLR_DateFrom | date |  |  | NO | Effective date for the record |
| LBCCONLR_DateTo | date |  |  | SI | DateTo
Last day the record is active
Optional.  ... |
| LBCCONLR_Department_DR | bigint |  | FK | SI | Department |
| LBCCONLR_LocationType | varchar |  |  | SI | Location Type |
| LBCCONLR_Report_DR | bigint |  | FK | SI | Report |
| LBCCONLR_RowID | varchar |  |  | NO | - |
| LBCCONLR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCCONLR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCCONLR_TestSet_DR | bigint |  | FK | SI | Test Set |
| Q19Q1 | - |  |  | SI | Straw number |
| Q19Q2 | - |  |  | SI | Comment |
| Q19Q3 | - |  |  | SI | Straw tip color |
| Q19Q4 | - |  |  | SI | Pencil color |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*