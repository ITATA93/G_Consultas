# SQLUser.MR_ExtraObservations

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| XOB_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ88DR | - |  |  | SI | Child Reference: Femostop Defaltion - 20mmHg every... |
| Q85Q1 | - |  |  | SI | Time |
| Q85Q2 | - |  |  | SI | mls |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| XOB_Childsub | double |  |  | NO | Childsub |
| XOB_GraphingMarker | double |  |  | SI | GraphingMarker |
| XOB_LineThick | double |  |  | SI | Line Thickness |
| XOB_ObsGroup_DR | bigint |  | FK | SI | Des REf ObsGroup |
| XOB_ObsItem_DR | bigint |  | FK | SI | Des Ref ObsItem |
| XOB_RowId | varchar |  |  | NO | - |
| XOB_RowPosition | double |  |  | SI | Row Position |
| XOB_YAxisOnGraph | varchar |  |  | SI | Y Axis On Graph |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*