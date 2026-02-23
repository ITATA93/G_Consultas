# questionnaire.QCLXXEFPEDQQ36

> Examen Físico Pediátrico : Oídos

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico : Oídos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q36Q1 | varchar |  |  | SI | Hallazgos |
| Q36Q2 | varchar |  |  | SI | Ubicación |
| Q36Q3 | varchar |  |  | SI | Lateralidad |
| Q36Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*