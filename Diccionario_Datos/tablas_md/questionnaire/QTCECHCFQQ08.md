# questionnaire.QTCECHCFQQ08

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q08Q10 | varchar | PK |  | SI | Estado Paciente  |
| Q08Q11 | varchar | PK |  | SI | Control Medico  |
| Q08Q12 | time | PK |  | SI | Hora Retiro Sujeciones  |
| Q08Q7 | time | PK |  | SI | Horario Inicio  |
| Q08Q8 | varchar | PK |  | SI | Tipo de Contencion  |
| Q08Q9 | varchar | PK |  | SI | Estado Contencion |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*