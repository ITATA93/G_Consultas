# questionnaire.QCLXXEFPEDQQ51

> Examen Físico Pediátrico : Pulmón

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico : Pulmón

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q51Q1 | varchar |  |  | SI | Percusión |
| Q51Q2 | varchar |  |  | SI | Auscultación |
| Q51Q3 | varchar |  |  | SI | Localización |
| Q51Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*