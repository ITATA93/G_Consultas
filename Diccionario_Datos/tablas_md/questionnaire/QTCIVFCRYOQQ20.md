# questionnaire.QTCIVFCRYOQQ20

> Cryopreservation : Embryo Thaw

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cryopreservation : Embryo Thaw

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | numeric |  |  | SI | Embryos frozen number |
| Q20Q2 | varchar |  |  | SI | Cells / Grade |
| Q20Q3 | varchar |  |  | SI | Post-thaw day 2 |
| Q20Q4 | varchar |  |  | SI | Post-thaw day 3 |
| Q20Q5 | varchar |  |  | SI | Post-thaw day 4 |
| Q20Q6 | varchar |  |  | SI | Post-thaw day 5 |
| Q20Q7 | varchar |  |  | SI | Transferred |
| Q20Q8 | varchar |  |  | SI | Refrozen |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*