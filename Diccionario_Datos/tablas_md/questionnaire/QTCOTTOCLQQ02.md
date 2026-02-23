# questionnaire.QTCOTTOCLQQ02

> Perioperative - Tourniquet and Clamp Details : Tourniquet

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Tourniquet and Clamp Details : Tourniquet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Tourniquet applied |
| Q02Q2 | varchar |  |  | SI | Body site |
| Q02Q3 | varchar |  |  | SI | Side |
| Q02Q4 | numeric |  |  | SI | Pressure (mmHg) |
| Q02Q5 | time |  |  | SI | Inflated time |
| Q02Q6 | time |  |  | SI | Deflated time |
| Q02Q7 | numeric |  |  | SI | Total tourniquet time |
| Q02Q8 | varchar |  |  | SI | Body site |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*