# questionnaire.QTCITDEQQ07

> Interdisciplinary Education : Education record

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Interdisciplinary Education : Education record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q07Q1 | date |  |  | SI | Date |
| Q07Q10 | varchar |  |  | SI | Performed  by: |
| Q07Q2 | time |  |  | SI | Time |
| Q07Q3 | numeric |  |  | SI | Duration of taught (Minutes) |
| Q07Q4 | varchar |  |  | SI | Participant(s) |
| Q07Q5 | varchar |  |  | SI | Education method used |
| Q07Q6 | varchar |  |  | SI | Learning barrier |
| Q07Q7 | varchar |  |  | SI | Education needs and information taught  (* is mand... |
| Q07Q8 | varchar |  |  | SI | Learning Response |
| Q07Q9 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*