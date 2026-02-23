# questionnaire.QTCPOSTEDQQ09

> Postpartum Emergency Documentation : Add action(s) for postpartum haemorrhage event

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add action(s) for postpartum haemorrhage event

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | numeric |  |  | SI | Action order number |
| Q09Q2 | time |  |  | SI | Time stamp |
| Q09Q3 | varchar |  |  | SI | Action type |
| Q09Q4 | varchar |  |  | SI | Other (specify) |
| Q09Q5 | varchar |  |  | SI | By whom |
| Q09Q6 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*