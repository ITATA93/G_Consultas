# questionnaire.QCLXXEFPEDQQ65

> Examen Físico Pediátrico : Extremidades

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico : Extremidades

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q65Q1 | varchar |  |  | SI | Hallazgos |
| Q65Q2 | varchar |  |  | SI | Extremidad superior |
| Q65Q3 | varchar |  |  | SI | Extremidad inferior |
| Q65Q4 | varchar |  |  | SI | Topografía |
| Q65Q5 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*