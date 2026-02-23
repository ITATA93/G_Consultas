# questionnaire.QTCDNEQQ82

> Discharge Newborn Examination : Oxygen saturation screening

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Discharge Newborn Examination : Oxygen saturation screening

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q82Q1 | date |  |  | SI | Date |
| Q82Q2 | time |  |  | SI | Time |
| Q82Q3 | varchar |  |  | SI | Screening timeframe |
| Q82Q4 | numeric |  |  | SI | Pre-ductal saturation - hand (%) |
| Q82Q5 | varchar |  |  | SI | Hand laterality |
| Q82Q6 | numeric |  |  | SI | Post-ductal saturation - foot (%) |
| Q82Q7 | varchar |  |  | SI | Foot laterality |
| Q82Q8 | varchar |  |  | SI | Result |
| Q82Q9 | varchar |  |  | SI | Other result |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*