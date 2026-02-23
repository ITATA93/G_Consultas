# questionnaire.QTCPDARQQ13

> Peritoneal Dialysis Assessment Record : Peritoneal dialysis training

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Peritoneal dialysis training

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q13Q1 | date |  |  | SI | Date |
| Q13Q2 | varchar |  |  | SI | Topic |
| Q13Q3 | varchar |  |  | SI | Evaluation |
| Q13Q4 | varchar |  |  | SI | Plan |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*