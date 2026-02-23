# SQLUser.LB_SubjectOrdItem

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSOI_RowID | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Información Social |
| LBSOI_Episode_DR | bigint |  | FK | NO | Lab Episode |
| LBSOI_ItmMast_DR | varchar |  | FK | NO | - |
| LBSOI_OrderDate | date |  |  | SI | Order Date |
| LBSOI_OrderTime | time |  |  | SI | Order Time |
| LBSOI_Priority_DR | bigint |  | FK | SI | Order priority |
| Q20Q1 | - |  |  | SI | Caso índice |
| Q20Q2 | - |  |  | SI | Motivos |
| Q20Q3 | - |  |  | SI | Objetivos |
| Q20Q4 | - |  |  | SI | Actividades |
| Q20Q5 | - |  |  | SI | Tiempo de intervención |
| Q20Q6 | - |  |  | SI | Observaciones |
| Q20Q7 | - |  |  | SI | Responsables |
| Q20Q8 | - |  |  | SI | Profesional |
| Q20Q9 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*