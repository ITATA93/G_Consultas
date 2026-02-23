# questionnaire.QTCTPACQQ06

> Transdermal Patch Administration Checks : Patch Assessment

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Transdermal Patch Administration Checks : Patch Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Date |
| Q06Q2 | time |  |  | SI | Time |
| Q06Q3 | varchar |  |  | SI | Skin condition |
| Q06Q4 | varchar |  |  | SI | Other skin condition |
| Q06Q5 | varchar |  |  | SI | Patch adhesion to skin |
| Q06Q6 | varchar |  |  | SI | Action taken |
| Q06Q7 | varchar |  |  | SI | Assessed by |
| Q06Q8 | varchar |  |  | SI | Assessment notes |
| Q06Q9 | varchar |  |  | SI | Action taken - Other notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*