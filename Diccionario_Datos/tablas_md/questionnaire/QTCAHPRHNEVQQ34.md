# questionnaire.QTCAHPRHNEVQQ34

> Neurological Evaluation : Knee

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation : Knee

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q34Q1 | varchar |  |  | SI | Movement |
| Q34Q2 | varchar |  |  | SI | Strength - Right |
| Q34Q3 | varchar |  |  | SI | Strength - Left |
| Q34Q4 | varchar |  |  | SI | AROM - Right |
| Q34Q5 | varchar |  |  | SI | AROM - Left |
| Q34Q6 | varchar |  |  | SI | PROM - Right |
| Q34Q7 | varchar |  |  | SI | PROM - Left |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*