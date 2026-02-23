# SQLUser.OR_An_Oper_Position

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPPOS_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPPOS_Childsub | numeric |  |  | NO | Childsub |
| OPPOS_Comments | varchar |  |  | SI | Comments |
| OPPOS_EndTime | time |  |  | SI | End Time |
| OPPOS_Position_DR | bigint |  | FK | NO | Position Des Ref to ORCPOS |
| OPPOS_RowId | varchar |  |  | NO | - |
| OPPOS_StartTime | time |  |  | SI | Start Time |
| Q09Q1 | - |  |  | SI | Date |
| Q09Q2 | - |  |  | SI | Time |
| Q09Q3 | - |  |  | SI | Dressing status |
| Q09Q4 | - |  |  | SI | Insertion site check |
| Q09Q5 | - |  |  | SI | Actions performed |
| Q09Q6 | - |  |  | SI | Assessment notes |
| Q09Q7 | - |  |  | SI | Assessment performed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*