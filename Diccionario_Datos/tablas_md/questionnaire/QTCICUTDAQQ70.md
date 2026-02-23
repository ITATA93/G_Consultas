# questionnaire.QTCICUTDAQQ70

> Tracheostomy Insertion and Care : Tracheostomy tube assessment

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tracheostomy Insertion and Care : Tracheostomy tube assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q70Q1 | date |  |  | SI | Date |
| Q70Q10 | varchar |  |  | SI | Assessed by |
| Q70Q2 | time |  |  | SI | Time |
| Q70Q3 | varchar |  |  | SI | Inner cannula |
| Q70Q4 | varchar |  |  | SI | Dressings and tapes |
| Q70Q5 | varchar |  |  | SI | Cuff pressure checked |
| Q70Q6 | numeric |  |  | SI | Cuff pressure (cmH20) |
| Q70Q7 | varchar |  |  | SI | Humidifier |
| Q70Q8 | varchar |  |  | SI | Emergency equipment in room / available |
| Q70Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*