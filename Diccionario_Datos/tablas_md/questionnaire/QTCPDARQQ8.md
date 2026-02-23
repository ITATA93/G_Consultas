# questionnaire.QTCPDARQQ8

> Peritoneal Dialysis Assessment Record : Nasal swab

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Nasal swab

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q8Q1 | date |  |  | SI | Date |
| Q8Q2 | varchar |  |  | SI | Taken for |
| Q8Q3 | varchar |  |  | SI | Result |
| Q8Q4 | varchar |  |  | SI | Treatment |
| Q8Q5 | varchar |  |  | SI | Comment |
| Q8Q6 | varchar |  |  | SI | Taken by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*