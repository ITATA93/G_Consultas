# questionnaire.QGXXXWOUNDQQ63

> Wound Management : Wound Physical Assessment

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management : Wound Physical Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q63Q1 | date |  |  | SI | Date |
| Q63Q2 | numeric |  |  | SI | Max length (cm) |
| Q63Q3 | numeric |  |  | SI | Max width (cm) |
| Q63Q4 | numeric |  |  | SI | Max depth (cm) |
| Q63Q5 | numeric |  |  | SI | Area (cm2) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*