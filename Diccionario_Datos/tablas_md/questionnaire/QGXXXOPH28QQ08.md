# questionnaire.QGXXXOPH28QQ08

> OPH - Excimer Laser/Intralase/Cross-Linking Intra-Operative Record : Items count

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* OPH - Excimer Laser/Intralase/Cross-Linking Intra-Operative Record : Items count

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | varchar |  |  | SI | Item |
| Q08Q2 | varchar |  |  | SI | 1st Count |
| Q08Q3 | bit |  |  | SI | Complete |
| Q08Q4 | bit |  |  | SI | Incomplete |
| Q08Q5 | varchar |  |  | SI | Final Count |
| Q08Q6 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*