# questionnaire.QTCNSSQQ04

> Total Parenteral Nutrition (TPN) Support Service : Nutritional treatment plan

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Total Parenteral Nutrition (TPN) Support Service : Nutritional treatment plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q04Q1 | date |  |  | SI | Date |
| Q04Q2 | time |  |  | SI | Time |
| Q04Q3 | varchar |  |  | SI | Bag and line changed and documented |
| Q04Q4 | varchar |  |  | SI | Summary of treatment plan |
| Q04Q5 | varchar |  |  | SI | Have treatment orders been placed? |
| Q04Q6 | varchar |  |  | SI | Who was present on ward round |
| Q04Q7 | varchar |  |  | SI | Additional comments |
| Q04Q8 | varchar |  |  | SI | Glycaemic control target |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*