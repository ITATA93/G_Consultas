# questionnaire.QTCEEGMATQQ01

> Egreso Madre Hijo : Egreso de Recién Nacido

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Egreso Madre Hijo : Egreso de Recién Nacido

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Identificación |
| Q01Q2 | varchar |  |  | SI | Estado de Salud |
| Q01Q3 | varchar |  |  | SI | Destino |
| Q01Q4 | varchar |  |  | SI | Alimentacion (al egreso) |
| Q01Q5 | numeric |  |  | SI | Peso al egreso (grs.) |
| Q01Q6 | varchar |  |  | SI | Comentarios |
| Q01Q7 | date |  |  | SI | Fecha de Egreso |
| Q01Q8 | varchar |  |  | SI | Alimentación (durante estadía) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*