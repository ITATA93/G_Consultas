# questionnaire.QTCPHRAQQ5

> Physiotherapist Rehabilitation Assessment : Clinical stability and secondary damage prevention

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapist Rehabilitation Assessment : Clinical stability and secondary damage prevention

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q5Q1 | varchar |  |  | SI | Micro goal |
| Q5Q2 | varchar |  |  | SI | Timing |
| Q5Q3 | varchar |  |  | SI | Outcome |
| Q5Q4 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*