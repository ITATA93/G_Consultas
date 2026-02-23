# questionnaire.QTCIVFFSHQQ21A

> Fertility Screening History : Ovulation induction table

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fertility Screening History : Ovulation induction table

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21AQ1 | numeric |  |  | SI | Clomid no of cycles |
| Q21AQ2 | numeric |  |  | SI | HMG no of cycles |
| Q21AQ3 | varchar |  |  | SI | Clomid ovulation |
| Q21AQ4 | varchar |  |  | SI | Clomid pregnancy |
| Q21AQ5 | varchar |  |  | SI | HMG ovulation |
| Q21AQ6 | varchar |  |  | SI | Gonadotrophin pregnancy |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*