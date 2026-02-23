# questionnaire.QTCEINGMEDQQ112

> Ingreso Medicina Interna : Pulsos periféricos

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Medicina Interna : Pulsos periféricos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q112Q1 | varchar |  |  | SI | Pulsos |
| Q112Q2 | varchar |  |  | SI | Lateralidad |
| Q112Q3 | varchar |  |  | SI | Hallazgos |
| Q112Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*