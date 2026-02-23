# questionnaire.QTCWOUNDMGTQQ71

> Wound Assessment and Care : Sinus Tract, Tunneling, Undermining

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care : Sinus Tract, Tunneling, Undermining

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q71Q1 | varchar |  |  | SI | Type |
| Q71Q2 | varchar |  |  | SI | Number |
| Q71Q3 | numeric |  |  | SI | Length (cm) |
| Q71Q4 | varchar |  |  | SI | O'Clock position |
| Q71Q5 | varchar |  |  | SI | Comments |
| Q71Q6 | varchar |  |  | SI | Entered by |
| Q71Q7 | date |  |  | SI | Date  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*