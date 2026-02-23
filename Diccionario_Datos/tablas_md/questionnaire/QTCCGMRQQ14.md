# questionnaire.QTCCGMRQQ14

> Continuous Glucose Monitoring Record : Basal rate settings (units / hour)

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Continuous Glucose Monitoring Record : Basal rate settings (units / hour)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q14Q1 | time |  |  | SI | Time from |
| Q14Q2 | time |  |  | SI | Time to |
| Q14Q3 | numeric |  |  | SI | Units / hour |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*