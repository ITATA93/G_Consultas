# questionnaire.QGXXXWOUNDQQ05

> Wound Management : Evaluation

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management : Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q05Q1 | date |  |  | SI | Date |
| Q05Q10 | varchar |  |  | SI | Skin colour surrounding wound |
| Q05Q11 | varchar |  |  | SI | Granulation tissue |
| Q05Q15 | varchar |  |  | SI | Note |
| Q05Q2 | varchar |  |  | SI | Size (length, width and depth) |
| Q05Q3 | varchar |  |  | SI | Stage of pressure injury |
| Q05Q4 | varchar |  |  | SI | Edges |
| Q05Q5 | varchar |  |  | SI | Undermining |
| Q05Q6 | varchar |  |  | SI | Exudate |
| Q05Q6a | varchar |  |  | SI | Wound infection |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*