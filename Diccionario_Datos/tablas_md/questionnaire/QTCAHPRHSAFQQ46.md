# questionnaire.QTCAHPRHSAFQQ46

> Shoulder Assessment : Muscle Power

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Assessment : Muscle Power

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q46Q1 | varchar |  |  | SI | Muscle |
| Q46Q2 | varchar |  |  | SI | Strength left |
| Q46Q3 | varchar |  |  | SI | Strength right |
| Q46Q4 | varchar |  |  | SI | Resisted isometric test |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*