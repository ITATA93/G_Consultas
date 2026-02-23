# questionnaire.QTCEFMENQQDIAG56

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : DIAGNÓSTICOS Y CÓDIGOS CIE-10

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae : DIAGNÓSTICOS Y CÓDIGOS CIE-10

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| QDIAG56Q1 | varchar |  |  | SI | Enfermedad Meningoc. |
| QDIAG56Q2 | varchar |  |  | SI | Meningitis |
| QDIAG56Q3 | varchar |  |  | SI | Enfermedad Invasiva Por Haemophilus Influenzae |
| QDIAG56Q4 | varchar |  |  | SI | Agente |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*