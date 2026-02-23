# lab.MIF_MachineQC

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIQC_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIQC_QCAssociationFrom | double |  |  | SI | QC Association From (Hours) |
| MIQC_QCAssociationTo | double |  |  | SI | QC Association To (Hours) |
| MIQC_QC_Group_DR | varchar |  | FK | NO | QC Group DR |
| MIQC_QC_Level | double |  |  | NO | QC Level |
| MIQC_QC_Type | varchar |  |  | NO | QC Type |
| MIQC_RowID | varchar |  |  | NO | - |
| MIQC_SampleID | varchar |  |  | SI | Sample ID |
| MIQC_SamplePosition | varchar |  |  | SI | Sample Position |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*