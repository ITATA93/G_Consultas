# questionnaire.QTCASURAQQ17

> Alcohol and Substance Use Risk Assessment : Other Drugs / Substances

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Alcohol and Substance Use Risk Assessment : Other Drugs / Substances

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | varchar |  |  | SI | Substance |
| Q17Q2 | varchar |  |  | SI | Route |
| Q17Q3 | date |  |  | SI | Last taken date / time |
| Q17Q4 | time |  |  | SI | Last taken time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*