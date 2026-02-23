# questionnaire.QTCWOUNDMGTQQ70

> Wound Assessment and Care : Measurements & Images

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Measurements & Images

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q70Q1 | date |  |  | SI | Date |
| Q70Q10 | varchar |  |  | SI | Entered by |
| Q70Q2 | numeric |  |  | SI | Max length (cm) |
| Q70Q3 | numeric |  |  | SI | Max width (cm) |
| Q70Q4 | numeric |  |  | SI | Max depth (cm) |
| Q70Q5 | varchar |  |  | SI | Sinus Tract |
| Q70Q6 | varchar |  |  | SI | Tunnelling / Undermining |
| Q70Q7 | varchar |  |  | SI | Pressure injury stage |
| Q70Q8 | varchar |  |  | SI | Add image |
| Q70Q9 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*