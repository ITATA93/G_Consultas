# questionnaire.QTCSDMQQ10

> Shoulder Dystocia Management : Staff present

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Dystocia Management : Staff present

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | varchar |  |  | SI | Name |
| Q10Q2 | varchar |  |  | SI | Role |
| Q10Q3 | varchar |  |  | SI | Presence |
| Q10Q4 | time |  |  | SI | Arrival time |
| Q10Q5 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*