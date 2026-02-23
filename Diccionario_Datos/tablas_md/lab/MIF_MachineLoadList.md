# lab.MIF_MachineLoadList

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MILL_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MILL_DateCreated | date |  |  | SI | Date |
| MILL_DateRequested | date |  |  | SI | Date Requested |
| MILL_DateSent | date |  |  | SI | Date Sent |
| MILL_Order | double |  |  | NO | Order |
| MILL_Print | varchar |  |  | SI | Print |
| MILL_RowId | varchar |  |  | NO | - |
| MILL_Specimen_DR | varchar |  | FK | SI | Des Ref Specimen |
| MILL_Status | varchar |  |  | SI | Status |
| MILL_TimeCreated | time |  |  | SI | Time |
| MILL_TimeRequested | time |  |  | SI | Time Requested |
| MILL_TimeSent | time |  |  | SI | Time Sent |
| MILL_TrayNumber | varchar |  |  | SI | Tray Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*