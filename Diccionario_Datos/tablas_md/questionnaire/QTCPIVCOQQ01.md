# questionnaire.QTCPIVCOQQ01

> Peripheral Intravenous Cannula (PIVC) Ongoing Care Record : Peripheral Intravenous Catheter (PIVC)

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peripheral Intravenous Cannula (PIVC) Ongoing Care Record : Peripheral Intravenous Catheter (PIVC)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | date |  |  | SI | Insertion date / time |
| Q01Q10 | varchar |  |  | SI | Nurse / Clinician |
| Q01Q2 | time |  |  | SI | Insertion time |
| Q01Q3 | varchar |  |  | SI | Day/Shift |
| Q01Q4 | varchar |  |  | SI | Visual Infusion Phlebitis (VIP) Score |
| Q01Q5 | varchar |  |  | SI | Site visible |
| Q01Q6 | varchar |  |  | SI | Dressing intact / clean / dated? |
| Q01Q7 | varchar |  |  | SI | Moisture / Leak from site |
| Q01Q8 | varchar |  |  | SI | Flow problems / flushed |
| Q01Q9 | varchar |  |  | SI | Needle-free device / extension in situ |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*