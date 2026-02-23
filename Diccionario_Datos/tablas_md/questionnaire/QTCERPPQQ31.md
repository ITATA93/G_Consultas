# questionnaire.QTCERPPQQ31

> Registro Pertenencias del Paciente : Lentes

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Pertenencias del Paciente : Lentes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q31Q1 | bit |  |  | SI | Sin Lentes |
| Q31Q2 | varchar |  |  | SI | Tipo de Lentes |
| Q31Q3 | varchar |  |  | SI | Estado |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*