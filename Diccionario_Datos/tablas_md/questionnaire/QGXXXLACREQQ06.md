# questionnaire.QGXXXLACREQQ06

> Laceration Repair  : Laceration repair

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Laceration Repair  : Laceration repair

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Date |
| Q06Q2 | time |  |  | SI | Time |
| Q06Q3 | varchar |  |  | SI | Anesthesia |
| Q06Q4 | varchar |  |  | SI | Layer |
| Q06Q5 | varchar |  |  | SI | Material |
| Q06Q6 | varchar |  |  | SI | Note |
| Q06Q7 | varchar |  |  | SI | Size |
| Q06Q8 | numeric |  |  | SI | No. |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*