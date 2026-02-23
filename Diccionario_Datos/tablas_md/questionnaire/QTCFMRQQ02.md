# questionnaire.QTCFMRQQ02

> Family Meeting Register : Staff members present

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Family Meeting Register : Staff members present

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Name |
| Q02Q2 | varchar |  |  | SI | Position |
| Q02Q3 | varchar |  |  | SI | Speciality |
| Q02Q4 | time |  |  | SI | Time arrived |
| Q02Q5 | time |  |  | SI | Time departed |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*