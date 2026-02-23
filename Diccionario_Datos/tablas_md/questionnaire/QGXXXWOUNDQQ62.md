# questionnaire.QGXXXWOUNDQQ62

> Wound Management : Medical Review

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management : Medical Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q62Q1 | varchar |  |  | SI | Requested |
| Q62Q2 | date |  |  | SI | Request date |
| Q62Q3 | varchar |  |  | SI | Completed |
| Q62Q4 | date |  |  | SI | Completed date |
| Q62Q5 | varchar |  |  | SI | Review notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*