# questionnaire.QCLXXEFRNQQ70

> Examen Físico del Recién Nacido : Extremidades Alteradas

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico del Recién Nacido : Extremidades Alteradas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q70Q1 | varchar |  |  | SI | Lesión |
| Q70Q2 | varchar |  |  | SI | Segmento |
| Q70Q3 | varchar |  |  | SI | Lateralidad |
| Q70Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*