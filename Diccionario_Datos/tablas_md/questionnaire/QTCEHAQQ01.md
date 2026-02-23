# questionnaire.QTCEHAQQ01

> Hospitalización Abreviada : Protocolo

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hospitalización Abreviada : Protocolo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | ETAPA |
| Q01Q2 | time |  |  | SI | HORA DE ATENCIÓN |
| Q01Q3 | numeric |  |  | SI | SCORE DE TAL MODIFICADO (SBO) |
| Q01Q4 | numeric |  |  | SI | SATURACIÓN DE OXÍGENO |
| Q01Q5 | varchar |  |  | SI | INHALOTERAPIA |
| Q01Q6 | varchar |  |  | SI | APLICACIÓN DE OXÍGENO |
| Q01Q7 | varchar |  |  | SI | KINESIOTERAPIA RESPIRATORIA |
| Q01Q8 | varchar |  |  | SI | OBSERVACIONES |
| Q01Q9 | varchar |  |  | SI | DERIVACIÓN |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*