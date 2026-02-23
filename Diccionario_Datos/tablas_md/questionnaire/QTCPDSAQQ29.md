# questionnaire.QTCPDSAQQ29

> Peritoneal Dialysis Suitability Assessment : Mobility

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Mobility

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q29Q1 | varchar |  |  | SI | Mobility assessment for |
| Q29Q2 | varchar |  |  | SI | Walking aids |
| Q29Q3 | varchar |  |  | SI | Amputation |
| Q29Q4 | varchar |  |  | SI | Location of amputation (if applicable) |
| Q29Q5 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*