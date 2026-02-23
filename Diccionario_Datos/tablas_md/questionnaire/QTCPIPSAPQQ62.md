# questionnaire.QTCPIPSAPQQ62

> Physiotherapy Inpatient Post Surgery Assessment and Plan : Continuous Passive Motion

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy Inpatient Post Surgery Assessment and Plan : Continuous Passive Motion

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q62Q1 | varchar |  |  | SI | Side |
| Q62Q2 | varchar |  |  | SI | Range of motion |
| Q62Q3 | varchar |  |  | SI | Frequency |
| Q62Q4 | varchar |  |  | SI | Duration |
| Q62Q5 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*