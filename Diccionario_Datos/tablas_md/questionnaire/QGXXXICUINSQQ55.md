# questionnaire.QGXXXICUINSQQ55

> General Drains Assessments : Daily shift assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* General Drains Assessments : Daily shift assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q55Q1 | varchar |  |  | SI | IV Check |
| Q55Q2 | varchar |  |  | SI | IV Access Heparin locked and labeled |
| Q55Q3 | varchar |  |  | SI | Flush bag pressure checked |
| Q55Q4 | date |  |  | SI | Date |
| Q55Q5 | time |  |  | SI | Time |
| Q55Q6 | varchar |  |  | SI | Note |
| Q55Q7 | varchar |  |  | SI | Actions |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*