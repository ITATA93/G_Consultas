# lab.MIF_MachineResultHeader

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRH_ParRef | varchar | PK |  | NO | MIF_MachineParameters Parent Reference |
| MIRH_DateOfRun | date |  |  | SI | Date of Run |
| MIRH_DateOfTransmission | date |  |  | SI | Date Of Transmission |
| MIRH_Epis_DR | varchar |  | FK | SI | Episode |
| MIRH_RowId | varchar |  |  | NO | - |
| MIRH_SampleNumber | varchar |  |  | NO | Sample Number |
| MIRH_Status | varchar |  |  | SI | Status |
| MIRH_StatusHold | varchar |  |  | SI | Status Hold |
| MIRH_StatusPathogen | numeric |  |  | SI | Status Pathogen |
| MIRH_StatusPlot | varchar |  |  | SI | Status Plot |
| MIRH_Surname | varchar |  |  | SI | Surname |
| MIRH_TSet_List | varchar |  |  | SI | Test Set List |
| MIRH_TimeOfRun | time |  |  | SI | Time of Run |
| MIRH_TimeOfTransmission | time |  |  | SI | Time of Transmission |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*