# questionnaire.QGXXXSTOMAQQ26

> Stoma : Stoma care

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stoma : Stoma care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q26Q1 | date |  |  | SI | Date |
| Q26Q2 | time |  |  | SI | Time |
| Q26Q3 | varchar |  |  | SI | Peristomal skin care and stoma products |
| Q26Q4 | varchar |  |  | SI | Education provided to patient |
| Q26Q5 | varchar |  |  | SI | Notes |
| Q26Q6 | varchar |  |  | SI | Care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*