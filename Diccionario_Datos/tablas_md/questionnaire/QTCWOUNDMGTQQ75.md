# questionnaire.QTCWOUNDMGTQQ75

> Wound Assessment and Care : Treatment Provided

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Treatment Provided

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q75Q1 | date |  |  | SI | Date |
| Q75Q10 | varchar |  |  | SI | Entered by |
| Q75Q2 | varchar |  |  | SI | Treatment |
| Q75Q3 | varchar |  |  | SI | Treatment comments |
| Q75Q4 | varchar |  |  | SI | Primary dressing(s) |
| Q75Q5 | varchar |  |  | SI | Secondary dressing(s) |
| Q75Q6 | varchar |  |  | SI | Dressing comments |
| Q75Q7 | varchar |  |  | SI | Packing count - IN |
| Q75Q8 | varchar |  |  | SI | Packing count - OUT |
| Q75Q9 | varchar |  |  | SI | Pack comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*