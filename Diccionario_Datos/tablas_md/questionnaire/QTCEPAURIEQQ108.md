# questionnaire.QTCEPAURIEQQ108

> Evaluación del Riesgo Familiar : Historial de Atención Familiar

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación del Riesgo Familiar : Historial de Atención Familiar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q108Q1 | date |  |  | SI | Fecha |
| Q108Q2 | varchar |  |  | SI | Registro de la Atención |
| Q108Q3 | varchar |  |  | SI | Profesional |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*