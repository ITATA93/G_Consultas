# questionnaire.QTCPOMOAQQ06

> Patient's Own Medications on Admission : Restricted / Scheduled medication storage details

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient's Own Medications on Admission : Restricted / Scheduled medication storage details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | varchar |  |  | SI | Medication |
| Q06Q2 | varchar |  |  | SI | Strength |
| Q06Q3 | varchar |  |  | SI | Quantity |
| Q06Q4 | varchar |  |  | SI | Storage location |
| Q06Q5 | varchar |  |  | SI | Other storage location |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*