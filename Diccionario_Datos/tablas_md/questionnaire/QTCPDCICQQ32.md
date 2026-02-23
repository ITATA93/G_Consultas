# questionnaire.QTCPDCICQQ32

> Peritoneal Dialysis Catheter Insertion and Care : Line change details

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Catheter Insertion and Care : Line change details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | date |  |  | SI | Date |
| Q32Q2 | time |  |  | SI | Time |
| Q32Q3 | varchar |  |  | SI | Indication for line change |
| Q32Q4 | varchar |  |  | SI | Other indication for PD line change |
| Q32Q5 | date |  |  | SI | Next line change due |
| Q32Q6 | varchar |  |  | SI | Line change notes |
| Q32Q7 | varchar |  |  | SI | Changed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*