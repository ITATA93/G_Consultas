# questionnaire.QTCWOUNDMGTQQ69

> Wound Assessment and Care : Wound Review - Medical / Wound Specialist

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Wound Review - Medical / Wound Specialist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q69Q1 | date |  |  | SI | Requested date |
| Q69Q2 | varchar |  |  | SI | Requested by |
| Q69Q3 | varchar |  |  | SI | Detail of request |
| Q69Q4 | date |  |  | SI | Completed date |
| Q69Q5 | varchar |  |  | SI | Completed by |
| Q69Q6 | varchar |  |  | SI | Detail of review |
| Q69Q7 | varchar |  |  | SI | Treatment plan modified? |
| Q69Q8 | date |  |  | SI | Date of treatment plan modification |
| Q69Q9 | varchar |  |  | SI | Rationale for plan modification |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*