# questionnaire.QTCPHRAQQ9

> Physiotherapist Rehabilitation Assessment : Recovery / improvement of  motor / sensory impairments

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapist Rehabilitation Assessment : Recovery / improvement of  motor / sensory impairments

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q9Q1 | varchar |  |  | SI | Micro goal |
| Q9Q2 | varchar |  |  | SI | Timing |
| Q9Q3 | varchar |  |  | SI | Outcome |
| Q9Q4 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*