# questionnaire.QTCAHPRHKEQQ62

> Knee Evaluation : Range of Motion (ROM)

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Knee Evaluation : Range of Motion (ROM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q62Q1 | varchar |  |  | SI | Joint / Motion |
| Q62Q2 | numeric |  |  | SI | AROM left |
| Q62Q3 | numeric |  |  | SI | PROM left |
| Q62Q4 | numeric |  |  | SI | AROM right |
| Q62Q5 | numeric |  |  | SI | PROM right |
| Q62Q6 | varchar |  |  | SI | End feel |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*