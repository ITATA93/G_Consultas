# questionnaire.QTCMROCQQ21

> Mechanical Restraint Observation Chart : Restraint Assesment

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mechanical Restraint Observation Chart : Restraint Assesment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | date |  |  | SI | Assessment date |
| Q21Q10 | varchar |  |  | SI | Assessment comments |
| Q21Q2 | time |  |  | SI | Assessment time |
| Q21Q3 | varchar |  |  | SI | Care provider |
| Q21Q4 | varchar |  |  | SI | Type of restraint applied |
| Q21Q5 | varchar |  |  | SI | Restraint location |
| Q21Q6 | varchar |  |  | SI | Patient's behaviour |
| Q21Q7 | varchar |  |  | SI | Restrained limbs checked |
| Q21Q8 | varchar |  |  | SI | Care performed |
| Q21Q9 | varchar |  |  | SI | Evaluation of restraint reduction |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*