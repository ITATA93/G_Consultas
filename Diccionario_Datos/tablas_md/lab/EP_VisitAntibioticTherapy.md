# lab.EP_VisitAntibioticTherapy

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISAT_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISAT_Antibiotic_DR | varchar |  | FK | NO | Antibiotic DR |
| VISAT_Dosage | varchar |  |  | SI | Dosage |
| VISAT_RowID | varchar |  |  | NO | - |
| VISAT_StartDate | date |  |  | SI | Start Date |
| VISAT_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*