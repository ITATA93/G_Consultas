# questionnaire.QTCPOSTEDQQ10

> Postpartum Emergency Documentation : Add action(s) for amniotic fluid embolism event

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add action(s) for amniotic fluid embolism event

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | numeric |  |  | SI | Action order number |
| Q10Q2 | time |  |  | SI | Time stamp |
| Q10Q3 | varchar |  |  | SI | Action type |
| Q10Q4 | varchar |  |  | SI | Other (specify) |
| Q10Q5 | varchar |  |  | SI | By whom |
| Q10Q6 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*