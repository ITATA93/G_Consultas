# SQLUser.LB_InstrumentScheduleInstrumentPanel

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBISIPN_ParRef | varchar | PK |  | NO | Parent |
| ChildQ73DR | - |  |  | SI | Child Reference: Oculomotilidad |
| LBISIPN_OutboundInstrumentPanelID | varchar |  |  | SI | Outbound Channel ID
For indexing only |
| LBISIPN_PendingUpload | varchar |  |  | SI | Upload Pending
Indicates the panel should be sent... |
| LBISIPN_RowID | varchar |  |  | NO | - |
| LBISIPN_TestSets | varchar |  |  | SI | The test sets of the panel IDs |
| LBISIPN_Transmitted | varchar |  |  | SI | Flag to indicate if the panel ID has been transmit... |
| Q166Q1 | - |  |  | SI | Ojo |
| Q166Q2 | - |  |  | SI | DPA |
| Q166Q3 | - |  |  | SI | Magnitud |
| Q166Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*