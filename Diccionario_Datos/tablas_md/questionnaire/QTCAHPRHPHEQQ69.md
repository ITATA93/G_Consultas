# questionnaire.QTCAHPRHPHEQQ69

> Pelvic and Hip Evaluation : Range of Motion (ROM)

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pelvic and Hip Evaluation : Range of Motion (ROM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q69Q1 | varchar |  |  | SI | Joint / Motion |
| Q69Q2 | numeric |  |  | SI | AROM Left |
| Q69Q3 | numeric |  |  | SI | PROM Left |
| Q69Q4 | numeric |  |  | SI | AROM Right |
| Q69Q5 | numeric |  |  | SI | PROM Right |
| Q69Q6 | varchar |  |  | SI | End Feel |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*