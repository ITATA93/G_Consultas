# questionnaire.QTCNOSCQQ09

> Nitric Oxide Safety Checklist : Nitric Oxide Safety Checklist

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nitric Oxide Safety Checklist : Nitric Oxide Safety Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | date |  |  | SI | Date |
| Q09Q2 | time |  |  | SI | Time |
| Q09Q3 | varchar |  |  | SI | Pressure in current cylinder >200 psi |
| Q09Q4 | varchar |  |  | SI | Check replacement cylinder available |
| Q09Q5 | varchar |  |  | SI | Empty water trap |
| Q09Q6 | varchar |  |  | SI | Bagging circuit intact and present |
| Q09Q7 | varchar |  |  | SI | Disc filter changed   (change every 12 hours) |
| Q09Q8 | varchar |  |  | SI | Comments / Variance notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*