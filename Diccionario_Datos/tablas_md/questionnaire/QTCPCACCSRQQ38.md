# questionnaire.QTCPCACCSRQQ38

> Patient Care Assistant Constant Care Shift Record : Meal consumption

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Care Assistant Constant Care Shift Record : Meal consumption

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q38Q1 | varchar |  |  | SI | Meal type |
| Q38Q2 | varchar |  |  | SI | Amount |
| Q38Q3 | varchar |  |  | SI | Any problems eating or swallowing? |
| Q38Q4 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*