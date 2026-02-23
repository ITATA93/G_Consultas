# questionnaire.QTCDWDQQ03

> Perioperative - Dressings and Wound Drainage : Wound drainage

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Dressings and Wound Drainage : Wound drainage

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Drain type |
| Q03Q2 | varchar |  |  | SI | If other please specify |
| Q03Q3 | date |  |  | SI | Expiry date |
| Q03Q4 | numeric |  |  | SI | Lot number |
| Q03Q5 | varchar |  |  | SI | Site |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*