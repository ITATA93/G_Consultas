# questionnaire.QTCCHDSQQ20

> Congenital Heart Disease Screening : Congenital heart disease screening

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Congenital Heart Disease Screening : Congenital heart disease screening

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | varchar |  |  | SI | Child status  |
| Q20Q2 | varchar |  |  | SI | Screening level |
| Q20Q3 | varchar |  |  | SI | Screening result |
| Q20Q4 | varchar |  |  | SI | Screen outcome |
| Q20Q5 | date |  |  | SI | Date |
| Q20Q6 | time |  |  | SI | Time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*