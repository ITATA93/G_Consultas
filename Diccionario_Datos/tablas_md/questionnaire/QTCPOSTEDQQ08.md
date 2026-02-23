# questionnaire.QTCPOSTEDQQ08

> Postpartum Emergency Documentation : Add clinicians present

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add clinicians present

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | varchar |  |  | SI | Clinician |
| Q08Q2 | varchar |  |  | SI | Role |
| Q08Q3 | varchar |  |  | SI | Other (specify) |
| Q08Q4 | time |  |  | SI | Arrival time |
| Q08Q5 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*