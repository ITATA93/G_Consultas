# questionnaire.QCLXXMCPRAQQ23

> Medidas de contención en Pacientes en Riesgo de Auto o Heterolesión : Control

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medidas de contención en Pacientes en Riesgo de Auto o Heterolesión : Control

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q23Q1 | date |  |  | SI | Fecha Control |
| Q23Q10 | varchar |  |  | SI | Nombre Profesional |
| Q23Q2 | time |  |  | SI | Hora Control |
| Q23Q3 | varchar |  |  | SI | Tipo Contención |
| Q23Q4 | varchar |  |  | SI | Estado Contención |
| Q23Q5 | varchar |  |  | SI | Estado Fijación |
| Q23Q6 | varchar |  |  | SI | Estado Paciente |
| Q23Q7 | varchar |  |  | SI | Perfusión PCTE |
| Q23Q8 | varchar |  |  | SI | Barandas en Alto |
| Q23Q9 | varchar |  |  | SI | Indicación de Contención por Médico en Ficha |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*