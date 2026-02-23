# questionnaire.QTCIPRQQ11

> "Insulin Pump Record : Blood glucose concentration target	"

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Insulin Pump Record : Blood glucose concentration target	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | time |  |  | SI | Time from |
| Q11Q2 | time |  |  | SI | Time to |
| Q11Q3 | numeric |  |  | SI | Blood glucose concentration target (mmol/L) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*