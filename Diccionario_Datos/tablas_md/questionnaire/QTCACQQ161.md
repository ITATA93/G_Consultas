# questionnaire.QTCACQQ161

> Admission Checklist : Paediatric Pre-Admission Services

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Admission Checklist : Paediatric Pre-Admission Services

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q1 | varchar |  |  | SI | Service |
| Q2 | varchar |  |  | SI | Other service |
| Q3 | varchar |  |  | SI | Contact name |
| Q4 | varchar |  |  | SI | Contact details |
| Q5 | varchar |  |  | SI | Notified of admission |
| Q6 | date |  |  | SI | Date |
| Q7 | time |  |  | SI | Time |
| Q8 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*