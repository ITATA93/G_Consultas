# questionnaire.QGXXXICUGAQQ02

> ICU General Assessment Information : Drains

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ICU General Assessment Information : Drains

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | numeric |  |  | SI | Drain Number |
| Q02Q2 | varchar |  |  | SI | Location |
| Q02Q3 | numeric |  |  | SI | Drainage Amount / Volume |
| Q02Q4 | varchar |  |  | SI | Drainage Type |
| Q02Q5 | numeric |  |  | SI | Days since Insertion |
| Q02Q6 | varchar |  |  | SI | Insertion Site Condition |
| Q02Q7 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*