# questionnaire.QTCEFMENQQIEP47

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : VISITA EPIDEMIOLÓGICA

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : VISITA EPIDEMIOLÓGICA

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QIEP47Q1 | varchar |  |  | SI | Lugar |
| QIEP47Q2 | date |  |  | SI | Fecha |
| QIEP47Q3 | time |  |  | SI | Hora Inicio |
| QIEP47Q4 | time |  |  | SI | Hora Fin |
| QIEP47Q5 | varchar |  |  | SI | Responsable |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*