# questionnaire.QTCELVFQQ01

> Línea de Vida Familiar : Registro de Eventos o Acontecimientos

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Línea de Vida Familiar : Registro de Eventos o Acontecimientos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | date |  |  | SI | Fecha del Evento |
| Q01Q2 | varchar |  |  | SI | Descripción del Evento |
| Q01Q3 | date |  |  | SI | Fecha de Registro |
| Q01Q4 | time |  |  | SI | Hora de Registro |
| Q01Q5 | varchar |  |  | SI | Profesional que Registra |
| Q01Q6 | varchar |  |  | SI | CESFAM |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*