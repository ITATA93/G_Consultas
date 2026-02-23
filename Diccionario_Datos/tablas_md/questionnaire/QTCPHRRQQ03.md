# questionnaire.QTCPHRRQQ03

> Medication History Sources and Checklist : Sources of medicine list

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medication History Sources and Checklist : Sources of medicine list

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Source(s) |
| Q03Q2 | varchar |  |  | SI | Confirmed by |
| Q03Q3 | date |  |  | SI | Date |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*