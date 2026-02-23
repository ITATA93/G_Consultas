# lab.MIF_MachineResultsAntib

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIRIA_ParRef | varchar | PK |  | NO | MIF_MachineResults Parent Reference |
| MIRIA_AntiBiotics_DR | varchar |  | FK | NO | AntiBioticsDR |
| MIRIA_AntibioticPanel_DR | varchar |  | FK | SI | Antibiotic Panel DR |
| MIRIA_Reportable | varchar |  |  | SI | Reportable |
| MIRIA_Result_DR | varchar |  | FK | SI | Result DR |
| MIRIA_Result_ETest | varchar |  |  | SI | Result E Test |
| MIRIA_Result_MIC | varchar |  |  | SI | Result MIC |
| MIRIA_Result_mm | varchar |  |  | SI | Result mm |
| MIRIA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*