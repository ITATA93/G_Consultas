# questionnaire.QTCPIVCOQQ06

> Peripheral Intravenous Cannula (PIVC) Ongoing Care Record : Day 4

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peripheral Intravenous Cannula (PIVC) Ongoing Care Record : Day 4

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Insertion date / time |
| Q06Q10 | varchar |  |  | SI | Nurse / Clinician |
| Q06Q2 | time |  |  | SI | Insertion time |
| Q06Q3 | varchar |  |  | SI | Day/Shift |
| Q06Q4 | varchar |  |  | SI | VIP score |
| Q06Q5 | varchar |  |  | SI | Site visible |
| Q06Q6 | varchar |  |  | SI | Dressing intact / clean / dated? |
| Q06Q7 | varchar |  |  | SI | Moisture / Leak from site |
| Q06Q8 | varchar |  |  | SI | Flow problems / flushed |
| Q06Q9 | varchar |  |  | SI | Needle-free device / Extension in situ |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*