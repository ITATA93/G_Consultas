# questionnaire.QTCEHOAMIQQ04

> Hoja de Acompañamiento Paciente Hospitalizado : Cuidador 6 Horas

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hoja de Acompañamiento Paciente Hospitalizado : Cuidador 6 Horas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q04Q10 | varchar |  |  | SI | Servicio Clínico |
| Q04Q11 | bit |  |  | SI | Recibió Alimentación Asistida |
| Q04Q5 | bit |  |  | SI | Turno Mañana 08:00 a 14:00  |
| Q04Q6 | bit |  |  | SI | Turno Tarde 14:00 a 20:00  |
| Q04Q7 | bit |  |  | SI | Turno Noche 20:00 a 08:00  |
| Q04Q8 | varchar |  |  | SI | Nombre del Cuidador |
| Q04Q9 | date |  |  | SI | Fecha  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*