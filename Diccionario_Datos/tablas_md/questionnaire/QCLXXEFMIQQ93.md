# questionnaire.QCLXXEFMIQQ93

> Examen Físico Medicina : Cardíaco

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Medicina : Cardíaco

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q93Q1 | varchar |  |  | SI | Ritmo |
| Q93Q2 | varchar |  |  | SI | Ruidos |
| Q93Q3 | varchar |  |  | SI | Soplos |
| Q93Q4 | varchar |  |  | SI | Grado (soplo) |
| Q93Q5 | varchar |  |  | SI | Ubicación |
| Q93Q6 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*