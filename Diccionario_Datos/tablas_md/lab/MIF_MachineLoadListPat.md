# lab.MIF_MachineLoadListPat

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MILLP_ParRef | varchar | PK |  | NO | MIF_MachineLoadList Parent Reference |
| MILLP_DateOfCollection | date |  |  | SI | Date Of Collection |
| MILLP_Dilution | varchar |  |  | SI | Dilution |
| MILLP_Episode | varchar |  |  | SI | Episode |
| MILLP_ListOfTests | varchar |  |  | SI | List Of Tests |
| MILLP_Order | double |  |  | NO | Order |
| MILLP_Replicates | numeric |  |  | SI | Number of Replicates |
| MILLP_RowId | varchar |  |  | NO | - |
| MILLP_SampleNumber | varchar |  |  | SI | Sample Number |
| MILLP_Specimen_DR | varchar |  | FK | SI | Des Ref Specimen |
| MILLP_Status | varchar |  |  | SI | Status |
| MILLP_TimeOfCollection | time |  |  | SI | Time Of Collection |
| MILLP_xxx2 | varchar |  |  | SI | Date Sent |
| MILLP_xxx4 | varchar |  |  | SI | Time Printed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*