# questionnaire.QGXXXSTOMAQQ25

> Stoma : Stoma evaluation

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stoma : Stoma evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q25Q1 | date |  |  | SI | Date |
| Q25Q10 | varchar |  |  | SI | Care provider |
| Q25Q2 | varchar |  |  | SI | Stoma colour |
| Q25Q3 | varchar |  |  | SI | Stoma profile |
| Q25Q4 | varchar |  |  | SI | Skin peristomal |
| Q25Q5 | varchar |  |  | SI | Descriptive bowel consistency |
| Q25Q6 | varchar |  |  | SI | Stoma output |
| Q25Q7 | varchar |  |  | SI | Pain |
| Q25Q8 | varchar |  |  | SI | Pain score |
| Q25Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*