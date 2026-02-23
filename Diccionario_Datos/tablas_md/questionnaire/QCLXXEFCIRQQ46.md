# questionnaire.QCLXXEFCIRQQ46

> Examen Físico : Pulsos

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico : Pulsos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q46Q1 | varchar |  |  | SI | Pulso |
| Q46Q2 | varchar |  |  | SI | lateralidad |
| Q46Q3 | varchar |  |  | SI | Hallazgos |
| Q46Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*