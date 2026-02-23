# questionnaire.QTCWOUNDMGTQQ72

> Wound Assessment and Care : Wound Bed

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Wound Bed

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q72Q1 | date |  |  | SI | Date |
| Q72Q10 | varchar |  |  | SI | Signs of Infection |
| Q72Q2 | varchar |  |  | SI | Tissue at base |
| Q72Q3 | varchar |  |  | SI | Tissue at base comments |
| Q72Q4 | varchar |  |  | SI | Exudate |
| Q72Q5 | varchar |  |  | SI | Signs of infection |
| Q72Q6 | varchar |  |  | SI | Swab taken? |
| Q72Q7 | varchar |  |  | SI | Wound bed comments |
| Q72Q8 | varchar |  |  | SI | Entered by |
| Q72Q9 | varchar |  |  | SI | Overall trend	 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*