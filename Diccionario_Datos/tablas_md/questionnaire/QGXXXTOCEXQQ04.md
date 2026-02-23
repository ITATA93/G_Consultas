# questionnaire.QGXXXTOCEXQQ04

> Toxic Exposure : Exposure details

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Toxic Exposure : Exposure details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q04Q1 | varchar |  |  | SI | Toxin |
| Q04Q2 | varchar |  |  | SI | Strength / concentration |
| Q04Q3 | varchar |  |  | SI | Quantity or volume |
| Q04Q4 | varchar |  |  | SI | Route of exposure |
| Q04Q5 | time |  |  | SI | Time of exposure |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*