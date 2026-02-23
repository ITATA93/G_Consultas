# questionnaire.QTCICPCQQ12

> Intracranial Pressure (ICP) Catheter Insertion and Care : Intracranial pressure catheter assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intracranial Pressure (ICP) Catheter Insertion and Care : Intracranial pressure catheter assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q12Q1 | date |  |  | SI | Date |
| Q12Q2 | time |  |  | SI | Time |
| Q12Q3 | varchar |  |  | SI | Dressing status |
| Q12Q4 | varchar |  |  | SI | Insertion site check |
| Q12Q5 | varchar |  |  | SI | Actions performed |
| Q12Q6 | varchar |  |  | SI | Assessment notes |
| Q12Q7 | varchar |  |  | SI | Assessment performed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*