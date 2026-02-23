# questionnaire.QGXXXICUGAQQ03

> ICU General Assessment Information : Dressings

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ICU General Assessment Information : Dressings

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Dressing Location |
| Q03Q2 | varchar |  |  | SI | Dressing Type |
| Q03Q3 | varchar |  |  | SI | Dressing Condition |
| Q03Q4 | varchar |  |  | SI | Exudate |
| Q03Q5 | varchar |  |  | SI | Odour |
| Q03Q6 | varchar |  |  | SI | Next Scheduled Dressing Change |
| Q03Q7 | varchar |  |  | SI | Wound Examination. Size (Length / Width / Depth in... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*