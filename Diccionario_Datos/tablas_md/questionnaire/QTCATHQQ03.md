# questionnaire.QTCATHQQ03

> Acne Treatment History : Treatment History

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Acne Treatment History : Treatment History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | date |  |  | SI | Date entered |
| Q03Q2 | time |  |  | SI | Time entered |
| Q03Q3 | varchar |  |  | SI | Treatment |
| Q03Q4 | varchar |  |  | SI | Other treatment |
| Q03Q5 | varchar |  |  | SI | Treatment status |
| Q03Q6 | varchar |  |  | SI | Reason for cessation |
| Q03Q7 | varchar |  |  | SI | Other reason for cessation |
| Q03Q8 | varchar |  |  | SI | Treatment notes |
| Q03Q9 | varchar |  |  | SI | Entered by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*