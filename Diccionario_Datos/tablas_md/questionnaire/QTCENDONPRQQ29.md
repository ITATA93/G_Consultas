# questionnaire.QTCENDONPRQQ29

> Endoscopy Nursing Procedure Report : Bronchoscopy Sampling

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Nursing Procedure Report : Bronchoscopy Sampling

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q29Q1 | varchar |  |  | SI | Intervention |
| Q29Q2 | varchar |  |  | SI | Location |
| Q29Q3 | varchar |  |  | SI | Location other |
| Q29Q4 | numeric |  |  | SI | Number of samples |
| Q29Q5 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*