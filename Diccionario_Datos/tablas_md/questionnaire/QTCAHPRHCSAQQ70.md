# questionnaire.QTCAHPRHCSAQQ70

> Cervical Spine Assessment : Test Movement Describe Effect on Present Pain

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cervical Spine Assessment : Test Movement Describe Effect on Present Pain

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q70Q1 | varchar |  |  | SI | Pretest Symptoms Sitting |
| Q70Q2 | varchar |  |  | SI | Pretest Symptoms Lying |
| Q70Q3 | varchar |  |  | SI | If required pretest symptoms |
| Q70Q4 | varchar |  |  | SI | Symptoms During Testing |
| Q70Q5 | varchar |  |  | SI | Symptoms After Testing |
| Q70Q6 | varchar |  |  | SI | Mechanical Response |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*