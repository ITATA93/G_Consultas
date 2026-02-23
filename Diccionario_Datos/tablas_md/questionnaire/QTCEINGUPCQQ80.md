# questionnaire.QTCEINGUPCQQ80

> INGRESO UNIDAD DE PACIENTE CRÍTICO : Motor

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO : Motor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q80Q1 | varchar |  |  | SI | Hallazgos |
| Q80Q2 | varchar |  |  | SI | Ubicación |
| Q80Q3 | varchar |  |  | SI | Lateralidad |
| Q80Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*