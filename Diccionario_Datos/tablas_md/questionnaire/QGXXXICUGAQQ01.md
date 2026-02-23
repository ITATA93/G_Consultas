# questionnaire.QGXXXICUGAQQ01

> ICU General Assessment Information : IV Access

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ICU General Assessment Information : IV Access

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | IV Access Device |
| Q01Q2 | varchar |  |  | SI | Location |
| Q01Q3 | varchar |  |  | SI | Insertion Site Condition |
| Q01Q4 | numeric |  |  | SI | Days since Insertion or Re-Wire |
| Q01Q5 | varchar |  |  | SI | Comments |
| Q01Q6 | varchar |  |  | SI | Line Number |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*