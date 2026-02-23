# questionnaire.QTCPDSAQQ30

> Peritoneal Dialysis Suitability Assessment : Strength

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Strength

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | varchar |  |  | SI | Strength assessment for |
| Q30Q2 | varchar |  |  | SI | Able to lift 2 litre bags |
| Q30Q3 | varchar |  |  | SI | Able to lift 6 litre bags |
| Q30Q4 | varchar |  |  | SI | Able to open packaging |
| Q30Q5 | varchar |  |  | SI | Able to hang bags |
| Q30Q6 | varchar |  |  | SI | Able to dispose of rubbish |
| Q30Q7 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*