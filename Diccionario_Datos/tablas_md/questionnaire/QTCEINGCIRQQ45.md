# questionnaire.QTCEINGCIRQQ45

> Ingreso Cirugía : Extremidades

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Cirugía : Extremidades

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q45Q1 | varchar |  |  | SI | Hallazgos |
| Q45Q2 | varchar |  |  | SI | Ext. Superior |
| Q45Q3 | varchar |  |  | SI | Ext. Inferior |
| Q45Q4 | varchar |  |  | SI | Topografía |
| Q45Q5 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*