# questionnaire.QTCPOSTEDQQ12

> Postpartum Emergency Documentation : Add action(s)

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add action(s)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q12Q1 | numeric |  |  | SI | Action order number |
| Q12Q2 | time |  |  | SI | Time stamp |
| Q12Q3 | varchar |  |  | SI | Action type |
| Q12Q4 | varchar |  |  | SI | By whom |
| Q12Q5 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*