# questionnaire.QTCFMRQQ01

> Family Meeting Register : Family or other persons present

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Family Meeting Register : Family or other persons present

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Name |
| Q01Q2 | varchar |  |  | SI | Relationship |
| Q01Q3 | varchar |  |  | SI | Relationship |
| Q01Q4 | varchar |  |  | SI | Location |
| Q01Q5 | time |  |  | SI | Time arrived |
| Q01Q6 | time |  |  | SI | Time departed |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*