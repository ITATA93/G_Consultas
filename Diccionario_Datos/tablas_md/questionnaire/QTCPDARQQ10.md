# questionnaire.QTCPDARQQ10

> Peritoneal Dialysis Assessment Record : Peritonitis

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Peritonitis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | date |  |  | SI | Date |
| Q10Q2 | varchar |  |  | SI | Peritonitis incidence number |
| Q10Q3 | varchar |  |  | SI | Organism |
| Q10Q4 | varchar |  |  | SI | Antibiotic therapy |
| Q10Q5 | varchar |  |  | SI | Outcome |
| Q10Q6 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*