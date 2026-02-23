# questionnaire.QCLXXSMPCIQQ16

> Plan de Cuidado Integral (PCI) APS / Especialidad : OTROS

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral (PCI) APS / Especialidad : OTROS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q16Q1 | varchar |  |  | SI | Objetivos  |
| Q16Q2 | varchar |  |  | SI | Estrategias o Actividades |
| Q16Q3 | varchar |  |  | SI | Responsables |
| Q16Q4 | varchar |  |  | SI | Plazo |
| Q16Q5 | varchar |  |  | SI | Indicador de Logro |
| Q16Q6 | varchar |  |  | SI | Cumplimiento  |
| Q16Q7 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*