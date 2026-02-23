# questionnaire.QGXXXIVAQQ133

> Intravascular Access : Haemodialysis shift assessment

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access : Haemodialysis shift assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q133Q1 | date |  |  | SI | Date |
| Q133Q10 | varchar |  |  | SI | Staff |
| Q133Q2 | time |  |  | SI | Time |
| Q133Q3 | varchar |  |  | SI | Arterial lumen |
| Q133Q4 | varchar |  |  | SI | Venous lumen |
| Q133Q5 | varchar |  |  | SI | Unused lumens flushed |
| Q133Q6 | varchar |  |  | SI | Arterial lumen condition |
| Q133Q7 | varchar |  |  | SI | Venous lumen condition |
| Q133Q8 | numeric |  |  | SI | Insertion length at skin (cm) |
| Q133Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*