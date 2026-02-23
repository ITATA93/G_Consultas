# questionnaire.QTCIPRQQ10

> Insulin Pump Record : Insulin sensitivity factor

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Insulin Pump Record : Insulin sensitivity factor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | time |  |  | SI | Time from |
| Q10Q2 | time |  |  | SI | Time to |
| Q10Q3 | numeric |  |  | SI | Insulin sensitivity factor (mmol/L) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*