# questionnaire.QTCAHPRHSAFQQ42

> Shoulder Assessment : Range of  Motion (ROM)

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Assessment : Range of  Motion (ROM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q42Q1 | varchar |  |  | SI | Joint / Motion |
| Q42Q2 | numeric |  |  | SI | AROM left |
| Q42Q3 | numeric |  |  | SI | PROM left |
| Q42Q4 | numeric |  |  | SI | AROM right |
| Q42Q5 | numeric |  |  | SI | PROM right |
| Q42Q6 | varchar |  |  | SI | End feel |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*