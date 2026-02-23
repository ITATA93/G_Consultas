# questionnaire.QGXXXCDQQ52

> Chest Drain : Daily assessment

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chest Drain : Daily assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q52Q1 | date |  |  | SI | Date |
| Q52Q2 | time |  |  | SI | Time |
| Q52Q3 | varchar |  |  | SI | Staff name |
| Q52Q4 | varchar |  |  | SI | Check |
| Q52Q5 | varchar |  |  | SI | Actions |
| Q52Q6 | varchar |  |  | SI | Daily assessment notes |
| Q52Q7 | varchar |  |  | SI | Drain location |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*