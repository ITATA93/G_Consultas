# questionnaire.QTCEFMENQQINFC25

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : VACUNACIÓN

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : VACUNACIÓN

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q25Q1 | varchar |  |  | SI | Vacunación Hib |
| Q25Q2 | numeric |  |  | SI | N° Dosis Hib |
| Q25Q3 | date |  |  | SI | Fecha Vacuna Hib |
| Q25Q4 | varchar |  |  | SI | Vacunación Neumocóccica |
| Q25Q5 | numeric |  |  | SI | N° Dosis Neumocóccica |
| Q25Q6 | date |  |  | SI | Fecha Vacuna Neumocóccica |
| Q25Q7 | varchar |  |  | SI | Otros |
| Q25Q8 | numeric |  |  | SI | N° Dosis Otros |
| Q25Q9 | date |  |  | SI | Fecha Otros |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*