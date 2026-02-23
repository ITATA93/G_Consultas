# questionnaire.QCLXXEFRNQQ21

> Examen Físico del Recién Nacido : Ojos Alterados

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico del Recién Nacido : Ojos Alterados

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | varchar |  |  | SI | Ojo |
| Q21Q2 | varchar |  |  | SI | Cuadrante |
| Q21Q3 | varchar |  |  | SI | Comentarios |
| Q21Q4 | varchar |  |  | SI | Hemorragia Subconjuntival |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*