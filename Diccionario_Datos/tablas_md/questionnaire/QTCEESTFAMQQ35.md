# questionnaire.QTCEESTFAMQQ35

> Estructura y Dinámica Familiar : Estructura y dinámica familiar del caso en estudio

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estructura y Dinámica Familiar : Estructura y dinámica familiar del caso en estudio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q35Q1 | date |  |  | SI | Fecha |
| Q35Q2 | varchar |  |  | SI | Normas o reglas observadas en la familia |
| Q35Q3 | varchar |  |  | SI | Roles significativos |
| Q35Q4 | varchar |  |  | SI | Comunicación |
| Q35Q5 | varchar |  |  | SI | Límites |
| Q35Q6 | varchar |  |  | SI | Coaliciones o alianzas |
| Q35Q7 | varchar |  |  | SI | Comportamiento del poder, autoridad y jerarquías e... |
| Q35Q8 | varchar |  |  | SI | Otros subsistemas observados |
| Q35Q9 | varchar |  |  | SI | Profesional |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*