# questionnaire.QTCPEGTQQ22

> Percutaneous Endoscopic Gastrostomy Tube (PEG) : PEG assessment

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Percutaneous Endoscopic Gastrostomy Tube (PEG) : PEG assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q22Q1 | date |  |  | SI | Date |
| Q22Q2 | time |  |  | SI | Time |
| Q22Q3 | varchar |  |  | SI | Site inspection |
| Q22Q4 | varchar |  |  | SI | Peri-tube skin integrity |
| Q22Q5 | varchar |  |  | SI | Predisposing factors notes |
| Q22Q6 | varchar |  |  | SI | Site cleaned |
| Q22Q7 | varchar |  |  | SI | Tube rotated 360 degrees |
| Q22Q8 | varchar |  |  | SI | Tube patent |
| Q22Q9 | varchar |  |  | SI | Assessment notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*