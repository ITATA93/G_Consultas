# questionnaire.QTCEFRCPQQ11

> Ficha Registro Cuidados Paliativos y Alivio del Dolor : Características del dolor

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Registro Cuidados Paliativos y Alivio del Dolor : Características del dolor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | varchar |  |  | SI | Lugar del Dolor |
| Q11Q2 | varchar |  |  | SI | Cronología: Duración/Temporalidad |
| Q11Q3 | varchar |  |  | SI | Topografía: Localización |
| Q11Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*