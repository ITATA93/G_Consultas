# questionnaire.QTCIVFESSQQ05

> Embryology Summary Sheet : Embryo transfer

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Embryology Summary Sheet : Embryo transfer

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | date |  |  | SI | Date of embryo transfer |
| Q05Q2 | numeric |  |  | SI | No. transfered |
| Q05Q3 | numeric |  |  | SI | No. frozen |
| Q05Q4 | numeric |  |  | SI | No. discarded |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*