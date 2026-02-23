# questionnaire.QCLXXPCIQQ18

> Plan de Cuidado Integral  : Tratamiento Farmacológico

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral  : Tratamiento Farmacológico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | varchar |  |  | SI | Medicamento  |
| Q18Q2 | varchar |  |  | SI | Dosificación |
| Q18Q3 | varchar |  |  | SI | Posología |
| Q18Q4 | varchar |  |  | SI | Función  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*