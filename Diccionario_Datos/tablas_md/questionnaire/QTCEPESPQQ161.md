# questionnaire.QTCEPESPQQ161

> Doc. Intra-Operatoria Proc. Específicos : Requisitos de vencimientos

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Doc. Intra-Operatoria Proc. Específicos : Requisitos de vencimientos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q161Q1 | varchar |  |  | SI | Items |
| Q161Q10 | bit |  |  | SI | No Aplica |
| Q161Q2 | varchar |  |  | SI | Otro |
| Q161Q3 | varchar |  |  | SI | Descripción del Item |
| Q161Q4 | date |  |  | SI | Fecha de Vencimiento |
| Q161Q5 | varchar |  |  | SI | Control de Viraje |
| Q161Q6 | varchar |  |  | SI | Comentarios |
| Q161Q7 | varchar |  |  | SI | N° de Lote |
| Q161Q8 | varchar |  |  | SI | N° de Serie |
| Q161Q9 | varchar |  |  | SI | Modelo |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*