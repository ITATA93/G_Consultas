# questionnaire.QTCEFRQQ09

> Enteral Feeding Regimen : Starting Bolus Regimen

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Enteral Feeding Regimen : Starting Bolus Regimen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | date |  |  | SI | Date |
| Q09Q2 | time |  |  | SI | Time |
| Q09Q3 | numeric |  |  | SI | ml |
| Q09Q4 | varchar |  |  | SI | Overnight (ml/hr) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*