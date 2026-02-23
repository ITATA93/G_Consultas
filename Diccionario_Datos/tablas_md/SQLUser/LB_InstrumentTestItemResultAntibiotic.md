# SQLUser.LB_InstrumentTestItemResultAntibiotic

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBITIRA_ParRef | varchar | PK |  | NO | Instrument Test Item Result Parent Reference |
| LBITIRA_Antibiotic_DR | bigint |  | FK | SI | Antibiotic |
| LBITIRA_Reportable | varchar |  |  | SI | Reportable flag |
| LBITIRA_ResultETest | varchar |  |  | SI | Result E Test |
| LBITIRA_ResultMIC | varchar |  |  | SI | Result MIC |
| LBITIRA_Result_DR | bigint |  | FK | SI | Antibiotic sensitivity result |
| LBITIRA_Resultmm | varchar |  |  | SI | Result mm |
| LBITIRA_RowID | varchar |  |  | NO | - |
| Q80Q1 | - |  |  | SI | Hallazgos |
| Q80Q2 | - |  |  | SI | Ubicación |
| Q80Q3 | - |  |  | SI | Lateralidad |
| Q80Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*