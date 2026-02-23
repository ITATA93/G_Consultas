# questionnaire.QCLXXPCIQQ09

> Plan de Cuidado Integral  : Plan de intervención Integral

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral  : Plan de intervención Integral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | varchar |  |  | SI | Gestor Terapéutico |
| Q09Q2 | varchar |  |  | SI | OBJETIVO TERAPEUTICO |
| Q09Q3 | varchar |  |  | SI | ACTIVIDAD  |
| Q09Q4 | varchar |  |  | SI | A QUIEN VA DIRIGIDO |
| Q09Q5 | varchar |  |  | SI | QUIEN LO REALIZA |
| Q09Q6 | varchar |  |  | SI | PLAZOS  |
| Q09Q7 | varchar |  |  | SI | CUMPLIMIENTO |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*