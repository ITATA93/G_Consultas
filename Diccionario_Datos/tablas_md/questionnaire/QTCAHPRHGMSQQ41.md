# questionnaire.QTCAHPRHGMSQQ41

> General MusculoSkeletal Evaluation : Joint assessment

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* General MusculoSkeletal Evaluation : Joint assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q41Q1 | varchar |  |  | SI | Joint |
| Q41Q2 | varchar |  |  | SI | Laterality |
| Q41Q3 | varchar |  |  | SI | Motion |
| Q41Q4 | numeric |  |  | SI | ROM (Degrees) |
| Q41Q5 | varchar |  |  | SI | Muscle power |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*