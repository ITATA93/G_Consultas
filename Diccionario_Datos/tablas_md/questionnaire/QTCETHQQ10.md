# questionnaire.QTCETHQQ10

> Eczema Treatment History : Treatment history

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Eczema Treatment History : Treatment history

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | varchar |  |  | SI | Treatment |
| Q10Q2 | varchar |  |  | SI | Other treatment |
| Q10Q3 | varchar |  |  | SI | Treatment status |
| Q10Q4 | varchar |  |  | SI | Reason for ceasing |
| Q10Q5 | varchar |  |  | SI | Other reason for ceasing |
| Q10Q6 | varchar |  |  | SI | Treatment notes |
| Q10Q7 | varchar |  |  | SI | Entered by |
| Q10Q8 | date |  |  | SI | Entered date |
| Q10Q9 | time |  |  | SI | Entered time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*