# questionnaire.QTCSSKINQQ30

> SSKIN Bundle Assessment : Reasons for care not delivered

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* SSKIN Bundle Assessment : Reasons for care not delivered

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | date |  |  | SI | Date |
| Q30Q2 | time |  |  | SI | Time |
| Q30Q3 | varchar |  |  | SI | Record element |
| Q30Q4 | varchar |  |  | SI | Reason for not delivering care |
| Q30Q5 | varchar |  |  | SI | Care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*