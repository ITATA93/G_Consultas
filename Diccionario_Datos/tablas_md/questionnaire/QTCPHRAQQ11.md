# questionnaire.QTCPHRAQQ11

> Physiotherapist Rehabilitation Assessment : Transfer recovery

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapist Rehabilitation Assessment : Transfer recovery

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | varchar |  |  | SI | Micro goal |
| Q11Q2 | varchar |  |  | SI | Timing |
| Q11Q3 | varchar |  |  | SI | Outcome |
| Q11Q4 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*