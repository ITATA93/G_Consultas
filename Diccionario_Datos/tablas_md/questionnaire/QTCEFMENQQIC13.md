# questionnaire.QTCEFMENQQIC13

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : DIRECCIÓN

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : DIRECCIÓN

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QIC13Q1 | varchar |  |  | SI | Calle |
| QIC13Q2 | varchar |  |  | SI | Número |
| QIC13Q3 | varchar |  |  | SI | Depto |
| QIC13Q4 | varchar |  |  | SI | Provincia, Villa u Otro |
| QIC13Q5 | varchar |  |  | SI | Ciudad o Localidad |
| QIC13Q6 | varchar |  |  | SI | Comuna |
| QIC13Q7 | numeric |  |  | SI | Teléfono |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*