# questionnaire.QGXXXIVAQQ85

> Intravascular Access : IABP Checks

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access : IABP Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q85Q3 | varchar |  |  | SI | Comments |
| Q85Q4 | varchar |  |  | SI | Staff |
| Q85Q5 | date |  |  | SI | Date |
| Q85Q6 | time |  |  | SI | Time |
| Q86Q1 | varchar |  |  | SI | Checklist |
| Q86Q2 | varchar |  |  | SI | Helium level in cylinder |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*