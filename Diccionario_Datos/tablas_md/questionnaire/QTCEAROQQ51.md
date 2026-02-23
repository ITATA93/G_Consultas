# questionnaire.QTCEAROQQ51

> Ingreso Prenatal Alto Riesgo Obstétrico : Hospitalizaciones durante el embarazo actual

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Prenatal Alto Riesgo Obstétrico : Hospitalizaciones durante el embarazo actual

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q51Q1 | numeric |  |  | SI | N° de días  |
| Q51Q2 | varchar |  |  | SI | Motivo de hospitalización |
| Q51Q3 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*