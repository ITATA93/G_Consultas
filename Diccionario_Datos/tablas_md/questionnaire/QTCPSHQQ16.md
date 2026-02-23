# questionnaire.QTCPSHQQ16

> Psoriasis History : Treatment history

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psoriasis History : Treatment history

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q16Q1 | varchar |  |  | SI | Treatment |
| Q16Q2 | date |  |  | SI | Entered date |
| Q16Q3 | time |  |  | SI | Entered time |
| Q16Q4 | varchar |  |  | SI | Other treatment |
| Q16Q5 | varchar |  |  | SI | Treatment status |
| Q16Q6 | varchar |  |  | SI | Reason for ceasing |
| Q16Q7 | varchar |  |  | SI | Other reason for ceasing |
| Q16Q8 | varchar |  |  | SI | Treatment notes |
| Q16Q9 | varchar |  |  | SI | Entered by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*