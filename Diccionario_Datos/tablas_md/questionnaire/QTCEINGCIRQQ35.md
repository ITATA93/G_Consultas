# questionnaire.QTCEINGCIRQQ35

> Ingreso Cirugía : Pulmonar

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Cirugía : Pulmonar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q35Q1 | varchar |  |  | SI | Percusión |
| Q35Q2 | varchar |  |  | SI | Auscultación |
| Q35Q3 | varchar |  |  | SI | Localización |
| Q35Q4 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*