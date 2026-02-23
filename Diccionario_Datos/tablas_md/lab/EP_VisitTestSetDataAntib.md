# lab.EP_VisitTestSetDataAntib

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISTA_ParRef | varchar | PK |  | NO | EP_VisitTestSetData Parent Reference |
| VISTA_AntibioticPanel_DR | varchar |  | FK | SI | Antibiotic Panel DR |
| VISTA_Antibiotic_DR | varchar |  | FK | NO | Antibiotics Code |
| VISTA_Machine_DR | varchar |  | FK | SI | Machine DR |
| VISTA_Reportable | varchar |  |  | SI | Reportable |
| VISTA_Restricted | varchar |  |  | SI | Restricted |
| VISTA_Result_DR | varchar |  | FK | SI | Des Ref Sens |
| VISTA_Result_ETest | varchar |  |  | SI | Result E Test |
| VISTA_Result_MIC | varchar |  |  | SI | Result MIC |
| VISTA_Result_mm | varchar |  |  | SI | Result mm |
| VISTA_RowId | varchar |  |  | NO | - |
| VISTA_Sequence | varchar |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*