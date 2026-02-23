# questionnaire.QTCEINGUPCQQ71

> INGRESO UNIDAD DE PACIENTE CRÍTICO : Extremidades

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO : Extremidades

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q71Q1 | varchar |  |  | SI | Hallazgos |
| Q71Q2 | varchar |  |  | SI | Extremidad superior |
| Q71Q3 | varchar |  |  | SI | Extremidad inferior |
| Q71Q4 | varchar |  |  | SI | Ubicación |
| Q71Q5 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*