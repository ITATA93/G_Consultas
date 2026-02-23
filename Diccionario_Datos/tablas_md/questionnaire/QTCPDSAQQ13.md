# questionnaire.QTCPDSAQQ13

> Peritoneal Dialysis Suitability Assessment : Carer details

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Carer details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q13Q1 | varchar |  |  | SI | Carer name |
| Q13Q2 | varchar |  |  | SI | Occupation / Community status |
| Q13Q3 | varchar |  |  | SI | Carer willing / able to support |
| Q13Q4 | varchar |  |  | SI | Support |
| Q13Q5 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*