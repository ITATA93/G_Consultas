# questionnaire.QTCAAICQQ32

> Artificial Airway Insertion and Care : Additional intubation attempt details

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Artificial Airway Insertion and Care : Additional intubation attempt details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q32Q1 | varchar |  |  | SI | Airway device |
| Q32Q2 | varchar |  |  | SI | Device size |
| Q32Q3 | varchar |  |  | SI | Laryngoscope |
| Q32Q4 | varchar |  |  | SI | Blade details |
| Q32Q5 | varchar |  |  | SI | Grade of view |
| Q32Q6 | varchar |  |  | SI | Airway adjuncts |
| Q32Q7 | varchar |  |  | SI | Insertion location |
| Q32Q8 | varchar |  |  | SI | Notes |
| Q32Q9 | varchar |  |  | SI | Attempted by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*