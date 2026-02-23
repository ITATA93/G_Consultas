# questionnaire.QTCDSEQQ12

> Dobutamine Stress Echocardiogram : Post Dobutamine Infusion

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dobutamine Stress Echocardiogram : Post Dobutamine Infusion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q12Q1 | time |  |  | SI | Time |
| Q12Q2 | numeric |  |  | SI | Heart rate (/min) |
| Q12Q3 | numeric |  |  | SI | Systolic BP (mmHg) |
| Q12Q4 | numeric |  |  | SI | Diastolic BP (mmHg) |
| Q12Q5 | varchar |  |  | SI | ECG result |
| Q12Q6 | varchar |  |  | SI | Patient symptoms |
| Q12Q7 | varchar |  |  | SI | Other details |
| Q12Q8 | varchar |  |  | SI | Medication given post testing |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*