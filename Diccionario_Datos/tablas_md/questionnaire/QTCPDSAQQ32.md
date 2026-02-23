# questionnaire.QTCPDSAQQ32

> Peritoneal Dialysis Suitability Assessment : Eyesight

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Eyesight

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | varchar |  |  | SI | Eyesight assessment for |
| Q32Q2 | varchar |  |  | SI | Requires reading aids |
| Q32Q3 | varchar |  |  | SI | Other reading aids, if applicable |
| Q32Q4 | varchar |  |  | SI | Able to read weigh scales |
| Q32Q5 | varchar |  |  | SI | Able to read PD bag labels |
| Q32Q6 | varchar |  |  | SI | Able to read automated PD messages |
| Q32Q7 | varchar |  |  | SI | Cataracts |
| Q32Q8 | varchar |  |  | SI | Eye review required |
| Q32Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*