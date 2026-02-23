# questionnaire.QTCIVFCRYOQQ19

> Cryopreservation : Straw Details

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cryopreservation : Straw Details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q19Q1 | numeric |  |  | SI | Straw number |
| Q19Q2 | varchar |  |  | SI | Comment |
| Q19Q3 | varchar |  |  | SI | Straw tip color |
| Q19Q4 | varchar |  |  | SI | Pencil color |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*