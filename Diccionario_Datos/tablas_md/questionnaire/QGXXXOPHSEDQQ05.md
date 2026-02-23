# questionnaire.QGXXXOPHSEDQQ05

> Sedation : PARR Table

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Sedation : PARR Table

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | varchar |  |  | SI | Activity |
| Q05Q2 | varchar |  |  | SI | Respiration |
| Q05Q3 | varchar |  |  | SI | Circulation |
| Q05Q4 | varchar |  |  | SI | Consciousness |
| Q05Q5 | varchar |  |  | SI | Pulse Oximetry on room air |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*