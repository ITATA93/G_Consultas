# questionnaire.QTCDSEQQ11

> Dobutamine Stress Echocardiogram : During Dobutamine Infusion

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dobutamine Stress Echocardiogram : During Dobutamine Infusion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | time |  |  | SI | Time |
| Q11Q10 | varchar |  |  | SI | Medication given during testing |
| Q11Q2 | numeric |  |  | SI | Dobutamine (mcg/kg/min) |
| Q11Q3 | numeric |  |  | SI | Rate (microdrop/min) |
| Q11Q4 | numeric |  |  | SI | Heart rate (/min) |
| Q11Q5 | numeric |  |  | SI | Systolic BP (mmHg) |
| Q11Q6 | numeric |  |  | SI | Diastolic BP (mmHg) |
| Q11Q7 | varchar |  |  | SI | ECG result |
| Q11Q8 | varchar |  |  | SI | Patient symptoms |
| Q11Q9 | varchar |  |  | SI | Other details |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*