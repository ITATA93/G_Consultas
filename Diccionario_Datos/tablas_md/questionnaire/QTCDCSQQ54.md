# questionnaire.QTCDCSQQ54

> Diabetes Complication Status : Ulcer examination

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diabetes Complication Status : Ulcer examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q54Q1 | varchar |  |  | SI | Location |
| Q54Q2 | varchar |  |  | SI | Ulcer grade (University of Texas system) |
| Q54Q3 | varchar |  |  | SI | Ulcer stage (University of Texas system) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*