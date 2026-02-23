# questionnaire.QGXXXWOUNDQQ08

> Wound Management : Pain Assessment

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management : Pain Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | date |  |  | SI | Date |
| Q08Q2 | time |  |  | SI | Time |
| Q08Q3 | varchar |  |  | SI | Type of pain |
| Q08Q4 | numeric |  |  | SI | Pain scale |
| Q08Q4NEW | varchar |  |  | SI | Pain scale |
| Q08Q5 | varchar |  |  | SI | Note |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*