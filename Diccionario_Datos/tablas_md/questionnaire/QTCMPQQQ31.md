# questionnaire.QTCMPQQQ31

> McGill Pain Questionnaire (MPQ) : Pain localization

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* McGill Pain Questionnaire (MPQ) : Pain localization

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q31Q1 | varchar |  |  | SI | Where is your pain? |
| Q31Q2 | varchar |  |  | SI | Which word would you use to describe the pattern o... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*