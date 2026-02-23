# questionnaire.QTCCANQQ24

> Congenital Anomaly Notification : Anomaly description

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Congenital Anomaly Notification : Anomaly description

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q24Q1 | date |  |  | SI | Date |
| Q24Q2 | time |  |  | SI | Time |
| Q24Q3 | varchar |  |  | SI | Care provider |
| Q24Q4 | varchar |  |  | SI | Code |
| Q24Q5 | varchar |  |  | SI | Description |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*