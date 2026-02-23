# questionnaire.QTCAHPRHNEVQQ32

> Neurological Evaluation : Fingers

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Fingers

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | varchar |  |  | SI | Movement |
| Q32Q2 | varchar |  |  | SI | Strength - Right |
| Q32Q3 | varchar |  |  | SI | Strength - Left |
| Q32Q4 | varchar |  |  | SI | AROM - Right |
| Q32Q5 | varchar |  |  | SI | AROM - Left |
| Q32Q6 | varchar |  |  | SI | PROM - Right |
| Q32Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*