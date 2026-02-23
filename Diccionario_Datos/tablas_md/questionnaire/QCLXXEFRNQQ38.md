# questionnaire.QCLXXEFRNQQ38

> Examen Físico del Recién Nacido : Pulmonar Alterado

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico del Recién Nacido : Pulmonar Alterado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q38Q1 | varchar |  |  | SI | Percusión |
| Q38Q2 | varchar |  |  | SI | Auscultación |
| Q38Q3 | varchar |  |  | SI | Localización |
| Q38Q4 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*