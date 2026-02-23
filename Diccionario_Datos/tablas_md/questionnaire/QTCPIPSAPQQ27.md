# questionnaire.QTCPIPSAPQQ27

> Physiotherapy Inpatient Post Surgery Assessment and Plan : Joint assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy Inpatient Post Surgery Assessment and Plan : Joint assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q27Q1 | varchar |  |  | SI | Joint |
| Q27Q2 | varchar |  |  | SI | Side |
| Q27Q3 | varchar |  |  | SI | Range of Motion (ROM) |
| Q27Q4 | varchar |  |  | SI | Strength |
| Q27Q5 | varchar |  |  | SI | Straight Leg Raise (SLR) |
| Q27Q6 | varchar |  |  | SI | Quadriceps lag |
| Q27Q7 | varchar |  |  | SI | Inner range quadriceps |
| Q27Q8 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*