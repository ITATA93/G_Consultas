# questionnaire.QGXXXICUTRAQQ06

> Tracheostomy Daily Assessment : Daily Assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tracheostomy Daily Assessment : Daily Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Date |
| Q06Q2 | time |  |  | SI | Time |
| Q06Q3 | varchar |  |  | SI | Staff Name |
| Q06Q4 | varchar |  |  | SI | Check |
| Q06Q5 | varchar |  |  | SI | Actions |
| Q06Q6 | varchar |  |  | SI | Daily Assessment Notes |
| Q06Q7 | numeric |  |  | SI | Cuff Pressure |
| Q06Q8 | numeric |  |  | SI | Leak Volume |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*