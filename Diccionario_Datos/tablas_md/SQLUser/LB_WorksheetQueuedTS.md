# SQLUser.LB_WorksheetQueuedTS

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWQTS_RowID | bigint | PK |  | NO | - |
| ChildQ46DR | - |  |  | SI | Child Reference: Pulsos |
| LBWQTS_TestSet_DR | bigint |  | FK | SI | - |
| Q45Q1 | - |  |  | SI | Hallazgos |
| Q45Q2 | - |  |  | SI | Ext. Superior |
| Q45Q3 | - |  |  | SI | Ext. Inferior |
| Q45Q4 | - |  |  | SI | Topografía |
| Q45Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*