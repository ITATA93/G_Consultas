# SQLUser.MR_PsychTreatmentForm

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TF_ParRef | varchar | PK |  | NO | MR_PsychDetails Parent Reference |
| Q0100 | - |  |  | SI | Item |
| Q0101 | - |  |  | SI | Start |
| Q0102 | - |  |  | SI | 1st Count |
| Q0103 | - |  |  | SI | 2nd Count |
| Q0104 | - |  |  | SI | 3rd Count |
| Q0105 | - |  |  | SI | Complete |
| Q0106 | - |  |  | SI | Incomplete |
| Q01Q10 | - |  |  | SI | Additions |
| Q01Q8 | - |  |  | SI | Accountable items |
| Q01Q9 | - |  |  | SI | Count all |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TF_Childsub | double |  |  | NO | Childsub |
| TF_Consent | varchar |  |  | SI | Consent |
| TF_ConsentObtained | varchar |  |  | SI | ConsentObtained |
| TF_DateFrom | date |  |  | SI | DateFrom |
| TF_DateTo | date |  |  | SI | DateTo |
| TF_RowId | varchar |  |  | NO | - |
| TF_SecondOpinion | varchar |  |  | SI | SecondOpinion |
| TF_TimeFrom | time |  |  | SI | TimeFrom |
| TF_TreatForm_DR | bigint |  | FK | SI | Des Ref TreatForm |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*