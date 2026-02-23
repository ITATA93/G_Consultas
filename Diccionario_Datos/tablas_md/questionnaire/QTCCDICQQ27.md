# questionnaire.QTCCDICQQ27

> Chest Drain Insertion and Care : Chest drain assessment

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chest Drain Insertion and Care : Chest drain assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q27Q1 | date |  |  | SI | Date |
| Q27Q2 | time |  |  | SI | Time |
| Q27Q3 | varchar |  |  | SI | Drain name |
| Q27Q4 | varchar |  |  | SI | Insertion site check |
| Q27Q5 | varchar |  |  | SI | Dressing status |
| Q27Q6 | varchar |  |  | SI | Actions performed |
| Q27Q7 | varchar |  |  | SI | Assessment notes |
| Q27Q8 | varchar |  |  | SI | Assessment performed by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*