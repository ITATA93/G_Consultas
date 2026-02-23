# questionnaire.QTCWWIFLBQQ12

> Warm Water Immersion For Labour / Birth : Water immersion record

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Warm Water Immersion For Labour / Birth : Water immersion record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q12Q1 | date |  |  | SI | Date / Time entered water |
| Q12Q2 | time |  |  | SI | Time entered water |
| Q12Q3 | varchar |  |  | SI | Reason for exiting water |
| Q12Q4 | varchar |  |  | SI | Compliance with clinical decision |
| Q12Q5 | date |  |  | SI | Date / Time exited water |
| Q12Q6 | time |  |  | SI | Time exited water |
| Q12Q7 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*