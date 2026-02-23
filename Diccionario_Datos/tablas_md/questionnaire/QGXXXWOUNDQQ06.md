# questionnaire.QGXXXWOUNDQQ06

> Wound Management : Treatment

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management : Treatment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Date |
| Q06Q2 | time |  |  | SI | Time |
| Q06Q3 | varchar |  |  | SI | Pain prevention |
| Q06Q4 | varchar |  |  | SI | Care |
| Q06Q5 | varchar |  |  | SI | Type of dressing |
| Q06Q6 | varchar |  |  | SI | Note |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*