# questionnaire.QCLXXEFMIQQ89

> Examen Físico Medicina : Pulmonar

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Medicina : Pulmonar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q89Q1 | varchar |  |  | SI | Percusión |
| Q89Q2 | varchar |  |  | SI | Auscultación |
| Q89Q3 | varchar |  |  | SI | Localización |
| Q89Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*