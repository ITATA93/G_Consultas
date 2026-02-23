# lab.MIF_MachinePatientList

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIMPL_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIMPL_DateTimeOfEntry | varchar |  |  | SI | Date and Time Of Entry |
| MIMPL_DateTimeOfRecResults | varchar |  |  | SI | Date and Time Of Receiving Results |
| MIMPL_DateTimeOfSendToMachine | varchar |  |  | SI | Date and Time Of Sending To the Machine |
| MIMPL_Episode_DR | varchar |  | FK | NO | Episode DR |
| MIMPL_ListOfTests | varchar |  |  | SI | List Of Tests |
| MIMPL_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*