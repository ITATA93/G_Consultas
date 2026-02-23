# questionnaire.QTCNOERQQ08

> Neonatal Ophthalmology Examination Record : Exam

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal Ophthalmology Examination Record : Exam

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | varchar |  |  | SI | Eye |
| Q08Q2 | varchar |  |  | SI | Zone |
| Q08Q3 | varchar |  |  | SI | Stage |
| Q08Q4 | varchar |  |  | SI | Preplus |
| Q08Q5 | varchar |  |  | SI | Plus |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*