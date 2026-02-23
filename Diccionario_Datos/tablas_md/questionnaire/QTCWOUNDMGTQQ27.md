# questionnaire.QTCWOUNDMGTQQ27

> Wound Assessment and Care : Structured Treatment Plan

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Structured Treatment Plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q27Q1 | varchar |  |  | SI | Plan item |
| Q27Q2 | varchar |  |  | SI | Other |
| Q27Q3 | varchar |  |  | SI | Detail and Comment |
| Q27Q4 | varchar |  |  | SI | Entered by |
| Q27Q5 | date |  |  | SI | Date  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*