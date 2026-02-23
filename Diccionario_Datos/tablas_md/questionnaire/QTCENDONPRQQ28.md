# questionnaire.QTCENDONPRQQ28

> Endoscopy Nursing Procedure Report : Lower Endoscopy Specimens & Interventions

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Nursing Procedure Report : Lower Endoscopy Specimens & Interventions

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q28Q1 | varchar |  |  | SI | Intervention |
| Q28Q2 | varchar |  |  | SI | Location |
| Q28Q3 | varchar |  |  | SI | Other location |
| Q28Q4 | numeric |  |  | SI | Number |
| Q28Q5 | varchar |  |  | SI | Specimen removal and treatment methods |
| Q28Q6 | varchar |  |  | SI | Other methods |
| Q28Q7 | varchar |  |  | SI | Retrieved |
| Q28Q8 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*