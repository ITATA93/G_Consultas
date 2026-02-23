# questionnaire.QTCIVALPLAQQ21

> Peripheral Line Assessment : Assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peripheral Line Assessment : Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | varchar |  |  | SI | Need daily assessment |
| Q21Q2 | varchar |  |  | SI | Care |
| Q21Q3 | varchar |  |  | SI | Site details |
| Q21Q4 | varchar |  |  | SI | Dressing type / appearance |
| Q21Q5 | varchar |  |  | SI | Peripheral intravenous patency |
| Q21Q6 | date |  |  | SI | Assessment date and time |
| Q21Q7 | time |  |  | SI | Assessment time |
| Q21Q8 | varchar |  |  | SI | Assessing care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*