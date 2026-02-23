# questionnaire.QTCECHCFSMQQ08

> Pauta Registro Contención Física SM : Control Horario de Contención Fisica

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta Registro Contención Física SM : Control Horario de Contención Fisica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q08Q10 | varchar |  |  | SI | Estado Paciente  |
| Q08Q11 | varchar |  |  | SI | Control Medico  |
| Q08Q12 | time |  |  | SI | Hora Retiro Sujeciones  |
| Q08Q14 | varchar |  |  | SI | Profesional |
| Q08Q15 | varchar |  |  | SI | Revisión |
| Q08Q16 | varchar |  |  | SI | Prevención de Eventos Adversos |
| Q08Q7 | time |  |  | SI | Horario Inicio  |
| Q08Q8 | varchar |  |  | SI | Tipo de Contención  |
| Q08Q9 | varchar |  |  | SI | Estado Contención |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*