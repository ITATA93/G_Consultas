# questionnaire.QTCEPLANCQQ08

> Plan Consensuado : Factores de Riesgo y Protectores

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan Consensuado : Factores de Riesgo y Protectores

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q1 | varchar |  |  | SI | Factores de Riesgo |
| Q08Q2 | varchar |  |  | SI | Factores Protectores |
| Q08Q3 | date |  |  | SI | Fecha |
| Q08Q4 | varchar |  |  | SI | Profesional |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*