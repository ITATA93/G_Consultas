# questionnaire.QTCOTPCOQQ06

> Perioperative - Procedural Count : Procedural final count

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Procedural Count : Procedural final count

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | varchar |  |  | SI | Procedure |
| Q06Q2 | varchar |  |  | SI | Item |
| Q06Q3 | varchar |  |  | SI | Other |
| Q06Q4 | numeric |  |  | SI | Count |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*