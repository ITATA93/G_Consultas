# questionnaire.QTCERSMQQ01

> Registro de Sesiones Mixtas : Registro de Actividades

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro de Sesiones Mixtas : Registro de Actividades

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | numeric |  |  | SI | N° Sesión EMPC |
| Q01Q2 | numeric |  |  | SI | N° Sesión EC |
| Q01Q3 | numeric |  |  | SI | N° Sesión AEVS |
| Q01Q4 | numeric |  |  | SI | BORG Modificado |
| Q01Q5 | numeric |  |  | SI | FC en Taller |
| Q01Q6 | varchar |  |  | SI | Registro de la Actividad |
| Q01Q7 | varchar |  |  | SI | Profesional |
| Q01Q8 | date |  |  | SI | Fecha |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*