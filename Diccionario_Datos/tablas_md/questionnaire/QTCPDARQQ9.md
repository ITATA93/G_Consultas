# questionnaire.QTCPDARQQ9

> Peritoneal Dialysis Assessment Record : Exit site condition

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Exit site condition

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q9Q1 | date |  |  | SI | Date |
| Q9Q2 | varchar |  |  | SI | Condition of the wound |
| Q9Q3 | varchar |  |  | SI | Culture taken |
| Q9Q4 | varchar |  |  | SI | Organism |
| Q9Q5 | varchar |  |  | SI | Treatment |
| Q9Q6 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*