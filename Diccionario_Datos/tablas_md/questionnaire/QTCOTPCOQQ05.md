# questionnaire.QTCOTPCOQQ05

> Perioperative - Procedural Count : Interim / change of staff check

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Procedural Count : Interim / change of staff check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | varchar |  |  | SI | Are swabs, sharps and instruments correct? |
| Q05Q2 | varchar |  |  | SI | Theatre scrub practitioner |
| Q05Q3 | varchar |  |  | SI | Theatre circulator |
| Q05Q4 | time |  |  | SI | Time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*