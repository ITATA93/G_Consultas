# lab.OLD_ResultsPack

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OLDA_ParRef | numeric | PK |  | NO | - |
| OLDA_DateLastTransaction | date |  |  | SI | Date Last Transaction |
| OLDA_DateReceived | date |  |  | SI | Date Received |
| OLDA_DiscardReason | varchar |  |  | SI | Discard Reason |
| OLDA_ExternalIssue | varchar |  |  | SI | External Issue |
| OLDA_PackBloodGroup | varchar |  |  | SI | Pack Blood Group |
| OLDA_PackFate | varchar |  |  | SI | Pack Fate |
| OLDA_PackID | varchar |  |  | SI | Pack ID |
| OLDA_RowID | varchar |  |  | NO | - |
| OLDA_Sequence | varchar |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*