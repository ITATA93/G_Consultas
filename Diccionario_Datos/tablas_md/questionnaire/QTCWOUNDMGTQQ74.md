# questionnaire.QTCWOUNDMGTQQ74

> Wound Assessment and Care : Pain Assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Pain Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q74Q1 | date |  |  | SI | Date |
| Q74Q2 | time |  |  | SI | Time |
| Q74Q3 | varchar |  |  | SI | When |
| Q74Q4 | varchar |  |  | SI | Pain medication status |
| Q74Q5 | varchar |  |  | SI | Description |
| Q74Q6 | varchar |  |  | SI | Patient scale |
| Q74Q7 | varchar |  |  | SI | Pain comments |
| Q74Q8 | varchar |  |  | SI | Entered by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*