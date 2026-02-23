# questionnaire.QTCISQQ10

> Infectious Status : Review of precautions

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infectious Status : Review of precautions

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | date |  |  | SI | Review date |
| Q10Q2 | varchar |  |  | SI | Screening status |
| Q10Q3 | varchar |  |  | SI | Review notes |
| Q10Q4 | varchar |  |  | SI | Reviewed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*