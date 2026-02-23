# questionnaire.QGXXXIVAQQ122

> Intravascular Access : Shift Assessment

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access : Shift Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q122Q1 | date |  |  | SI | Date |
| Q122Q2 | time |  |  | SI | Time |
| Q122Q3 | varchar |  |  | SI | Catheter check |
| Q122Q4 | varchar |  |  | SI | Dressing status |
| Q122Q5 | varchar |  |  | SI | Insertion site check |
| Q122Q6 | varchar |  |  | SI | Visual phlebitis score |
| Q122Q7 | varchar |  |  | SI | Actions |
| Q122Q8 | varchar |  |  | SI | Comments |
| Q122Q9 | varchar |  |  | SI | Staff |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*