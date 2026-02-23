# questionnaire.QTCNSSQQ02

> Total Parenteral Nutrition (TPN) Support Service : Nutritional review

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Total Parenteral Nutrition (TPN) Support Service : Nutritional review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | date |  |  | SI | Date |
| Q02Q10 | varchar |  |  | SI | Blood glucose levels (BGL) in previous 24 hours wi... |
| Q02Q2 | time |  |  | SI | Time |
| Q02Q3 | varchar |  |  | SI | TPN rate at review |
| Q02Q4 | numeric |  |  | SI | Days on TPN |
| Q02Q5 | varchar |  |  | SI | Pathology comments |
| Q02Q6 | varchar |  |  | SI | Glycaemic control target |
| Q02Q7 | varchar |  |  | SI | Current frequency of BGL check |
| Q02Q8 | varchar |  |  | SI | Additional comments |
| Q02Q9 | varchar |  |  | SI | Bag and line changed within last 24 hours |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*