# questionnaire.QTCMROCQQ22

> Mechanical Restraint Observation Chart : Medical Officer Review

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mechanical Restraint Observation Chart : Medical Officer Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q22Q1 | date |  |  | SI | Date |
| Q22Q2 | time |  |  | SI | Time |
| Q22Q3 | varchar |  |  | SI | Reviewed by |
| Q22Q4 | varchar |  |  | SI | Frequency for review |
| Q22Q5 | varchar |  |  | SI | New order placed? |
| Q22Q6 | varchar |  |  | SI | Continue restraint? |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*