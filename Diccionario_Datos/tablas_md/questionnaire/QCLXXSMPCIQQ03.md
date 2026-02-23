# questionnaire.QCLXXSMPCIQQ03

> Plan de Cuidado Integral (PCI) APS / Especialidad : INDIVIDUAL

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral (PCI) APS / Especialidad : INDIVIDUAL

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Objetivos |
| Q03Q2 | varchar |  |  | SI | Estrategias o Actividades |
| Q03Q3 | varchar |  |  | SI | Responsables |
| Q03Q4 | varchar |  |  | SI | Plazo |
| Q03Q5 | varchar |  |  | SI | Indicador de Logro |
| Q03Q6 | varchar |  |  | SI | Cumplimiento  |
| Q03Q7 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*