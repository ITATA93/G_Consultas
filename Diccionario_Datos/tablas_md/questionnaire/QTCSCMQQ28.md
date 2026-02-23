# questionnaire.QTCSCMQQ28

> Spinal Clearance and Management : Spinal Precautions and Management

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Spinal Clearance and Management : Spinal Precautions and Management

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q28Q1 | date |  |  | SI | Date |
| Q28Q2 | time |  |  | SI | Time |
| Q28Q3 | varchar |  |  | SI | Status of spinal assessment |
| Q28Q4 | varchar |  |  | SI | Spinal precautions required? |
| Q28Q5 | varchar |  |  | SI | Spinal precautions to apply |
| Q28Q6 | varchar |  |  | SI | Precaution details |
| Q28Q7 | varchar |  |  | SI | Care provider |
| Q28Q8 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*