# questionnaire.QGXXXSTOMAQQ11

> Stoma : Evaluation

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stoma : Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | date |  |  | SI | Date |
| Q11Q2 | varchar |  |  | SI | Appearance |
| Q11Q3 | varchar |  |  | SI | Skin peristomal |
| Q11Q4 | varchar |  |  | SI | Excretion |
| Q11Q5 | varchar |  |  | SI | Pain |
| Q11Q6 | varchar |  |  | SI | Pain Score |
| Q11Q7 | varchar |  |  | SI | Note |
| Q11Q8 | time |  |  | SI | Time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*