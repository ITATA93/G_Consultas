# questionnaire.QGXXXRESUSQQ87

> Resuscitation Report : Defibrillation details

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Resuscitation Report : Defibrillation details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q87Q1 | numeric |  |  | SI | Joules given |
| Q87Q2 | varchar |  |  | SI | Care provider |
| Q87Q3 | date |  |  | SI | Date |
| Q87Q4 | time |  |  | SI | Time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*