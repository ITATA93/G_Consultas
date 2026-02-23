# questionnaire.QTCAHPRHNEVQQ35

> Neurological Evaluation : Ankle

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Ankle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q35Q1 | varchar |  |  | SI | Movement |
| Q35Q2 | varchar |  |  | SI | Strength - Right |
| Q35Q3 | varchar |  |  | SI | Strength - Left |
| Q35Q4 | varchar |  |  | SI | AROM - Right |
| Q35Q5 | varchar |  |  | SI | AROM - Left |
| Q35Q6 | varchar |  |  | SI | PROM - Right |
| Q35Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*