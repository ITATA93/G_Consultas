# questionnaire.QCLXXEVAEXTQQ01

> Evaluaciones Externas  : Pauta Aplicada

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluaciones Externas  : Pauta Aplicada

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Listado de Evaluaciones |
| Q01Q2 | varchar |  |  | SI | Resultado 1 |
| Q01Q3 | varchar |  |  | SI | Resultado 2 |
| Q01Q4 | varchar |  |  | SI | Resultado 3 |
| Q01Q5 | varchar |  |  | SI | Resultado 4 |
| Q01Q6 | varchar |  |  | SI | Observaciones Adicionles |
| Q01Q7 | varchar |  |  | SI | Otra Medición |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*