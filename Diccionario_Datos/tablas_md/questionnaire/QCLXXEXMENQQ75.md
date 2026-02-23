# questionnaire.QCLXXEXMENQQ75

> Examen Mental : Examen Neurológico

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Mental : Examen Neurológico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q75Q1 | varchar |  |  | SI | Área |
| Q75Q2 | varchar |  |  | SI | Evaluación |
| Q75Q3 | varchar |  |  | SI | Comentarios (Texto libre) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*