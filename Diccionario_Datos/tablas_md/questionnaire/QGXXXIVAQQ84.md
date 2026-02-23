# questionnaire.QGXXXIVAQQ84

> Intravascular Access : PA Catheter Check

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access : PA Catheter Check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q84Q1 | date |  |  | SI | Date |
| Q84Q2 | time |  |  | SI | Time |
| Q84Q3 | varchar |  |  | SI | Checklist |
| Q84Q4 | numeric |  |  | SI | Catheter length at wedge (cm) |
| Q84Q5 | numeric |  |  | SI | Pulmonary capillary wedge pressure (mmHg) |
| Q84Q6 | varchar |  |  | SI | Comments |
| Q84Q7 | varchar |  |  | SI | Staff |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*