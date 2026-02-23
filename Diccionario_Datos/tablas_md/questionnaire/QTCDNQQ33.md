# questionnaire.QTCDNQQ33

> Death Notification : Call notification history

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Death Notification : Call notification history

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q33Q1 | numeric |  |  | SI | Phone number |
| Q33Q2 | varchar |  |  | SI | Call attempt number |
| Q33Q3 | varchar |  |  | SI | Call answered |
| Q33Q4 | time |  |  | SI | Time of attempt |
| Q33Q5 | varchar |  |  | SI | Responder name |
| Q33Q6 | varchar |  |  | SI | Relationship |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*