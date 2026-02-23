# questionnaire.QTCIPRQQ08

> Insulin Pump Record : Basal insulin infusion rate

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Insulin Pump Record : Basal insulin infusion rate

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | time |  |  | SI | Time from |
| Q08Q2 | time |  |  | SI | Time to |
| Q08Q3 | numeric |  |  | SI | Basal insulin infusion rate (units/hr) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*