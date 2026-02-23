# SQLUser.LB_WorksheetCounter

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWSCNT_RowID | bigint | PK |  | NO | - |
| LBWSCNT_Configuration | bigint |  |  | SI | Configuration |
| LBWSCNT_CounterNumber | integer |  |  | SI | Counter Number |
| Q28Q1 | - |  |  | SI | N° Tamizaje |
| Q28Q2 | - |  |  | SI | Técnica |
| Q28Q3 | - |  |  | SI | Lote |
| Q28Q4 | - |  |  | SI | CUT-OFF |
| Q28Q5 | - |  |  | SI | Reactividad |
| Q28Q6 | - |  |  | SI | Resultado |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*