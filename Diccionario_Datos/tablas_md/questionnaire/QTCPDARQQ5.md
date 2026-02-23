# questionnaire.QTCPDARQQ5

> Peritoneal Dialysis Assessment Record : Pd catheter

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Pd catheter

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q5Q1 | date |  |  | SI | Insertion date |
| Q5Q2 | varchar |  |  | SI | Surgeon |
| Q5Q3 | varchar |  |  | SI | Type of catheter |
| Q5Q4 | varchar |  |  | SI | Complication |
| Q5Q5 | varchar |  |  | SI | Addtional details |
| Q5Q6 | date |  |  | SI | Removal date |
| Q5Q7 | varchar |  |  | SI | Reason for removal |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*