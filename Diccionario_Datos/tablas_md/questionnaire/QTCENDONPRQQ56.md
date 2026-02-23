# questionnaire.QTCENDONPRQQ56

> Endoscopy Nursing Procedure Report : Scope Register

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Nursing Procedure Report : Scope Register

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q56Q1 | varchar |  |  | SI | Scope type |
| Q56Q2 | varchar |  |  | SI | Scope number |
| Q56Q3 | time |  |  | SI | Insertion time |
| Q56Q4 | time |  |  | SI | Removal time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*