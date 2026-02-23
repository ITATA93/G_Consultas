# lab.MIF_MachineResults

**Schema:** lab
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRI_ParRef | varchar | PK |  | NO | MIF_MachineResultHeader Parent Reference |
| MIRI_AASupress | varchar |  |  | SI | Supress AA |
| MIRI_Active | varchar |  |  | SI | Active |
| MIRI_Antibiotics | varchar |  |  | SI | Antibiotics |
| MIRI_Comments | varchar |  |  | SI | Comments |
| MIRI_CreatedByUser_DR | varchar |  | FK | SI | Created By User |
| MIRI_DataItem_DR | varchar |  | FK | NO | Des Ref Data Item |
| MIRI_Date | date |  |  | SI | Date of filing |
| MIRI_Flag | varchar |  |  | SI | Flag |
| MIRI_MultipleResults | varchar |  |  | SI | Multiple Results |
| MIRI_Order | double |  |  | NO | Order number |
| MIRI_OriginalMachine_DR | varchar |  | FK | SI | Original machine |
| MIRI_QC_DR | varchar |  | FK | SI | QC DR field |
| MIRI_Result | varchar |  |  | SI | Result |
| MIRI_RowId | varchar |  |  | NO | - |
| MIRI_Specimen_DR | varchar |  | FK | SI | Specimen |
| MIRI_Time | time |  |  | SI | Time of filing |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*