# questionnaire.QTCEFRQQ11

> Enteral Feeding Regimen : Target Bolus Regimen

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Enteral Feeding Regimen : Target Bolus Regimen

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | time |  |  | SI | Time |
| Q11Q2 | varchar |  |  | SI | Feed / Water |
| Q11Q3 | numeric |  |  | SI | ml |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*