# questionnaire.QTCVPQQ09

> Custody and Visitation Arrangements : Persons permitted to visit patient

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Custody and Visitation Arrangements : Persons permitted to visit patient

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | varchar |  |  | SI | Name |
| Q09Q2 | varchar |  |  | SI | Relationship |
| Q09Q3 | varchar |  |  | SI | Address |
| Q09Q4 | varchar |  |  | SI | Phone |
| Q09Q5 | varchar |  |  | SI | Permission to take patient on ward leave |
| Q09Q6 | varchar |  |  | SI | Permission to take patient within hospital campus |
| Q09Q7 | varchar |  |  | SI | Requires supervised visit |
| Q09Q8 | varchar |  |  | SI | Dummy1 |
| Q09Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*