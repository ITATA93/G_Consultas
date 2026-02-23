# questionnaire.QTCILMQQ18

> Induction of Labour Management : Cervical ripening details and induction

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Induction of Labour Management : Cervical ripening details and induction

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | date |  |  | SI | Date / Time |
| Q18Q2 | time |  |  | SI | Time |
| Q18Q3 | varchar |  |  | SI | Method |
| Q18Q4 | varchar |  |  | SI | Type of balloon catheter |
| Q18Q5 | numeric |  |  | SI | Volume inserted into balloon catheter (ml) |
| Q18Q6 | time |  |  | SI | Time for removal / reassessment |
| Q18Q7 | varchar |  |  | SI | Notes |
| Q18Q8 | varchar |  |  | SI | Care provider |
| Q18Q9 | date |  |  | SI | Date / Time for removal / reassessment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*