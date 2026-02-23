# questionnaire.QTCUCICQQ28

> Urinary Catheter Insertion and Care : Assessment

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Urinary Catheter Insertion and Care : Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q28Q1 | date |  |  | SI | Assessment date |
| Q28Q10 | date |  |  | SI | Due date for catheter bag change |
| Q28Q2 | time |  |  | SI | Assessment time |
| Q28Q3 | varchar |  |  | SI | Can urinary catheter be removed? |
| Q28Q4 | varchar |  |  | SI | Indication for continued catheter |
| Q28Q5 | varchar |  |  | SI | Insertion site  check |
| Q28Q6 | varchar |  |  | SI | Catheter check |
| Q28Q7 | varchar |  |  | SI | Actions performed |
| Q28Q8 | varchar |  |  | SI | Assessment notes |
| Q28Q9 | varchar |  |  | SI | Assessment performed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*