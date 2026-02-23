# questionnaire.QTCEDIRQQ39

> Intubation Record : Intubation

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intubation Record : Intubation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q39Q1 | numeric |  |  | SI | Attempt |
| Q39Q2 | varchar |  |  | SI | Intubator |
| Q39Q3 | varchar |  |  | SI | Intubation experience level |
| Q39Q4 | varchar |  |  | SI | Laryngoscope |
| Q39Q5 | varchar |  |  | SI | Cormack and Lehane grade |
| Q39Q6 | varchar |  |  | SI | External laryngeal manipulation |
| Q39Q7 | varchar |  |  | SI | Cricoid	 |
| Q39Q8 | varchar |  |  | SI | Manual in-line stabilisation |
| Q39Q9 | varchar |  |  | SI | Intubation assisting devices used? |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*