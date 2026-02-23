# questionnaire.QTCAHPRHNEVQQ31

> Neurological Evaluation : Wrist

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Wrist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q31Q1 | varchar |  |  | SI | Movement |
| Q31Q2 | varchar |  |  | SI | Strength - Right |
| Q31Q3 | varchar |  |  | SI | Strength - Left |
| Q31Q4 | varchar |  |  | SI | AROM - Right |
| Q31Q5 | varchar |  |  | SI | AROM - Left |
| Q31Q6 | varchar |  |  | SI | PROM - Right |
| Q31Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*