# SQLUser.LB_InstrumentEventRecord

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIEREC_ParRef | bigint | PK |  | NO | Parent Instrument Event DR |
| ChildQ160DR | - |  |  | SI | Child Reference: Campo Visual (Espec.) |
| LBIEREC_EventTypeRecord_DR | varchar |  | FK | NO | Link to the Record |
| LBIEREC_RowID | varchar |  |  | NO | - |
| LBIEREC_Value | varchar |  |  | SI | Value |
| Q159Q1 | - |  |  | SI | Uso de Lentes |
| Q159Q2 | - |  |  | SI | Ojo derecho (OD): |
| Q159Q3 | - |  |  | SI | Ojo Izquierdo (OI): |
| Q159Q4 | - |  |  | SI | CAE (OD): |
| Q159Q5 | - |  |  | SI | CAE (OI): |
| Q159Q6 | - |  |  | SI | Comentarios: |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*