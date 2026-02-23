# questionnaire.QTCEFRMEMPQQR119

> Examen Anual de Medicina Preventiva Del Adulto Mayor (EMPAM) : Vacunación del Adulto Mayor

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Anual de Medicina Preventiva Del Adulto Mayor (EMPAM) : Vacunación del Adulto Mayor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QR119Q1 | varchar |  |  | SI | Vacunas |
| QR119Q2 | varchar |  |  | SI | Aplicación |
| QR119Q3 | date |  |  | SI | Fecha |
| QR119Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*