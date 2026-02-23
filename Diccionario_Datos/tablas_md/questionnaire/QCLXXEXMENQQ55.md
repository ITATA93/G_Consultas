# questionnaire.QCLXXEXMENQQ55

> Examen Mental : Piel

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Mental : Piel

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q55Q1 | varchar |  |  | SI | Piel |
| Q55Q2 | varchar |  |  | SI | Evaluación |
| Q55Q3 | varchar |  |  | SI | Comentarios (Texto libre) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*