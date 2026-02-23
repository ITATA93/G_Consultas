# questionnaire.QTCAHPRHLYQQ68

> Lymphoedema Assessment : Compression garment requirements

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lymphoedema Assessment : Compression garment requirements

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q68Q1 | varchar |  |  | SI | Assessed By |
| Q68Q2 | date |  |  | SI | Date |
| Q68Q3 | varchar |  |  | SI | Order / Garment type |
| Q68Q4 | varchar |  |  | SI | Relevant funding body |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*