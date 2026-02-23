# questionnaire.QTCUCAQQ16

> Urinary Catheter Access : Daily Shift Assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Urinary Catheter Access : Daily Shift Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q16Q1 | date |  |  | SI | Date |
| Q16Q2 | time |  |  | SI | Time |
| Q16Q3 | varchar |  |  | SI | Catheter Check |
| Q16Q4 | varchar |  |  | SI | Actions |
| Q16Q7 | varchar |  |  | SI | Comments |
| Q16Q8 | varchar |  |  | SI | Urinary specimen taken |
| Q16Q9 | varchar |  |  | SI | Insertion site swab taken |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*