# questionnaire.QCLXXSMPCIQQ02

> Plan de Cuidado Integral (PCI) APS / Especialidad : METAS

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral (PCI) APS / Especialidad : METAS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | varchar |  |  | SI | Metas |
| Q02Q2 | varchar |  |  | SI | Logro |
| Q02Q3 | varchar |  |  | SI | Cumplimiento  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*