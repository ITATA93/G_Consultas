# questionnaire.QTCAHPRHCRPQQ120

> Cardiac Rehabilitation Physiotherapy Assessment : Exercise Test Scale

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Rehabilitation Physiotherapy Assessment : Exercise Test Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q120Q1 | varchar |  |  | SI | Time |
| Q120Q2 | numeric |  |  | SI | Systolic |
| Q120Q3 | numeric |  |  | SI | Diastolic |
| Q120Q4 | varchar |  |  | SI | Rating of Perceived Exertion |
| Q120Q5 | numeric |  |  | SI | Burdon's Modified Borg Scale |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*