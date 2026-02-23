# questionnaire.QTCIVFESSQQ17

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q17Q1 | numeric | PK |  | SI | Oocyte |
| Q17Q10 | varchar | PK |  | SI | Frozen |
| Q17Q2 | varchar | PK |  | SI | Stage |
| Q17Q3 | varchar | PK |  | SI | Insemination |
| Q17Q4 | numeric | PK |  | SI | Day 1 pronuclei |
| Q17Q5 | numeric | PK |  | SI | Cleavage day 2 |
| Q17Q6 | numeric | PK |  | SI | Cleavage day  3 |
| Q17Q7 | numeric | PK |  | SI | Cleavage day 4 |
| Q17Q8 | numeric | PK |  | SI | Cleavage day 5 |
| Q17Q9 | varchar | PK |  | SI | Transferred |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*