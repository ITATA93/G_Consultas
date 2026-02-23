# questionnaire.QTCEINGUPCQQ58

> INGRESO UNIDAD DE PACIENTE CRÍTICO : Pulmonar

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO : Pulmonar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q58Q1 | varchar |  |  | SI | Percusión |
| Q58Q2 | varchar |  |  | SI | Auscultación |
| Q58Q3 | varchar |  |  | SI | Localización |
| Q58Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*