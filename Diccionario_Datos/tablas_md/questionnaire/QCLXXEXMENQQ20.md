# questionnaire.QCLXXEXMENQQ20

> Examen Mental : Desarrollo Psicomotor

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Mental : Desarrollo Psicomotor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | varchar |  |  | SI | Área |
| Q20Q2 | varchar |  |  | SI | Evaluación |
| Q20Q3 | varchar |  |  | SI | Observaciones (texto libre) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*