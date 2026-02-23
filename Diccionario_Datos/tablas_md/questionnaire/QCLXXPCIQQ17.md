# questionnaire.QCLXXPCIQQ17

> Plan de Cuidado Integral  : Registro de modificaciones

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral  : Registro de modificaciones

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | date |  |  | SI | Fecha |
| Q17Q2 | varchar |  |  | SI | Modificación   |
| Q17Q3 | numeric |  |  | SI | Página |
| Q17Q4 | varchar |  |  | SI | Aprobado por |
| Q17Q5 | varchar |  |  | SI | Firma Responsable   |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*