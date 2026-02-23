# questionnaire.QTCFMRQQ16

> Family Meeting Register : Interpreters present

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Family Meeting Register : Interpreters present

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q16Q1 | varchar |  |  | SI | Name |
| Q16Q2 | varchar |  |  | SI | Language |
| Q16Q3 | time |  |  | SI | Time arrived |
| Q16Q4 | time |  |  | SI | Time departed |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*