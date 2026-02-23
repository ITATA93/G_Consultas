# questionnaire.QTCPOSTEDQQ20

> Postpartum Emergency Documentation : Add action(s) for Dummy1

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add action(s) for Dummy1

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | numeric |  |  | SI | Action order number |
| Q20Q2 | time |  |  | SI | Time stamp |
| Q20Q3 | varchar |  |  | SI | Action type |
| Q20Q4 | varchar |  |  | SI | Other (specify) |
| Q20Q5 | varchar |  |  | SI | By whom |
| Q20Q6 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*