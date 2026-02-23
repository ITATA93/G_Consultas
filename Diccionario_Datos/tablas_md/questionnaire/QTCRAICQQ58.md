# questionnaire.QTCRAICQQ58

> Regional Anaesthesia Insertion and Care : Insertion site assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Regional Anaesthesia Insertion and Care : Insertion site assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q58Q1 | varchar |  |  | SI | Insertion site checks |
| Q58Q2 | varchar |  |  | SI | Catheter check |
| Q58Q3 | varchar |  |  | SI | Dressing status |
| Q58Q4 | varchar |  |  | SI | Actions performed |
| Q58Q5 | varchar |  |  | SI | Assessment notes |
| Q58Q6 | varchar |  |  | SI | Assessment performed by  |
| Q58Q7 | date |  |  | SI | Date |
| Q58Q8 | time |  |  | SI | Time |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*