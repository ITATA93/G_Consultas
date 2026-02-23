# questionnaire.QTCERPPQQ30

> Registro Pertenencias del Paciente : Prótesis Dental

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Pertenencias del Paciente : Prótesis Dental

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | bit |  |  | SI | Sin Prótesis Dental |
| Q30Q2 | varchar |  |  | SI | Ubicación Prótesis |
| Q30Q3 | varchar |  |  | SI | Estado |
| Q30Q4 | varchar |  |  | SI | Tipo de Prótesis |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*