# questionnaire.QTCIVALALAQQ26

> Arterial Line Assessment : Arterial line assessment

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Arterial Line Assessment : Arterial line assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q26Q1 | varchar |  |  | SI | Status |
| Q26Q2 | varchar |  |  | SI | Care / Troubleshoot |
| Q26Q3 | varchar |  |  | SI | Site care |
| Q26Q4 | varchar |  |  | SI | Site condition |
| Q26Q5 | varchar |  |  | SI | Dressing |
| Q26Q6 | varchar |  |  | SI | Dressing condition |
| Q26Q7 | date |  |  | SI | Assessment date and time |
| Q26Q8 | time |  |  | SI | Assessment time |
| Q26Q9 | varchar |  |  | SI | Assessing care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*