# questionnaire.QTCEAROQQ32

> Ingreso Prenatal Alto Riesgo Obstétrico : Tipo de aborto

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Prenatal Alto Riesgo Obstétrico : Tipo de aborto

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | date |  |  | SI | Fecha de aborto |
| Q32Q3 | varchar |  |  | SI | Comentario |
| Q32Q4 | varchar |  |  | SI | Tipo de Aborto |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*