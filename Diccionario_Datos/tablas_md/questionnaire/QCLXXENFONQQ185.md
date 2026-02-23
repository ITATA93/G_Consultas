# questionnaire.QCLXXENFONQQ185

> Ingreso de Enfermería Oncología : Tipo de Tratamiento

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso de Enfermería Oncología : Tipo de Tratamiento

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q185Q1 | varchar |  |  | SI | Tratamiento |
| Q185Q2 | date |  |  | SI | Fecha de Inicio  |
| Q185Q3 | date |  |  | SI | Fecha de Termino  |
| Q185Q4 | varchar |  |  | SI | Esquema / Tipo / Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*