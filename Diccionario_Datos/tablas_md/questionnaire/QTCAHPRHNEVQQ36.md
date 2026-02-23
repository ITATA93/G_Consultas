# questionnaire.QTCAHPRHNEVQQ36

> Neurological Evaluation : Long Toe

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Long Toe

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q36Q1 | varchar |  |  | SI | Movement |
| Q36Q2 | varchar |  |  | SI | Strength - Right |
| Q36Q3 | varchar |  |  | SI | Strength - Left |
| Q36Q4 | varchar |  |  | SI | AROM - Right |
| Q36Q5 | varchar |  |  | SI | AROM - Left |
| Q36Q6 | varchar |  |  | SI | PROM - Right |
| Q36Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*