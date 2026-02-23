# questionnaire.QTCGDAQQ46

> General Drain Access : Daily shift assessment

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* General Drain Access : Daily shift assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q46Q1 | date |  |  | SI | Date |
| Q46Q2 | time |  |  | SI | Time |
| Q46Q3 | varchar |  |  | SI | Note |
| Q46Q4 | varchar |  |  | SI | Actions |
| Q46Q5 | varchar |  |  | SI | Drain Check |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*