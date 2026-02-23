# questionnaire.QGXXXPPQQ05

> Patient Property and Belongings : Cash

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Property and Belongings : Cash

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | varchar |  |  | SI | Banknotes |
| Q05Q2 | numeric |  |  | SI | Number |
| Q05Q3 | numeric |  |  | SI | Coins combined |
| Q05Q4 | varchar |  |  | SI | Currency |
| Q05Q5 | numeric |  |  | SI | Total amount |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*