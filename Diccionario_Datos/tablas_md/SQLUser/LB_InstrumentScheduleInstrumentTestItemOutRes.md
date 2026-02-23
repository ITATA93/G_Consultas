# SQLUser.LB_InstrumentScheduleInstrumentTestItemOutRes

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBISITIOR_ParRef | varchar | PK |  | NO | Parent |
| ChildQ64DR | - |  |  | SI | Child Reference: Abdomen |
| LBISITIOR_OutResultInstrumentTestItemID | varchar |  |  | SI | Outbound Result Instrument Test Item ID (Channel I... |
| LBISITIOR_RowID | varchar |  |  | NO | - |
| LBISITIOR_TestItem_DR | bigint |  | FK | SI | The test set item result to be transmitted with th... |
| Q61Q1 | - |  |  | SI | Ritmo |
| Q61Q2 | - |  |  | SI | Soplos |
| Q61Q3 | - |  |  | SI | Grado |
| Q61Q4 | - |  |  | SI | Foco |
| Q61Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*