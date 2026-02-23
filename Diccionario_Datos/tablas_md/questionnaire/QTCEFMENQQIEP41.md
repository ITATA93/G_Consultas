# questionnaire.QTCEFMENQQIEP41

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : QUIMIOPROFILAXIS CIPROFLOXACINO

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : QUIMIOPROFILAXIS CIPROFLOXACINO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QIE40Q1 | numeric |  |  | SI | N° Cáp. Ciprofloxacino (0 a 4 Años) |
| QIE40Q2 | numeric |  |  | SI | N° Cáp. Ciprofloxacino (5 a 17 Años) |
| QIE40Q3 | numeric |  |  | SI | N° Cáp. Ciprofloxacino (> 18 Años) |
| QIE40Q4 | numeric |  |  | SI | N° Cáp. Ciprofloxacino (Gestantes) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*