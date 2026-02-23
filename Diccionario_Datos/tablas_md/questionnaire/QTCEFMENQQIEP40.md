# questionnaire.QTCEFMENQQIEP40

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : GRUPOS ESPECÍFICOS

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : GRUPOS ESPECÍFICOS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QIEP40Q1 | varchar |  |  | SI | Grupos  |
| QIEP40Q2 | varchar |  |  | SI | N° de Contactos 0 a 4 Años |
| QIEP40Q3 | varchar |  |  | SI | N° de Contactos 5 a 17 Años  |
| QIEP40Q4 | varchar |  |  | SI | N° de Contactos > 18 Años |
| QIEP40Q5 | varchar |  |  | SI | N° de Contactos Gestantes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*