# questionnaire.QTCEHOAMIQQ02

> Hoja de Acompañamiento Paciente Hospitalizado : Cuidador 24 Horas

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hoja de Acompañamiento Paciente Hospitalizado : Cuidador 24 Horas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q02Q1 | bit |  |  | SI | Turno Mañana 08:00 a 14:00 |
| Q02Q2 | bit |  |  | SI | Turno Tarde 14:00 a 20:00 |
| Q02Q3 | bit |  |  | SI | Turno Noche 20:00 a 08:00  |
| Q02Q4 | varchar |  |  | SI | Nombre del Cuidador |
| Q02Q5 | date |  |  | SI | Fecha |
| Q02Q6 | varchar |  |  | SI | Servicio Clínico |
| Q02Q7 | bit |  |  | SI | Recibió Alimentación Asistida |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*