# questionnaire.QTCMFRQQ06

> Medications Falls Risk Review : Medication falls review

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medications Falls Risk Review : Medication falls review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | varchar |  |  | SI | Medication |
| Q06Q2 | varchar |  |  | SI | Risk |
| Q06Q3 | varchar |  |  | SI | Nature of risk |
| Q06Q4 | varchar |  |  | SI | Other risks |
| Q06Q5 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*