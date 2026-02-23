# lab.MIF_MachineResultsBugAnt

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRBA_ParRef | varchar | PK |  | NO | MIF_MachineResultsBugs Parent Reference |
| MIRBA_AntiBiotic_DR | varchar |  | FK | NO | AntiBiotic DR |
| MIRBA_Reportable | varchar |  |  | SI | Reportable |
| MIRBA_Result_DR | varchar |  | FK | SI | Result DR |
| MIRBA_Result_ETest | varchar |  |  | SI | Result E Test |
| MIRBA_Result_MIC | varchar |  |  | SI | Result MIC |
| MIRBA_Result_mm | varchar |  |  | SI | Result mm |
| MIRBA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*