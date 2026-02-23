# questionnaire.QTCACQQ143

> Admission Checklist : Family / Friend care arrangements

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Admission Checklist : Family / Friend care arrangements

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q143Q1 | varchar |  |  | SI | Name |
| Q143Q2 | varchar |  |  | SI | Relationship |
| Q143Q3 | varchar |  |  | SI | Other relationship |
| Q143Q4 | varchar |  |  | SI | Notified of admission |
| Q143Q5 | date |  |  | SI | Date |
| Q143Q6 | time |  |  | SI | Time |
| Q143Q7 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*