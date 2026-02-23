# questionnaire.QTCAHPRHNEVQQ30

> Neurological Evaluation : Elbow

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Elbow

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | varchar |  |  | SI | Movement |
| Q30Q2 | varchar |  |  | SI | Strength - Right |
| Q30Q3 | varchar |  |  | SI | Strength - Left |
| Q30Q4 | varchar |  |  | SI | AROM - Right |
| Q30Q5 | varchar |  |  | SI | AROM - Left |
| Q30Q6 | varchar |  |  | SI | PROM - Right |
| Q30Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*