# questionnaire.QTCAAICQQ42

> Artificial Airway Insertion and Care : ETT re-positioning detail

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Artificial Airway Insertion and Care : ETT re-positioning detail

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q42Q1 | date |  |  | SI | Date |
| Q42Q2 | time |  |  | SI | Time |
| Q42Q3 | numeric |  |  | SI | Length of ETT after repositioning (cm) |
| Q42Q4 | varchar |  |  | SI | ETT measured at |
| Q42Q5 | varchar |  |  | SI | Position confirmed by x-ray |
| Q42Q6 | varchar |  |  | SI | Repositioned by |
| Q42Q7 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*