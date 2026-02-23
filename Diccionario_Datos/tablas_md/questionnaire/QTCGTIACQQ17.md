# questionnaire.QTCGTIACQQ17

> Gastric Tube Insertion and Care : Gastric tube assessments

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Gastric Tube Insertion and Care : Gastric tube assessments

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | date |  |  | SI | Date |
| Q17Q2 | time |  |  | SI | Time |
| Q17Q3 | numeric |  |  | SI | Length of tube from nostril / teeth / gums (cm) |
| Q17Q4 | varchar |  |  | SI | Tube position checked |
| Q17Q5 | varchar |  |  | SI | Securement device checked |
| Q17Q6 | varchar |  |  | SI | Actions performed |
| Q17Q7 | varchar |  |  | SI | Assessment notes |
| Q17Q8 | varchar |  |  | SI | Assessment performed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*